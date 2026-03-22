# Roadmap: Modernizing pyraingen & Fortran Removal

This document outlines the strategy for the continued evolution of `pyraingen`. The primary goal is to transition the package into a high-performance, pure-Python library by removing legacy Fortran dependencies while preserving scientific integrity.

---

## 🏗️ Phase 1: Fortran Logic Port (The "Pure Python" Engine)
The core daily simulation logic has been successfully translated from `regionalised_dailyT4.for`.

- [🌕] **Baseline Generation**: Created reference logic for verification of the Python port.
- [🌕] **Subroutine Translation**:
    - Ported stochastic generators (`ran1`, `gasdev`) to NumPy/Numba.
    - Ported transition probability logic (`smoothprob`) and simulation loops to `src/pyraingen/daily_simulation.py`.
    - Ported k-NN/kernel regression engine (`psimmain`, `rf_amt_gen`) to Python.
- [🌕] **Numba Acceleration**: Utilized `@njit` to ensure Python performance matches or exceeds Fortran.
- [🌓] **Build System Cleanup**:
    - [ ] Remove `f2py` build requirements from `pyproject.toml`.
    - [ ] Deprecate and remove `src/pyraingen/fortran_daily/` directory.

## 📊 Phase 2: Enhanced Data Integration
Seamless integration with Australian climate datasets.

- [🌕] **SILO Point Data API**: Implemented direct fetching of daily rainfall by BOM station number or coordinates (`src/pyraingen/silo.py`).
- [🌕] **Decoupled Workflows**: Added support for user-supplied arrays in `regionalisedsubdailysim` (genSeqOption=5).
- [🌑] **AWAP/AGCD Support**: Add utility to extract daily rainfall time-series from Australian Water Availability Project (AWAP) or Australian Gridded Climate Data (AGCD) NetCDF/Zarr files.
- [🌑] **BOM CDO Scraper/Loader**: Add robust loader for BOM "Climate Data Online" (CDO) zip/csv files.
- [🌑] **Xarray Native Support**: Update internal functions to accept and return `xarray.DataArray` objects natively.

## 🌡️ Phase 3: Advanced Climate Analysis (HWRS 2025)
Implementation of state-of-the-art methodology from Millard et al. and Batchelor et al.

- [🌕] **IFD Uplift (ARR v4.2)**: Implemented temperature-based IFD projection formula.
- [🌕] **Seasonal Volume Adjustment**: Implemented the $\beta$ scaling factor to reconcile extremes with GCM volume projections.
- [🌕] **Recursive IFD Fitting**: Integrated the damped adjustment ratio for numerical stability during conditioning.
- [🌕] **Case Study Documentation**: Created the **Darling Downs Worked Example** (`docs/darling_downs_worked_example.ipynb`) featuring the Esk and Millmerran gauges.

## 🧹 Phase 4: Architectural Cleanup (Pythonic Refactoring)
Removing remaining "MATLAB-isms" and improving maintainability.

- [🌕] **Zero-Based Indexing Shakedown**: Audited and fixed all major modules for 1-based indexing remnants.
- [🌕] **Vectorization Audit**: Replaced slow manual loops in `aggregaterainfall` and fragment sampling with NumPy broadcasting.
- [🌓] **OO-Refactoring**: Move toward a unified `RainfallGenerator` class to manage state.
- [🌑] **Standardized Logging**: Replace `print` statements with the Python `logging` module.
- [🌑] **Type Hinting**: Apply PEP 484 type hints across the entire codebase.

---

## 🧪 Phase 5: Continuous Quality & CI/CD
- [🌑] **GitHub Actions Modernization**: Automate testing across multiple Python versions (3.9 - 3.12).
- [🌑] **Stochastic Testing**: Implement tests that verify the *statistical properties* of generated rainfall.
- [🌕] **README Enhancement**: Updated with modern "pure-Python" usage examples and SILO instructions.

---

## 📈 Status Legend
- 🌑 **Planned**: Not started.
- 🌓 **In Progress**: Active development.
- 🌕 **Complete**: Verified and merged.
