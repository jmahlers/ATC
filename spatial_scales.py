import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, NullFormatter
from matplotlib.patches import Patch

# Create figure with two vertically stacked subplots sharing x-axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True, 
                                gridspec_kw={'height_ratios': [1, 1], 'hspace': 0.5})

# Define spatial scale range
x_min = 1e-9  # 1 nm
x_max = 1e-3  # 1 mm

# ============== UPPER PLOT: Phenomena Length Scales ==============
ax1.set_xscale('log')
ax1.set_xlim(x_min, x_max)
ax1.set_ylim(0, 0.55)

# Remove spines
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(True)
ax1.spines['bottom'].set_linewidth(3)
ax1.spines['bottom'].set_color('black')

# Remove y-axis
ax1.yaxis.set_visible(False)

# Disable automatic tick labels
ax1.tick_params(axis='x', which='both', labelbottom=False)

# Set major tick positions (no labels)
tick_positions = [1e-9, 1e-6, 1e-3]
ax1.xaxis.set_major_locator(FixedLocator(tick_positions))
ax1.xaxis.set_major_formatter(NullFormatter())
ax1.tick_params(axis='x', which='major', length=25, width=3, pad=15, direction='out', top=False)

# Decade and minor ticks
decade_ticks = [1e-8, 1e-7, 1e-5, 1e-4]
minor_ticks = []
for exp in range(-9, -2):
    for sub in range(2, 10):
        minor_ticks.append(sub * 10**exp)

for tick in decade_ticks:
    ax1.plot([tick, tick], [0, -0.02], color='black', linewidth=1.5, clip_on=False, transform=ax1.get_xaxis_transform())

for tick in minor_ticks:
    if x_min <= tick <= x_max:
        ax1.plot([tick, tick], [0, -0.035], color='black', linewidth=1.5, clip_on=False, transform=ax1.get_xaxis_transform())

ax1.xaxis.set_minor_locator(FixedLocator([]))
ax1.xaxis.set_minor_formatter(NullFormatter())

# Grid lines
ax1.grid(True, which='major', axis='x', alpha=0.4, linestyle='-', linewidth=1.5, color='gray')
ax1.set_axisbelow(True)

# Title for upper plot
ax1.set_title('Phenomena Length Scales', fontsize=36, fontweight='bold', pad=20)

"""Superconducting Vortices length scales: coherence length (ξ) and London penetration depth (λ_L)."""
# Superconducting Vortices bar with two fill regions
# ξ segment: 1 nm to 15 nm
xi_start = 1e-9
xi_end = 15e-9
# λ_L segment: 50 nm to 500 nm
lambda_start = 50e-9
lambda_end = 500e-9

sv_y = 0.48
sv_height = 0.11

