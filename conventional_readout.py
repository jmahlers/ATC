import numpy as np
from dataclasses import dataclass

import matplotlib.pyplot as plt

@dataclass
class AcquisitionParams:
    """Parameters for acquisition system"""
    photon_count_rate: float  # photons/second
    readout_time: float  # seconds
    contrast: float  # signal visibility (0-1)
    
    def photons_per_readout(self):
        """Calculate expected photons per readout"""
        return self.photon_count_rate * self.readout_time

def calculate_time_to_snr(params: AcquisitionParams, evolution_time: float, target_snr: float) -> float:
    """
    Calculate acquisition time needed to achieve target SNR.
    
    Signal: contrast * photons_per_readout
    Noise: sqrt(photons_per_readout) (shot noise)
    SNR per readout = signal / noise = contrast * sqrt(photons_per_readout)
    
    To achieve target_snr, need n readouts where:
    target_snr = sqrt(n) * SNR_per_readout
    
    Args:
        params: AcquisitionParams object
        evolution_time: time spent evolving the system (not counted in acquisition)
        target_snr: desired signal-to-noise ratio
        
    Returns:
        Total time including evolution time to achieve target SNR
    """
    photons = params.photons_per_readout()
    snr_per_readout = params.contrast * np.sqrt(photons)*1/np.sqrt(2)  # factor of sqrt(2) for difference measurement
    
    # Number of readouts needed
    n_readouts = (target_snr / snr_per_readout) ** 2
    
    # Total acquisition time
    acquisition_time = n_readouts * params.readout_time
    
    # Total time including evolution
    total_time = evolution_time*n_readouts + acquisition_time
    
    return total_time

# Example usage
if __name__ == "__main__":
    # System parameters
    system_params = AcquisitionParams(
        photon_count_rate=50e3,  # 1 MHz
        readout_time=1e-6,      # 1 ms
        contrast=0.30            # 50% contrast
    )

    target_snr = 5

    # Array of evolution times
    evolution_times = np.linspace(0, 1e-1, 100)  # 0 to 1 second

    # Calculate time to SNR for each evolution time
    times_to_snr = np.array([
        calculate_time_to_snr(system_params, evo_time, target_snr)
        for evo_time in evolution_times
    ])

    # Plot results
    plt.figure(figsize=(10, 6))
    plt.plot(evolution_times*1e3, times_to_snr/60, linewidth=2)
    plt.xlabel("Evolution Time (ms)")
    plt.ylabel("Total Averaging Time (min)")
    plt.title(r"Total Averaging Time to Achieve $\sigma = 5$")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()

    system_params = AcquisitionParams(
        photon_count_rate=200e3,  # 1 MHz
        readout_time=1e-6,  # 1 ms
        contrast=0.30  # 50% contrast
    )
    # Calculate time to SNR for each evolution time
    times_to_snr = np.array(
        [
            calculate_time_to_snr(system_params, evo_time, target_snr)
            for evo_time in evolution_times
        ]
    )
    plt.plot(evolution_times * 1e3, times_to_snr / 60, linewidth=2)
    system_params = AcquisitionParams(
        photon_count_rate=1500e3,  # 1 MHz
        readout_time=1e-6,      # 1 ms
        contrast=0.08            # 50% contrast
    )
    # Calculate time to SNR for each evolution time
    times_to_snr = np.array(
        [
            calculate_time_to_snr(system_params, evo_time, target_snr)
            for evo_time in evolution_times
        ]
    )

    plt.plot(evolution_times * 1e3, times_to_snr / 60, linewidth=2)
    plt.legend(
        [
            "50k cps, 30% contrast (single NV)",
            "200k cps, 30% contrast (single NV - Pillared)",
            "1.5M cps, 8% contrast (L035 Ensemble)",
        ]
    )
    plt.savefig(
        "total_averaging_time.png", transparent=True, dpi=600, bbox_inches="tight"
    )
    plt.show(block=False)
    # Additional illustration: horizontal levels and arrows (saved separately)
    fig, ax = plt.subplots(figsize=(2, 10))  # narrower width

    contrast_example = 0.30  # choose contrast to illustrate (adjust if needed)
    y_top = 1.0
    y_bottom = 1.0 - contrast_example
    y_mid = 0.93
    xmin, xmax = 0.0, 1.0

    ax.hlines([y_top, y_mid, y_bottom], xmin, xmax,
              colors=['black', 'gray', 'black'],
              linestyles=['-', '--', '-'], linewidth=2)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0 - 0.05, 1 + 0.05)
    ax.set_xticks([])

    # make axis text larger and bold
    ylabel_fs = 16
    tick_fs = 14
    ax.set_ylabel("Normalized PL Signal", fontsize=ylabel_fs, fontweight="bold")
    ax.tick_params(axis='y', labelsize=tick_fs)

    x_arrow = 0.5
    # Arrow between top and mid labeled P1
    ax.annotate('', xy=(x_arrow, y_mid), xytext=(x_arrow, y_top),
                arrowprops=dict(arrowstyle='<->', lw=2.5, color='red'))
    ax.text(x_arrow + 0.02, (y_top + y_mid) / 2, r'$P_1$',
            color='red', va='center', fontsize=14, fontweight='bold')

    # Arrow between mid and bottom labeled P0
    ax.annotate('', xy=(x_arrow, y_bottom), xytext=(x_arrow, y_mid),
                arrowprops=dict(arrowstyle='<->', lw=2.5, color='blue'))
    ax.text(x_arrow + 0.02, (y_mid + y_bottom) / 2, r'$P_0$',
            color='blue', va='center', fontsize=14, fontweight='bold')

    fig.tight_layout()
    fig.savefig("levels_and_P0_P1.png", transparent=True, dpi=300, bbox_inches="tight")

    plt.show()
