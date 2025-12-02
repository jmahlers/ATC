import numpy as np

import matplotlib.pyplot as plt

def delta_function(x, center, width, amplitude=1.0):
    """
    Approximates a delta function using a Gaussian.
    
    Parameters:
    -----------
    x : array-like
        Input values
    center : float
        Center position of the delta function
    width : float
        Width of the delta function (standard deviation of Gaussian)
    amplitude : float
        Peak amplitude of the delta function
    
    Returns:
    --------
    array-like
        Delta function approximation values
    """
    sigma = width / (2 * np.sqrt(2 * np.log(2)))  # Convert FWHM to sigma
    return amplitude * np.exp(-((x - center) ** 2) / (2 * sigma ** 2))


if __name__ == "__main__":
    # Create x values
    x = np.linspace(0, 2, 1000)
    
    # Delta function parameters
    center = 1.0
    width = 0.10  # 10% width (was 0.05)
    amplitude = 1.0
    
    # Calculate delta function
    y = delta_function(x, center, width, amplitude)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(9, 7))
    
    # Plot delta function
    ax.plot(x, y, 'b-', linewidth=2)
    
    # Set labels
    ax.set_xlabel(r'$\frac{\omega}{\omega_0}$', fontsize=32)
    ax.set_ylabel('Temporal-Frequency Filter Function', fontsize=24)
    
    # Hide y-axis tick marks
    ax.yaxis.set_ticks([])
    
    # Add double-sided arrow at half amplitude
    half_amplitude = amplitude / 2
    arrow_left = center - width / 1.95
    arrow_right = center + width / 1.95
    

    # Draw double-sided arrow
    ax.annotate(
        '',
        xy=(arrow_right, half_amplitude),
        xytext=(arrow_left, half_amplitude),
        arrowprops=dict(arrowstyle='<->', color='black', lw=2.2)
    )
    ax.text(
        center + width*1.15,
        half_amplitude-0.07,
        r'$\frac{1}{T_{2}^{*}\!\!}$',
        fontsize=32,
        ha='center',
        va='bottom'
    )
    
    # Set axis limits
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 1.1)
    
    ax.grid(True, alpha=0.35, linestyle='--')
    
    plt.tight_layout()
    fig.savefig("delta_function.png", transparent=True, dpi=300, bbox_inches="tight")
    plt.show()