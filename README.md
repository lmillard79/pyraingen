# pyraingen

A package for stochastically generating daily and subdaily rainfall in Australia with ifd constraining.

## Installation

```bash
$ pip install pyraingen
```

## Usage

`pyraingen` can be used to stochastically generate regionalised daily rainfall, disaggregate daily rainfall to subdaily fragments and constrain generated rainfall to observed or predicted Intensity Frequency Duration (IFD) relationships.
The three main functions are:

```python
from pyraingen.regionaliseddailysim import regionaliseddailysim
from pyraingen.regionalisedsubdailysim import regionalisedsubdailysim
from pyraingen.ifdcond import ifdcond
```

### ⚡ Bypassing Fortran with SILO or User Data

You can now bypass the internal Fortran daily rainfall generator by supplying your own daily rainfall data (e.g., from BOM gauges or AWAP) or by fetching it directly from the **SILO API**. This allows for a pure-Python workflow:

```python
from pyraingen.regionalisedsubdailysim import regionalisedsubdailysim
from pyraingen.silo import get_silo_point_data, prepare_silo_for_pyraingen

# 1. Fetch daily data from SILO
silo_df = get_silo_point_data(site="066062", start_date="20000101", end_date="20101231", email="your@email.com")
daily_rain = prepare_silo_for_pyraingen(silo_df, 2000, 2010)

# 2. Run disaggregation using the supplied data (genSeqOption=5)
regionalisedsubdailysim(
    fnameInput=None,
    pathSubDaily=path_to_pluviographs,
    targetIndex=66062,
    suppliedDailyRain=daily_rain,
    genSeqOption=5,
    nSims=1
)
```

Go to [`pyraingen.readthedocs.io`](https://pyraingen.readthedocs.io) for further documentation.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`pyraingen` was created by Caleb Dykman. Caleb Dykman retains all rights to the source and it may not be reproduced, distributed, or used to create derivative works.

## Credits

`pyraingen` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