# ξ segment (gray fill)
ax1.barh(sv_y, xi_end - xi_start, left=xi_start, height=sv_height,
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

# λ_L segment (solid fill)
ax1.barh(sv_y, lambda_end - lambda_start, left=lambda_start, height=sv_height,
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

# Main label
ax1.text(x_max/1.3, sv_y - 0.005, 'SC Vortices',
         fontsize=28, ha='right', va='center', color='black')

# Segment annotations (placed at left side of boxes)
ax1.text(xi_start * 1.5, sv_y - 0.005, r'$\xi_c$', fontsize=24, ha='left', va='center', color='black')
ax1.text(lambda_start * 1.2, sv_y - 0.005, r'$\lambda_{L}$', fontsize=24, ha='left', va='center', color='black')

"""Electron Transport length scales: mean free path (l_mc) and momentum relaxation (l_mr)."""
# e^- Transport bar spanning from 80 nm to 10 μm
et_start = 80e-9   # 80 nm
et_end = 10e-6      # 10 μm

et_y = 0.22
et_height = 0.11

# Single bar spanning full range
ax1.barh(et_y, et_end - et_start, left=et_start, height=et_height,
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

# Main label
ax1.text(x_max/1.3, et_y - 0.005, r'$e^{-}$ Transport',
         fontsize=28, ha='right', va='center', color='black')

# Combined label with comma inside the box
ax1.text(et_start * 1.5, et_y - 0.005, r'$l_{mc}, l_{mr}$', fontsize=24, ha='left', va='center', color='black')

# Magnetic Domains bar: 15 nm to 1 mm
md_start = 15e-9   # 15 nm
md_end = 1e-3      # 1 mm
md_y = 0.35
md_height = 0.11

ax1.barh(md_y, md_end - md_start, left=md_start, height=md_height,
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

ax1.text(x_max/1.3, md_y - 0.005, 'Magnetic Domains',
         fontsize=28, ha='right', va='center', color='black')

# AFM/FM Magnons bar: 1 nm to 1 mm
magnon_start = 1e-9   # 1 nm
magnon_end = 1e-3     # 1 mm
magnon_y = 0.09
magnon_height = 0.11

ax1.barh(magnon_y, magnon_end - magnon_start, left=magnon_start, height=magnon_height,
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

ax1.text(x_max/1.3, magnon_y - 0.005, 'AFM/FM Magnons',
         fontsize=28, ha='right', va='center', color='black')

# ============== HORIZONTAL DIVIDER LINE ==============
# Draw black line between plots using figure coordinates (positioned between plots)
fig.add_artist(plt.Line2D([0.05, 0.95], [0.52, 0.52], color='black', linewidth=3, transform=fig.transFigure))

# ============== LOWER PLOT: Accessible Length Scales ==============
ax2.set_xscale('log')
ax2.set_xlim(x_min, x_max)
ax2.set_ylim(0, 0.7)

# Remove spines
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)
ax2.spines['bottom'].set_visible(True)
ax2.spines['bottom'].set_linewidth(3)
ax2.spines['bottom'].set_color('black')

# Remove y-axis
ax2.yaxis.set_visible(False)

# Disable automatic tick labels
ax2.tick_params(axis='x', which='both', labelbottom=False)

# Set major tick positions (no labels)
ax2.xaxis.set_major_locator(FixedLocator(tick_positions))
ax2.xaxis.set_major_formatter(NullFormatter())
ax2.tick_params(axis='x', which='major', length=25, width=3, pad=15, direction='out', top=False)

# Decade and minor ticks
for tick in decade_ticks:
    ax2.plot([tick, tick], [0, -0.02], color='black', linewidth=1.5, clip_on=False, transform=ax2.get_xaxis_transform())

for tick in minor_ticks:
    if x_min <= tick <= x_max:
        ax2.plot([tick, tick], [0, -0.035], color='black', linewidth=1.5, clip_on=False, transform=ax2.get_xaxis_transform())

ax2.xaxis.set_minor_locator(FixedLocator([]))
ax2.xaxis.set_minor_formatter(NullFormatter())

# Manually place text labels at tick positions (only on bottom plot)
ax2.text(1e-9, -0.11, '1 nm', fontsize=32, fontweight='bold', ha='center', va='top', transform=ax2.get_xaxis_transform())
ax2.text(1e-6, -0.11, '1 μm', fontsize=32, fontweight='bold', ha='center', va='top', transform=ax2.get_xaxis_transform())
ax2.text(1e-3, -0.11, '1 mm', fontsize=32, fontweight='bold', ha='center', va='top', transform=ax2.get_xaxis_transform())

# Grid lines
ax2.grid(True, which='major', axis='x', alpha=0.4, linestyle='-', linewidth=1.5, color='gray')
ax2.set_axisbelow(True)

# Title for lower plot - placed above the plot area
ax2.set_title('Measurable Length Scales', fontsize=36, fontweight='bold', pad=20)

# Single NV bar (6 nm to 1 mm, XYZ Resolved) - TOP bar
single_nv_start = 6e-9  # 6 nm
single_nv_end = 1e-3    # 1 mm
bar_y1 = 0.35
bar_height = 0.11

ax2.barh(bar_y1, single_nv_end - single_nv_start, left=single_nv_start, height=bar_height, 
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

ax2.text(
    x_max / 1.3,
    bar_y1 - 0.005,
    "Single NV",
    fontsize=28,
    ha="right",
    va="center",
    color="black",
)

# δ-Doped Ensemble bar - MIDDLE bar
delta_start = 6e-9      # 6 nm
delta_mid = 500e-9      # 500 nm
delta_end = 1e-3        # 1 mm
bar_y2 = 0.22

# Draw solid portion from 500 nm to 1 mm
ax2.barh(bar_y2, delta_end - delta_mid, left=delta_mid, height=bar_height, 
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

# Draw dashed/hatched portion from 6 nm to 500 nm
ax2.barh(bar_y2, delta_mid - delta_start, left=delta_start, height=bar_height, 
         color='white', edgecolor='black', linewidth=2, align='center', log=True, 
         hatch='///', alpha=0.5)

ax2.text(
    x_max / 1.3,
    bar_y2 - 0.005,
    r"$\delta$-Doped Ensemble",
    fontsize=28,
    ha="right",
    va="center",
    color="black",
)

# Single NV Scanning Probe bar - BOTTOM bar
nv_start = 40e-9  # 40 nm
nv_end = 1e-3     # 1 mm
bar_y3 = 0.09

ax2.barh(bar_y3, nv_end - nv_start, left=nv_start, height=bar_height, 
         color='lightgray', edgecolor='black', linewidth=2, align='center', log=True)

ax2.text(
    x_max / 1.3,
    bar_y3 - 0.005,
    "Single NV Scanning Probe",
    fontsize=28,
    ha="right",
    va="center",
    color="black",
)

# Legend (place in lower plot)
hatched_proxy = Patch(facecolor='white', edgecolor='black', hatch='///', label='Z Resolved, XY Averaged')
solid_proxy = Patch(facecolor='lightgray', edgecolor='black', label='XYZ Resolved')
ax2.legend(handles=[hatched_proxy, solid_proxy], loc='upper left', fontsize=18, frameon=False)

plt.tight_layout()

# Save high-resolution figure
plt.savefig(r'./img/spatial_scales.png', transparent=True, dpi=300, bbox_inches='tight')
print("Saved 'spatial_scales.png'")

plt.show()
