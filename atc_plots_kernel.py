import numpy as np
from scipy.optimize import fminbound

import matplotlib.pyplot as plt

def f(q, d):
    return q**3 * np.exp(-2*q*d)

# Create a grid of q and d values
q = np.linspace(0.5, 8, 200)
d = np.linspace(0.5, 1.5, 200)
Q, D = np.meshgrid(q, d)
Z = f(Q, D)

# Plot
fig, ax = plt.subplots(figsize=(10, 7))
contour = ax.contourf(Q, D, Z, levels=30, cmap='plasma')
ax.contour(Q, D, Z, levels=10, colors='black', alpha=0.3, linewidths=0.5)

# Find and plot the maximum curve
d_vals = np.linspace(0.5, 1.5, 200)
q_max_vals = []
for d_val in d_vals:
    # Find q that maximizes f(q, d) for this d
    q_max = fminbound(lambda q: -f(q, d_val), 0.5, 8)
    q_max_vals.append(q_max)

ax.plot(q_max_vals, d_vals, 'r-', linewidth=2.5, label='Maximum (Slope = -1)')

# Calculate slope in log-log space
log_q = np.log10(q_max_vals)
log_d = np.log10(d_vals)
slope = np.polyfit(log_q, log_d, 1)[0]
# print(f"Slope in log-log space: {slope:.4f}")

ax.set_xlabel('Momentum Coordinate: q', fontsize=20, fontweight='bold', labelpad=15)
ax.set_ylabel('Qubit Distance: d', fontsize=20, fontweight='bold', labelpad=15)
ax.set_title(r'Momentum Filter Function', fontsize=24, fontweight='bold')
ax.set_xscale('log')
ax.set_yscale('log')
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])
ax.xaxis.set_ticklabels([])
ax.yaxis.set_ticklabels([])
# Add back tick marks (no labels)
ax.tick_params(axis='both', which='major', length=10, width=2, labelleft=False, labelbottom=False)
ax.tick_params(axis='both', which='minor', length=6, width=1.5, labelleft=False, labelbottom=False)
ax.grid(True, alpha=0.3, linestyle='--', which='both')
ax.legend(loc='upper right', fontsize=14)

cbar = fig.colorbar(contour, ax=ax, label=r'$f(q,d) = q^3 e^{-2qd}$')
cbar.set_label(r'$F(q,d)$', fontsize=22)
cbar.ax.set_yticklabels([])
plt.tight_layout()
# Save the figure with a transparent background
plt.savefig(r'./img/filter_function.png', transparent=True)
plt.show()