# pyraingen

A package for stochastically generating daily and sub-daily rainfall in Australia with IFD constraining.

## The Full Stack

`pyraingen` provides a complete, pure-Python pipeline for continuous rainfall simulation and climate adjustment:

1. **Daily Generation**: A Numba-accelerated stochastic engine (ported from the original Fortran) for regionalised daily rainfall generation.
2. **Data Integration**: Direct fetching of high-fidelity, patched historical rainfall from the SILO API (supporting BOM station numbers).
3. **Sub-daily Disaggregation**: An implementation of the Regionalised Method of Fragments to convert daily totals into hourly or 6-minute sequences.
4. **IFD Reconciliation**: Recursive conditioning of synthetic rainfall to match official BoM 2016 Intensity-Frequency-Duration (IFD) statistics.
5. **Climate Change Scaling**: Support for ARR v4.2 temperature-based IFD uplift and CMIP6-based seasonal volume adjustments.

## Installation

```bash
pip install pyraingen
```

## Usage

### Minimum viable example

Fetch observed daily data from SILO and disaggregate it to 6-minute intervals:

```python
from pyraingen.silo import get_silo_point_data, prepare_silo_for_pyraingen
from pyraingen.regionalisedsubdailysim import regionalisedsubdailysim

# Fetch observed daily totals from SILO (e.g. Esk 040075, 1980-2023)
silo_df = get_silo_point_data(
    site="040075",
    start_date="19800101",
    end_date="20231231",
    email="your@email.com"
)
daily_rain = prepare_silo_for_pyraingen(silo_df, 1980, 2023)

# Disaggregate to sub-daily using nearby pluviograph records (genSeqOption=5)
regionalisedsubdailysim(
    fnameInput=None,
    pathSubDaily="/path/to/pluviograph/netcdfs",
    targetIndex=40075,
    suppliedDailyRain=daily_rain,
    suppliedSimYearStart=1980,
    genSeqOption=5
)
```

### Enabling log output

`pyraingen` uses Python's standard `logging` module. To see progress messages:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Further documentation

See [`pyraingen.readthedocs.io`](https://pyraingen.readthedocs.io) for full API reference and worked examples including the Darling Downs case study.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Authors and Acknowledgements

`pyraingen` is an open-science initiative developed through the collaboration of:

- **WRM Water & Environment**: Primary development, refactoring, and application in the Darling Downs Flood Study.
- **Bureau of Meteorology (BoM)**: Provision of foundational historical climate data and IFD design standards.
- **University of New South Wales (UNSW)**: Original research and stochastic methodology.

We acknowledge the decades of work by Australian hydrologists and software engineers, supported by various Australian Research Grants and industrial partnerships, whose contributions form the basis of this library. This package aims to contribute to open hydrological research and provide a robust, transparent tool for the Australian engineering community.

## License

This project is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** licence.

You are free to share and adapt this work, provided appropriate credit is given to the contributing institutions and the relevant research papers (e.g., Millard et al. 2025, Batchelor et al. 2025).

## Credits

`pyraingen` was originally scaffolded with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
