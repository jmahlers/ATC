import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from mpl_toolkits.mplot3d import Axes3D

# Create figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create mesh grid
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)

# Animation setup
n_frames = 60
writer = PillowWriter(fps=30)
writer.setup(fig, "sombrero_symmetry_breaking.gif", dpi=100)

# Animate from hump to valley
for frame in range(n_frames):
    ax.clear()
    
    # Interpolate mu parameter from positive (hump) to negative (valley)
    mu = 2.0 - (frame / n_frames) * 2.5
    
    # Sombrero potential: V(r) = mu * r^2 + lambda * r^4
    r_squared = X**2 + Y**2
    Z = mu * r_squared + r_squared**2
    
    # Plot surface
    surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('V(x,y)')
    ax.set_title(f'Sombrero Potential (μ={mu:.2f})')
    ax.set_zlim(-5, 20)
    ax.view_init(elev=25, azim=45)
    
    writer.grab_frame()

writer.finish()
print("GIF saved as 'sombrero_symmetry_breaking.gif'")