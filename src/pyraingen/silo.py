import requests
import pandas as pd
import io
import numpy as np

def get_silo_point_data(site, start_date, end_date, email, apikey=None):
    """
    Fetches daily rainfall data from the SILO Point Data API.
    Ref: https://www.longpaddock.qld.gov.au/silo/api-documentation/reference/#PointData

    Parameters
    ----------
    site : str or tuple
        Station ID (str) or (latitude, longitude) tuple.
    start_date : str
        Start date in YYYYMMDD format.
    end_date : str
        End date in YYYYMMDD format.
    email : str
        Required email address for SILO API access.
    apikey : str, optional
        Optional API key if required for premium access.

    Returns
    ----------
    pd.DataFrame
        DataFrame with daily rainfall data.
    """
    url = "https://www.longpaddock.qld.gov.au/silo-api/v1/point-data"
    
    params = {
        "start": start_date,
        "finish": end_date,
        "format": "csv",
        "variable": "rain",
        "email": email
    }
    
    if isinstance(site, str):
        params["station"] = site
    elif isinstance(site, (list, tuple)) and len(site) == 2:
        params["lat"] = site[0]
        params["lon"] = site[1]
    else:
        raise ValueError("site must be a station ID (str) or (lat, lon) tuple")

    if apikey:
        params["apikey"] = apikey

    response = requests.get(url, params=params)
    response.raise_for_status()

    # SILO CSV has a preamble. We need to skip lines until the header.
    # Usually the header starts with 'YYYYMMDD' or similar.
    content = response.text
    # Find where the data starts
    lines = content.splitlines()
    header_idx = -1
    for i, line in enumerate(lines):
        if 'YYYY-MM-DD' in line or 'date' in line.lower():
            header_idx = i
            break
    
    if header_idx == -1:
        # Fallback to a guess if standard header not found
        df = pd.read_csv(io.StringIO(content), comment='#')
    else:
        df = pd.read_csv(io.StringIO("\n".join(lines[header_idx:])))

    # Ensure date column is datetime
    date_col = [c for c in df.columns if 'date' in c.lower() or 'YYYY-MM-DD' in c][0]
    df[date_col] = pd.to_datetime(df[date_col])
    df.set_index(date_col, inplace=True)
    
    # Rainfall column is usually 'rain' or similar
    rain_col = [c for c in df.columns if 'rain' in c.lower()][0]
    df = df[[rain_col]].rename(columns={rain_col: 'rainfall'})
    
    return df

def prepare_silo_for_pyraingen(df, sim_year_start, sim_year_end):
    """
    Formats SILO data for injection into pyraingen's sub-daily process.
    Handles padding/alignment if necessary.
    """
    # Filter to requested years
    df = df[(df.index.year >= sim_year_start) & (df.index.year <= sim_year_end)]
    
    # pyraingen expects a numpy array
    # We might need to ensure full years are present if the logic requires it
    # For now, return the values
    return df['rainfall'].values
