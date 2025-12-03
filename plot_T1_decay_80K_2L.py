"""
Plot T1 decay data with error bars and stretched exponential fit.

- Data: T1_T=80K_2L.csv (columns: time, signal, error)
- Plot: error bars only (no connecting lines)
- Fit: Stretched exponential S(t) = A * exp(-(t/tau)^beta) + C
- Title: Longitudinal Decay (T1)
- Note: 80 K 2 Layer CrSBr
- Publication-ready: 300 DPI, transparent, tight bbox
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import argparse

# Toggle: show fit parameters in legend (default True). Use --hide-params to disable.
SHOW_PARAMS_DEFAULT = False

# Stretched exponential function (no offset): S(t) = A * exp(-(t/tau)^gamma)
def stretched_exp(t, A, tau, gamma):
    return A * np.exp(- (t / tau) ** gamma)

# Load data (assume 3 columns: time, signal, error)
data = np.loadtxt('img/T1_T=80K_2L.csv', delimiter=',', skiprows=1)
# Data units: time in milliseconds; convert to microseconds for plotting and fitting
time_ms = data[:, 0]
time_us = time_ms * 1000.0
signal = data[:, 1]
error = data[:, 2]

# Initial parameter guesses: A, tau (µs), gamma
A0 = signal.max()  # amplitude near max polarization
tau0 = (time_us.max() - time_us.min()) / 2
gamma0 = 1.0
p0 = [A0, tau0, gamma0]

# Fit (units: time in microseconds)
popt, pcov = curve_fit(stretched_exp, time_us, signal, sigma=error, p0=p0, absolute_sigma=True, maxfev=10000)
A_fit, tau_fit, gamma_fit = popt
perr = np.sqrt(np.diag(pcov))  # parameter uncertainties

# Generate fit curve (in microseconds for x-axis)
fit_time_us = np.linspace(time_us.min(), time_us.max(), 200)
fit_signal = stretched_exp(fit_time_us, *popt)

# Plot
plt.figure(figsize=(10, 7))
plt.errorbar(time_us, signal, yerr=error, fmt='o', color='tab:blue', ecolor='gray', capsize=3, markersize=8, label='Data')

# Fit legend text with units and uncertainties
# Render using independent variable as tau and characteristic time as T_1
eq_legend = "$S(\\tau)=A\\,e^{-\\left(\\frac{\\tau}{T_{1}}\\right)^{\\gamma}}$"
params_legend = (
    f"$A={A_fit:.3g}\\pm{perr[0]:.2g}$\n"
    f"$T_{1}={tau_fit:.3g}\\pm{perr[1]:.2g}\\,\\mu s$\n"
    f"$\\gamma={gamma_fit:.3g}\\pm{perr[2]:.2g}$"
)
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument('--hide-params', action='store_true', help='Hide fit parameters in legend')
args, _ = parser.parse_known_args()
show_params = SHOW_PARAMS_DEFAULT and not args.hide_params
fit_label = eq_legend if not show_params else (eq_legend + "\n" + params_legend)
plt.plot(fit_time_us, fit_signal, color='crimson', lw=2.5, label=fit_label)

plt.title(r'Longitudinal Decay ($T_1$)', fontsize=34)
plt.xlabel(r'$\tau$ (µs)', fontsize=40)
plt.ylabel('Polarization', fontsize=40)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=32)
plt.grid(alpha=0.3, linestyle='--')

# Removed sample note per request

# Fit equation and values with errors
# Move parameter reporting into legend; no separate annotation

plt.tight_layout()
plt.savefig('img/T1_decay_80K_2L.png', dpi=300, transparent=True, bbox_inches='tight')
plt.show()
