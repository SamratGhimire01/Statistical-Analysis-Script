
import numpy as np
def medians(data):
    sorted_data = np.sort(data,axis=0)
    n=data.shape[0]
    if n%2==0:
        mid1=sorted_data[n//2-1]
        mid2 = sorted_data[n//2]
        return((mid1+mid2)/2).round(2).flatten()
    else:
        return sorted_data[n//2].round(2).flatten()
def basic_operation(data,col_names,format):
    means = ((np.sum(data,axis=0)) /data.shape[0]).round(2)
    median =medians(data)
    std = np.sqrt(np.mean((data - means)**2,axis=0)).round(2)


    cal1 = np.stack([means,median,std],axis=1).tolist()
    cal2 = np.array(['mean','median','std'])
    cal = [dict(zip(cal2, row)) for row in cal1]
    features_dict= dict(zip(col_names,cal))
    
     # Calculate denominator and handle zero-division (where std is 0)
    std_prod = np.outer(std, std)
    with np.errstate(divide='ignore', invalid='ignore'):
        corr = ((data - means).T @ (data - means) / data.shape[0]) / std_prod
        # Replace resulting NaNs (from 0/0) with 0.0
        corr = np.nan_to_num(corr)

    features_dict["correlation_matrix"] = corr.round(2).tolist()
    
    return features_dict