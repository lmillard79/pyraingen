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

### Pure-Python workflow

Fetch observed daily data from SILO and disaggregate it to 6-minute intervals without requiring any Fortran components:

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

# Disaggregate to sub-daily using nearby pluviograph records
regionalisedsubdailysim(
    fnameInput=None,
    pathSubDaily="/path/to/pluviograph/netcdfs",
    targetIndex=40075,
    suppliedDailyRain=daily_rain,
    suppliedSimYearStart=1980,
    genSeqOption=5
)
```

`suppliedSimYearStart` must be set to the calendar year of the first day in your supplied data. Omitting it defaults to 2000 and will produce incorrect seasonal assignment for any other period.

### Enabling log output

`pyraingen` uses Python's standard `logging` module. To see progress messages:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

### Further documentation

See [pyraingen.readthedocs.io](https://pyraingen.readthedocs.io) for full API reference and worked examples including the Darling Downs case study.

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## Authors and Acknowledgements

`pyraingen` is an open-science initiative developed through the collaboration of:

- **WRM Water & Environment**: Primary development, Pythonic refactoring, and application in the Darling Downs Flood Study.
- **Bureau of Meteorology (BoM)**: Provision of foundational historical climate data and IFD design standards.
- **University of New South Wales (UNSW)**: Original research and stochastic methodology.

We acknowledge the decades of work by Australian hydrologists and software engineers, supported by various Australian Research Grants and industrial partnerships, whose contributions form the basis of this library. This package aims to contribute to open hydrological research and provide a robust, transparent tool for the Australian engineering community.

## Licence

`pyraingen` is released under the **Creative Commons Attribution 4.0 International (CC BY 4.0)** licence.

This package is the product of layered intellectual contributions spanning multiple decades, institutions, and funding bodies. The methodology rests on peer-reviewed research; the software implementation draws on Fortran and MATLAB origins that predate this repository; and the continued development has been supported by Australian government research investment and private practice. No single party holds exclusive ownership of this work. It is offered to the community as a collective contribution to Australian hydrological practice.

### You are free to

- **Share** — copy and redistribute this material in any medium or format.
- **Adapt** — remix, transform, and build upon this material for any purpose, including commercially.

The licensor cannot revoke these freedoms as long as you comply with the licence terms.

### Under the following terms

**Attribution** — You must give appropriate credit, provide a link to the licence, and indicate if changes were made. Attribution must acknowledge:

1. The foundational research methodology: Westra, S., Mehrotra, R., Sharma, A., & Srikanthan, R. (2012). Continuous rainfall simulation 1: A regionalised subdaily disaggregation approach. *Water Resources Research*, 48, W01535.
2. The IFD conditioning methodology: Woldemeskel, F., McInerney, D., Thyer, M., Kavetski, D., Shin, D., Shao, Q., Bates, B., & Sharma, A. (2018). Evaluating residual error approaches for post-processing monthly and seasonal streamflow forecasts. *Hydrology and Earth System Sciences*.
3. Climate change scaling (where used): Millard, J. et al. (2025) and Batchelor, C. et al. (2025), HWRS 2025.
4. This software repository and its contributors.

**No additional restrictions** — You may not apply legal terms or technological measures that legally restrict others from doing anything the licence permits.

Full licence text: [creativecommons.org/licenses/by/4.0](https://creativecommons.org/licenses/by/4.0/)

### A note on software licensing

CC BY 4.0 is a licence designed for creative and scientific works rather than software specifically. It is used here intentionally: the primary value of `pyraingen` lies in the hydrological methodology it encodes, and CC BY 4.0's attribution requirement ensures that methodology — and the researchers who developed it — are credited whenever this work is used or adapted. Users building derived software tools should also consider the practical expectations of the Australian hydrological research community when determining appropriate attribution.

## Credits

`pyraingen` was originally scaffolded with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
