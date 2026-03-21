import numpy as np
import logging
from . import log

def analysis(input_file, output_file, format_type):
    try:
        with open(input_file, 'r') as f:
            header = f.readline().strip().split(',')

        
        raw_data = np.genfromtxt(input_file, delimiter=',', skip_header=1)
        data = np.array(raw_data, dtype=float)

        # 3. Create a mask: Keep columns that are NOT all NaN
        mask = ~np.all(np.isnan(data), axis=0)
        
        # 4. Filter both data and header using the mask
        data = data[:, mask]
        header = [h for i, h in enumerate(header) if mask[i]]

        return data, header, format_type

    except Exception as e:
        log.log_error(f"Error: {e}")
        return None, None, None
