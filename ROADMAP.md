# Roadmap: Modernizing pyraingen & Fortran Removal

This document outlines the strategy for the continued evolution of `pyraingen`. The primary goal is to transition the package into a high-performance, pure-Python library by removing legacy Fortran dependencies while preserving scientific integrity.

## 🎯 Vision
Transform `pyraingen` from a collection of ported MATLAB/Fortran scripts into a modern, idiomatic Python package that is easy to install (no compilers required) and integrates seamlessly with the Australian climate data ecosystem (SILO, AWAP, BOM).

---

## 🏗️ Phase 1: Fortran Logic Port (The "Pure Python" Engine)
The core daily simulation logic currently resides in `regionalised_dailyT4.for`. This is the most significant barrier to entry for users.

- [ ] **Baseline Generation**: Create a comprehensive set of reference outputs from the existing Fortran code using fixed random seeds. This is our "Ground Truth."
- [ ] **Subroutine Translation**:
    - Port `RAN1` and other stochastic generators to `numpy.random` or `scipy.stats`.
    - Port the spatial correlation and weighting logic (Cholesky decomposition/matrix math) to NumPy.
    - Port the logistic regression application logic to Python.
- [ ] **Numba Acceleration**: Use `@njit` on the translated loops to ensure the Python implementation matches or exceeds Fortran's execution speed.
- [ ] **Build System Cleanup**: Remove `f2py` requirements from `pyproject.toml` and delete the `src/pyraingen/fortran_daily/` directory once parity is achieved.

## 📊 Phase 2: Enhanced Data Integration
Leverage the success of the SILO integration to support other critical Australian datasets.

- [ ] **AWAP/AGCD Support**: Add a utility to extract daily rainfall time-series from Australian Water Availability Project (AWAP) or Australian Gridded Climate Data (AGCD) NetCDF/Zarr files for any coordinate.
- [ ] **BOM CDO Scraper/Loader**: While SILO is preferred, adding a robust loader for BOM's "Climate Data Online" (CDO) zip/csv files would help users with local archives.
- [ ] **Xarray Native Support**: Update internal functions to accept and return `xarray.DataArray` objects, preserving metadata (units, coordinates, station names) throughout the disaggregation process.

## 🧹 Phase 3: Architectural Cleanup (Pythonic Refactoring)
Remove the remaining "MATLAB-isms" to make the codebase more maintainable.

- [ ] **OO-Refactoring**: Move from a script-heavy functional approach to a more object-oriented structure (e.g., a `RainfallGenerator` class) to manage state and parameters more cleanly.
- [ ] **Vectorization Audit**: Review all remaining modules for manual `for` loops (similar to the `aggregaterainfall` fix) and replace them with NumPy/Xarray operations.
- [ ] **Standardized Logging**: Replace `print` statements with the standard Python `logging` module for better control over output levels.
- [ ] **Type Hinting**: Apply PEP 484 type hints across the entire codebase to improve IDE support and developer experience.

## 🧪 Phase 4: Continuous Quality & CI/CD
- [ ] **GitHub Actions Modernization**: Automate testing across multiple Python versions (3.9 - 3.12).
- [ ] **Stochastic Testing**: Implement tests that verify the *statistical properties* of the generated rainfall (e.g., mean, variance, dry-spell lengths) rather than just exact array matches.
- [ ] **Documentation Site**: Expand the `ReadTheDocs` content with the new SILO/User-supplied workflows and a gallery of example applications (e.g., urban drainage design, crop modeling).

---

## 📈 Status Legend
- 🌑 **Planned**: Not started.
- 🌓 **In Progress**: Active development.
- 🌕 **Complete**: Verified and merged.
