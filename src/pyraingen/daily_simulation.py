import numpy as np
from numba import njit
from .global_ import nSeasons, ndaysYearLeap

@njit
def day_count(year):
    """Returns number of days in Feb for a given year."""
    if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
        return 29
    return 28

@njit
def get_month_days(month, year):
    """Returns number of days in a month."""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        return day_count(year)
    return 0

@njit
def compute_conditional_probs(rainfall, rain_threshold):
    """
    Computes transition probabilities for wet/dry states.
    rainfall: (years, months, days)
    """
    n_years, n_months, n_days = rainfall.shape
    # result: [p_wet_given_dry, p_wet_given_wet, p_wet_overall]
    # monthly results for now to match Fortran smoothprob() logic
    probs = np.zeros((n_months, n_days, 3)) 
    
    # In practice, smoothprob uses a window (iband).
    # This is a simplified version of the logic in smoothprob()
    # We will need the full window logic for production.
    return probs

class DailyRainfallSimulator:
    def __init__(self, rain_threshold=0.30):
        self.rain_threshold = rain_threshold
        
    def run_simulation(self, n_sims, n_years, start_year, nearby_data):
        """
        Main entry point for daily simulation.
        nearby_data: list of dicts/arrays containing historical data for nearby stations.
        """
        # 1. Pre-process historical data (smoothprob, etc.)
        # 2. Run simulation loop (simulate)
        # 3. Return results
        pass
