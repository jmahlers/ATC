import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D

# Create a grid - only half angle to see interior
x = np.linspace(-3, 3, 100)
y = np.linspace(0, 3, 100)  # Only positive y to show half
X, Y = np.meshgrid(x, y)
r_squared = X**2 + Y**2

# Number of frames
n_frames = 30

# Parameter that controls the central hump height
# mu^2 goes from negative (symmetry broken) to positive (symmetric)
mu_squared_values = np.linspace(-0.5, 3, n_frames)

# Maximum height to display on surface
max_height = 3.0

# Set up the figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")


def update(frame):
    ax.clear()

    # Sombrero potential: V = -mu^2 * r^2 + lambda * r^4
    # When mu^2 < 0: minimum at r=0 (no symmetry breaking)
    # When mu^2 > 0: minimum at r = sqrt(mu^2/(2*lambda)) (symmetry broken)
    mu_sq = mu_squared_values[frame]
    lambda_param = 0.5

    V = -mu_sq * r_squared + lambda_param * r_squared**2

    # Smooth cutoff using a sigmoid function
    V_masked = np.copy(V)
    cutoff_height = 3.0
    smoothness = 0.5  # Controls transition width (smaller = sharper)

    # Create smooth transition: 1 where V < cutoff, 0 where V > cutoff
    smooth_mask = 1 / (1 + np.exp((V - cutoff_height) / smoothness))
    V_masked = V_masked * smooth_mask
    V_masked[smooth_mask < 0.01] = np.nan  # Hide nearly zero values

    # Plot surface
    surf = ax.plot_surface(
        X, Y, V_masked, cmap="viridis", alpha=0.8, linewidth=0, antialiased=True
    )

    # Set labels and title
    ax.set_xlabel("φ₁", fontsize=12)
    ax.set_ylabel("φ₂", fontsize=12)
    ax.set_zlabel("V(φ)", fontsize=12)
    ax.set_title(f"Sombrero Potential: μ² = {mu_sq:.2f}", fontsize=14)

    # Set consistent z-limits for smooth animation
    ax.set_zlim(-3, 4)
    ax.set_xlim(-3, 3)
    ax.set_ylim(0, 3)

    # Fixed viewing angle to see the cross-section
    ax.view_init(elev=20, azim=-90)

    return (surf,)


# Create animation
anim = FuncAnimation(fig, update, frames=n_frames, interval=100, blit=False)

# Save as GIF
writer = PillowWriter(fps=10)
anim.save("sombrero_potential.gif", writer=writer)
print("Animation saved as 'sombrero_potential.gif'")

plt.close()
