import numpy as np
def median_fun(data):
    sorted_data = np.sort(data,axis=0)
    n= data.shape[0]
    if n%2==0:
        return ((sorted_data[n//2-1] + sorted_data[n//2])/2).round(2).flatten()
    else:
        return sorted_data[n//2].round(2).flatten()
def basic_operation(data,header):
    mean = (np.sum(data , axis = 0) / data.shape[0]).round(2)
    median = median_fun(data)
    std = np.sqrt(np.mean((data-mean)**2,axis=0)).round(2)
    
    result = np.array([mean,median,std])
    
    
    corre = np.corrcoef(data,rowvar=False).round(2)
    return result,corre