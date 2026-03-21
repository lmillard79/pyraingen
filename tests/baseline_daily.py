from pyraingen.regionaliseddailysim import regionaliseddailysim
import os
import numpy as np

def generate_baseline():
    """Generates a baseline daily rainfall simulation using the current Fortran implementation."""
    # Use the example data parameters
    nyears = 10
    startyear = 1990
    nsim = 2
    targetidx = 66037 
    targetlat = -33.9410 
    targetlon = 151.1730 
    targetelev = 6.00 
    targetdcoast = 0.27 
    targetanrf = 1086.71
    targettemp = 22.40
    
    # We need to point to existing daily data. 
    # Based on the file structure, it's in src/pyraingen/data/example/daily/
    data_path = "src/pyraingen/data/example/daily/"
    
    output_nc = "tests/baseline_daily.nc"
    if os.path.exists(output_nc):
        os.remove(output_nc)
        
    print("Generating baseline with Fortran backend...")
    regionaliseddailysim(
        nyears, startyear, nsim,
        targetidx, targetlat, targetlon, 
        targetelev, targetdcoast, targetanrf,
        targettemp, data_path,
        output_path_nc=output_nc,
        getstations=True
    )
    print(f"Baseline generated: {output_nc}")

if __name__ == "__main__":
    generate_baseline()
