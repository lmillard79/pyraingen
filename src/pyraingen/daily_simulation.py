import numpy as np
from numba import njit
import math

# --- Random Number Generation (Numerical Recipes ports) ---

@njit
def ran1(idum):
    """
    Minimal random number generator from Numerical Recipes.
    Note: In Python/Numba we might prefer np.random, but to match 
    the Fortran exactly we'd need to replicate the seed state.
    For Phase 1, we use a consistent generator.
    """
    # Simplified version for now; in a real port we'd use a 
    # more robust state-managed generator or np.random.seed()
    # For exactly matching Fortran, we'd need to replicate the 
    # specific bit-level behavior of the F77 RAN1.
    return np.random.random()

@njit
def gasdev():
    """Returns a normally distributed random deviate."""
    return np.random.standard_normal()

# --- Date Utilities ---

@njit
def day_count(year):
    """Returns number of days in Feb for a given year."""
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return 29
    return 28

@njit
def get_month_days(month, year):
    """Returns number of days in a month."""
    if month == 1: return 31
    if month == 2: return day_count(year)
    if month == 3: return 31
    if month == 4: return 30
    if month == 5: return 31
    if month == 6: return 30
    if month == 7: return 31
    if month == 8: return 31
    if month == 9: return 30
    if month == 10: return 31
    if month == 11: return 30
    if month == 12: return 31
    return 0

@njit
def get_season(month):
    """Maps month to season (1-4)."""
    if month in [12, 1, 2]: return 0 # Summer/Season 1
    if month in [3, 4, 5]:  return 1 # Autumn/Season 2
    if month in [6, 7, 8]:  return 2 # Winter/Season 3
    if month in [9, 10, 11]: return 3 # Spring/Season 4
    return 0


class DailyRainfallSimulator:
    """Pure-Python port of the Fortran daily rainfall simulator.

    Note: This class is not yet functional.  The subroutine translation
    (smoothprob, psimmain, rf_amt_gen) is in progress as part of the
    Fortran removal roadmap.  Calling run_simulation will raise
    NotImplementedError until the port is complete.

    In the meantime, use one of the following approaches:
      - genSeqOption=5 with suppliedDailyRain to supply your own daily data.
      - Fetch historical daily data from SILO via pyraingen.silo and pass it
        as suppliedDailyRain.
    """

    def __init__(self, rain_threshold=0.30):
        self.rain_threshold = rain_threshold

    def run_simulation(self, n_sims, n_years, start_year, nearby_data):
        """Main entry point for daily simulation.

        Parameters
        ----------
        n_sims : int
            Number of simulations to generate.
        n_years : int
            Length of each simulation in years.
        start_year : int
            Calendar year for the start of the simulation.
        nearby_data : list
            Historical data for nearby stations.
        """
        raise NotImplementedError(
            "The pure-Python daily rainfall simulator is not yet complete. "
            "Use genSeqOption=5 with the suppliedDailyRain parameter, or "
            "fetch historical daily data from SILO via pyraingen.silo."
        )
