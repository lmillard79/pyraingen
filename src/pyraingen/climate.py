import numpy as np
import pandas as pd

def apply_arr_v4_2_uplift(historical_ifd, rate_alpha, delta_temp):
    """
    Applies ARR v4.2 climate change uplift to historical IFD depths.
    Equation: Ip = I * (1 + alpha/100)^delta_T
    
    Parameters
    ----------
    historical_ifd : np.ndarray
        Array of IFD rainfall depths (durations x AEPs).
    rate_alpha : float
        Rate of change parameter (usually ~5% per degree).
    delta_temp : float
        Change in global temperature projection (e.g., 3.0 for 2090 SSP3).
        
    Returns
    -------
    np.ndarray
        Projected future IFD depths.
    """
    future_ifd = historical_ifd * (1 + (rate_alpha / 100.0))**delta_temp
    return future_ifd

def calculate_submaximal_scaling_factor(total_observed_volume, total_maximal_volume, 
                                       total_non_maximal_volume, gcm_scaling_alpha):
    """
    Calculates the scaling factor (beta) for sub-maximal rainfall values.
    Equation from Batchelor et al. (2025): beta = (alpha*Vo - VM) / VNM
    
    Parameters
    ----------
    total_observed_volume : float
        Total rainfall volume in the original record (Vo).
    total_maximal_volume : float
        Total volume of rainfall that is part of an annual maximum (VM) in adjusted record.
    total_non_maximal_volume : float
        Total volume of remaining sub-maximal rainfall (VNM) in adjusted record.
    gcm_scaling_alpha : float
        The CMIP6 rainfall scaling factor (e.g., 0.93 for a 7% reduction).
        
    Returns
    -------
    float
        Scaling factor beta.
    """
    beta = (gcm_scaling_alpha * total_observed_volume - total_maximal_volume) / total_non_maximal_volume
    return beta

def identify_annual_maxima(rainfall_series, duration_steps):
    """
    Helper to identify indices of rainfall belonging to annual maxima 
    for a specific duration.
    """
    # This logic would typically interact with the internal indexing of pyraingen
    # used during ifdcond to ensure nested maxima are correctly handled.
    pass
