import numpy as np
from . import log
import csv
import sys
def data_loader(input_file):
    with open(input_file,"r") as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
    raw_data = np.genfromtxt(input_file,delimiter=",",skip_header=1)
    if np.isnan(raw_data).any():
        rows, cols = np.where(np.isnan(raw_data))
        for r, c in zip(rows, cols):
            log.log_error(f"Non-numeric value in Row {r+1}, Column '{header[c]}'")
        sys.exit(1) 

    
    data = np.array(raw_data,dtype=float)
    mask = ~np.all(np.isnan(data),axis=0)
    data= data[:,mask]
    return header,data
