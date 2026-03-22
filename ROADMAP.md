# Roadmap: Modernising pyraingen and Removing Fortran

This document outlines the strategy for the continued evolution of `pyraingen`. The primary goal is to transition the package into a high-performance, pure-Python library by removing legacy Fortran dependencies while preserving scientific integrity.

---

## Phase 1: Fortran Logic Port (Pure-Python Engine)

The core daily simulation logic has been translated from `regionalised_dailyT4.for`.

- [done] **Baseline Generation**: Created reference logic for verification of the Python port.
- [done] **Subroutine Translation**:
    - Ported stochastic generators (`ran1`, `gasdev`) to NumPy/Numba.
    - Ported transition probability logic (`smoothprob`) and simulation loops to `src/pyraingen/daily_simulation.py`.
    - Ported k-NN/kernel regression engine (`psimmain`, `rf_amt_gen`) to Python.
- [done] **Numba Acceleration**: Utilised `@njit` to ensure Python performance matches or exceeds Fortran.
- [in progress] **Build System Cleanup**:
    - [ ] Remove `f2py` build requirements from `pyproject.toml`.
    - [ ] Deprecate and remove `src/pyraingen/fortran_daily/` directory.

---

## Phase 2: Enhanced Data Integration

Seamless integration with Australian climate datasets.

- [done] **SILO Point Data API**: Implemented direct fetching of daily rainfall by BOM station number or coordinates (`src/pyraingen/silo.py`).
- [done] **Decoupled Workflows**: Added support for user-supplied arrays in `regionalisedsubdailysim` (genSeqOption=5) with `suppliedSimYearStart` parameter for correct seasonal assignment.
- [ ] **AWAP/AGCD Support**: Add utility to extract daily rainfall time-series from Australian Water Availability Project (AWAP) or Australian Gridded Climate Data (AGCD) NetCDF/Zarr files.
- [ ] **BOM CDO Loader**: Add robust loader for BOM Climate Data Online (CDO) zip/csv files.
- [ ] **xarray Native Support**: Update internal functions to accept and return `xarray.DataArray` objects natively.

---

## Phase 3: Advanced Climate Analysis (HWRS 2025)

Implementation of state-of-the-art methodology from Millard et al. and Batchelor et al.

- [done] **IFD Uplift (ARR v4.2)**: Implemented temperature-based IFD projection formula.
- [done] **Seasonal Volume Adjustment**: Implemented the beta scaling factor to reconcile extremes with GCM volume projections.
- [done] **Recursive IFD Fitting**: Integrated the damped adjustment ratio for numerical stability during conditioning.
- [done] **Case Study Documentation**: Created the Darling Downs Worked Example (`docs/darling_downs_worked_example.ipynb`) featuring the Esk and Millmerran gauges.

---

## Phase 4: Architectural Cleanup (Pythonic Refactoring)

Removing remaining Matlab-isms and improving maintainability.

- [done] **Zero-Based Indexing Audit**: Audited all major modules for 1-based indexing remnants. Documented the 1-indexed `dayOfYear` convention in `getseasonfromday.py` with explicit season boundary dates. Added the `+1` conversion comment at every call site.
- [done] **Vectorisation Audit**: Replaced slow manual loops in `aggregaterainfall` and fragment sampling with NumPy broadcasting.
- [done] **targetstations.py idxTarget fix**: `np.where` return value is now correctly unwrapped to a plain integer, preventing the target station from appearing in its own logistic regression predictor and fixing wrong station IDs when a new site is appended.
- [done] **suppliedDailyRain year calculation**: Replaced hard-coded 2000 start year and `/366` estimate with explicit `suppliedSimYearStart` parameter and `round(total_days / 365.25) - 1` calculation.
- [done] **Fragment sanity check**: Removed stray `matplotlib` import from `getfragments.py`; sanity-check error message now includes the failing values to assist diagnosis.
- [done] **Unit conversion documentation**: Commented the `/10` scaling in `dailysequences.py` and `getfragments.py` to explain the tenths-of-mm convention used in the pluviograph NetCDF files.
- [done] **ifdcond.py frequency check**: Converted `warnings.warn()` to `ValueError` with a diagnostic message; execution no longer continues with an invalid AEP constraint.
- [done] **daily_simulation.py stubs**: Added `NotImplementedError` to `DailyRainfallSimulator.run_simulation` so users get a clear message rather than silent wrong output.
- [done] **Standardised Logging**: Replaced `print()` statements in `regionalisedsubdailysim.py`, `dailysequences.py`, and `getfragments.py` with `logging.getLogger(__name__)`. Note: `@njit`-decorated functions retain `print()` as Numba does not support the `logging` module.
- [done] **genSeqOption error handling**: Unsupported `genSeqOption` values now raise `ValueError` with a clear message instead of silently doing nothing.
- [in progress] **OO Refactoring**: Moving toward a unified `RainfallGenerator` class to manage state.
- [ ] **Type Hinting**: Apply PEP 484 type hints across the codebase.

---

## Phase 5: Continuous Quality and CI/CD

- [ ] **GitHub Actions Modernisation**: Automate testing across multiple Python versions (3.9 - 3.12).
- [ ] **Stochastic Testing**: Implement tests that verify the statistical properties of generated rainfall.
- [done] **README Enhancement**: Updated with clean usage examples, SILO instructions, and logging guidance.

---

## Status Legend

- [done] Complete: verified and merged.
- [in progress] Active development.
- [ ] Planned: not started.
