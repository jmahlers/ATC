import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Ellipsoid semi-axes (horizontal, horizontal, vertical)
a, b, c = 0.5, 0.5, 1.0

# Angle (degrees) measured from the vertical (z) axis to draw contour rings
angle_from_vertical = 54.7

# Scale factor to enlarge contour rings for visibility
scale_factor = 1.01

# Create mesh grid for the ellipsoid surface
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = a * np.outer(np.cos(u), np.sin(v))
y = b * np.outer(np.sin(u), np.sin(v))
z = c * np.outer(np.ones_like(u), np.cos(v))

# Create figure and 3D axis
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the ellipsoid surface
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.7, linewidth=0, edgecolor='none')

# Prepare contour rings as line plots
theta = np.radians(angle_from_vertical)
u_contour = np.linspace(0, 2 * np.pi, 200)

x_contour = scale_factor * a * np.cos(u_contour) * np.sin(theta)
y_contour = scale_factor * b * np.sin(u_contour) * np.sin(theta)
z_contour_pos = scale_factor * c * np.cos(theta) * np.ones_like(u_contour)
z_contour_neg = -z_contour_pos

# Plot contour lines
#ax.plot(x_contour, y_contour, z_contour_pos, 'r-', linewidth=3, label=f'+{angle_from_vertical:.1f}°')
#ax.plot(x_contour, y_contour, z_contour_neg, 'r--', linewidth=3, label=f'-{angle_from_vertical:.1f}°')

# Compute centered, equal axis limits
mid_x = 0.5 * (x.max() + x.min())
mid_y = 0.5 * (y.max() + y.min())
mid_z = 0.5 * (z.max() + z.min())
max_range = 0.5 * np.max([x.max() - x.min(), y.max() - y.min(), z.max() - z.min()])

ax.set_xlim(mid_x - max_range, mid_x + max_range)
ax.set_ylim(mid_y - max_range, mid_y + max_range)
ax.set_zlim(mid_z - max_range, mid_z + max_range)

# Labels and title
ax.set_xlabel('Bx Magnetic Field (T)', fontsize=12, fontweight='bold')
ax.set_ylabel('By Magnetic Field (T)', fontsize=12, fontweight='bold')
ax.set_zlabel('Bz Magnetic Field Radius (T)', fontsize=12, fontweight='bold')
ax.set_title('Accessible Magnetic Field LTSPM3', fontsize=16, fontweight='bold')

#plt.subplots_adjust(top=0.7)
plt.show()
