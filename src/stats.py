
import numpy as np

def basic_operation(data,col_names,format):
    means = np.mean(data,axis=0).round(2)
    median = np.median(data,axis=0).round(2)
    std = np.std(data,axis=0).round(2)


    cal1 = np.stack([means,median,std],axis=1).tolist()
    cal2 = np.array(['mean','median','std'])
    cal = [dict(zip(cal2, row)) for row in cal1]
    features_dict= dict(zip(col_names,cal))
    
    
    corr_matrix= np.corrcoef(data,rowvar=False).round(2).tolist()
    features_dict["correlation_matrix"]= corr_matrix
    
    
    return features_dict