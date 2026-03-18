import numpy as np
import logging
import log
def analysis(input_file,output_file,format):
    raw_data = np.genfromtxt(input_file,delimiter=",",names=True,encoding='utf-8')
    header = list(raw_data.dtype.names)
    data = raw_data.view((float,len(header)))
    try:
        if np.issubdtype(data.dtype,np.number):
            return data,header,format
    except ValueError as e:
        logging.error(f"File contains non-numeric data: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
            
    
data,col_names,format=analysis("data/sample_input.csv" , "sample_output.json" , "console")

if __name__ == "__main__":
    print(analysis("data/sample_input.csv" , "sample_output.json" , "json"))