# ATC Project - AI Coding Agent Instructions

## Project Overview
ATC is a Python-based scientific visualization project focused on quantum sensing, NV (Nitrogen-Vacancy) center physics, and theoretical physics concepts. The codebase generates publication-quality figures and animations for research papers, emphasizing mathematical accuracy and visual clarity.

## Core Domain: Quantum Sensing & Physics Visualization

### Key Physics Concepts
- **NV Center Magnetometry**: Momentum-space kernels (`atc_plots.py`) with q³e^(-2qd) functional forms
- **Sombrero Potential**: Symmetry breaking animations showing phase transitions (mu² parameter from positive to negative)
- **Acquisition Systems**: SNR calculations for photon counting with shot noise analysis
- **Delta Functions**: Gaussian approximations for temporal-frequency filter functions with T₂* coherence times

### Mathematical Conventions
- Use LaTeX notation in plot labels: `r'$\frac{\omega}{\omega_0}$'`, `r'$P_0$'`, `r'$T_{2}^{*}$'`
- Log-log plots for power-law relationships (slope analysis via `np.polyfit(log_q, log_d, 1)`)
- Normalized units: frequencies as ω/ω₀, spatial coordinates in units of characteristic length scales

## Visualization Standards

### Matplotlib Configuration
- **Publication-ready exports**: 300 DPI, transparent backgrounds, tight bounding boxes
  ```python
  plt.savefig("filename.png", transparent=True, dpi=300, bbox_inches="tight")
  ```
- **Figure sizes**: (10, 7) for standard plots, (16, 8) for dual-axis plots, (8, 6) for 3D animations
- **Font sizes**: titles=28-40, axis labels=20-28, tick labels=18, legends=18-20
- **Tick formatting**: Hide tick labels for abstract/schematic plots using `ax.set_xticklabels([])` and `ax.yaxis.set_ticks([])`

### Color Schemes & Styling
- Primary colormaps: `viridis` (surface plots), `plasma` (contour plots)
- Contrast overlays: black contours with alpha=0.3, linewidth=0.5
- Grid styling: `alpha=0.3, linestyle='--'` for both major and minor grids
- Arrow annotations: `arrowstyle='<->'` with linewidth=2-2.5 for measurement indicators

### Animation Patterns
- Use `PillowWriter` for GIF exports (fps=10-30)
- Frame count typically 30-60 for smooth parameter sweeps
- Parameter interpolation: linear for mu_squared, smooth transitions via sigmoid masks for cutoffs
- Fixed z-limits across frames (`ax.set_zlim(-3, 4)`) to prevent visual jumps
- 3D view angles: `ax.view_init(elev=20-25, azim=-90 to 45)` depending on perspective needs

## Code Organization Patterns

### File Structure
Each script is **standalone** and **self-contained** - directly executable with `python scriptname.py`. No shared modules or imports between project files.

### Dataclass Usage for Parameters
Physical systems use `@dataclass` for parameter grouping:
```python
@dataclass
class AcquisitionParams:
    photon_count_rate: float  # Include units in comments
    readout_time: float       # seconds
    contrast: float           # 0-1 range
```

### Calculation Functions
Physics calculations separate from plotting:
```python
def calculate_time_to_snr(params: AcquisitionParams, evolution_time: float, target_snr: float) -> float:
    """Docstring with equations:
    SNR per readout = contrast * sqrt(photons_per_readout)
    """
    # Implementation with sqrt(2) corrections for difference measurements
```

## Development Workflow

### Testing Visualizations
1. Run scripts directly: `python scriptname.py`
2. Check output files in project root (PNG/GIF)
3. Verify absolute paths are not hardcoded (except temporary user-specific saves like `C:\Users\...`)

### Adding New Visualizations
- Keep physical parameters at module level or in `if __name__ == "__main__"` blocks
- Use `np.linspace()` for smooth parameter sweeps (typically 100-200 points)
- For multi-curve comparisons, iterate parameter sets and plot sequentially (see `conventional_readout.py` legend pattern)

### Common Numerical Patterns
- Mesh grids: `X, Y = np.meshgrid(x, y)` then `Z = f(X, Y)`
- Optimization: `scipy.optimize.fminbound` for finding maxima (negate function for maxima)
- Shot noise: `sqrt(photons)` with `1/sqrt(2)` factor for difference measurements

## Dependencies
Assumed installed (no requirements file):
- `numpy`, `scipy`
- `matplotlib` (with `mpl_toolkits.mplot3d`)
- `PIL` (Pillow) for GIF manipulation

## File-Specific Notes
- `spatial_scales.py`: Currently empty - placeholder for future spatial analysis
- `double_playback.py`: Utility for GIF speed manipulation (halves frame duration)
- `accessible_B.py`: 3D ellipsoid visualization for magnetic field accessibility (semi-axes ratio a:b:c = 1:1:2)

## When Creating New Physics Plots
1. Include detailed docstrings with equation definitions
2. Use meaningful variable names matching physics notation (q, d, mu, lambda_param)
3. Add comprehensive legends when comparing multiple parameter sets
4. Set appropriate axis scales (log/linear) based on expected power-law behavior
5. Save both display (`plt.show()`) and export (`plt.savefig()`) versions
