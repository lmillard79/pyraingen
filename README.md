# pyraingen

A package for stochastically generating daily and subdaily rainfall in Australia with IFD constraining.

## 🚀 The Full Stack

`pyraingen` provides a complete, pure-Python pipeline for continuous rainfall simulation and climate adjustment:

1.  **Daily Generation**: A Numba-accelerated stochastic engine (ported from the original Fortran) for regionalised daily rainfall generation.
2.  **Data Integration**: Direct fetching of high-fidelity, patched historical rainfall from the **SILO API** (supporting BOM station numbers).
3.  **Sub-daily Disaggregation**: An implementation of the **Regionalised Method of Fragments** to convert daily totals into hourly or 6-minute sequences.
4.  **IFD Reconcilation**: Recursive conditioning of synthetic rainfall to match official BoM 2016 Intensity-Frequency-Duration (IFD) statistics.
5.  **Climate Change Scaling**: Support for ARR v4.2 temperature-based IFD uplift and CMIP6-based seasonal volume adjustments.

## Installation

```bash
$ pip install pyraingen
```

## Usage

### ⚡ Pure-Python Workflow (Bypassing Fortran)

You can now bypass the legacy Fortran components by supplying your own daily rainfall data or by fetching it directly from the **SILO API**:

```python
from pyraingen.regionalisedsubdailysim import regionalisedsubdailysim
from pyraingen.silo import get_silo_point_data, prepare_silo_for_pyraingen

# 1. Fetch daily data for a BOM station (e.g., Esk 040075)
silo_df = get_silo_point_data(site="040075", start_date="19800101", end_date="20231231", email="your@email.com")
daily_rain = prepare_silo_for_pyraingen(silo_df, 1980, 2023)

# 2. Run disaggregation using the supplied data (genSeqOption=5)
regionalisedsubdailysim(
    fnameInput=None,
    pathSubDaily=path_to_pluviographs,
    targetIndex=40075,
    suppliedDailyRain=daily_rain,
    genSeqOption=5
)
```

Go to [`pyraingen.readthedocs.io`](https://pyraingen.readthedocs.io) for further documentation and worked examples.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Authors and Acknowledgements

`pyraingen` is an open-science initiative developed through the collaboration of:

*   **Bureau of Meteorology (BoM)**: Provision of foundational historical climate data and IFD design standards.
*   **University of New South Wales (UNSW)**: Original research and stochastic methodology.

We acknowledge the decades of work by Australian hydrologists and software engineers, supported by various **Australian Research Grants** and industrial partnerships, whose contributions form the basis of this library. This package aims to contribute to open hydrological research and provide a robust, transparent tool for the Australian engineering community.

## License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** License. 

You are free to share and adapt this work, provided appropriate credit is given to the contributing institutions and the relevant research papers (e.g., Millard et al. 2025, Batchelor et al. 2025).

## Credits

`pyraingen` was originally scaffolded with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
