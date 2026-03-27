import numpy as np
import pytest
from src import stats

def test_basic_operation_math():
    # 1. Setup Mock Data (4 rows, 2 columns)
    # Column 0: [10, 20, 30, 40] -> Mean: 25, Median: 25
    # Column 1: [100, 200, 300, 400] -> Mean: 250, Median: 250
    data = np.array([
        [10, 100],
        [20, 200],
        [30, 300],
        [40, 400]
    ])
    header = ["age", "salary"]
    
    # 2. Run your function (returns two NumPy arrays)
    basic_data, corre = stats.basic_operation(data, header)
    
    # 3. Assertions (Checking NumPy array indices)
    # basic_data[0] is Mean row, basic_data[1] is Median row
    assert basic_data[0, 0] == 25.0   # Mean of age
    assert basic_data[0, 1] == 250.0  # Mean of salary
    
    # Check Median (Even rows case: (20+30)/2 = 25)
    assert basic_data[1, 0] == 25.0
    
    # Check Correlation (Perfect linear relationship = 1.0)
    # corre[0, 1] is the correlation between age and salary
    assert corre[0, 1] == 1.0

def test_median_fun_logic():
    # Test odd rows: [10, 20, 100] -> Median is 20
    data_odd = np.array([[10], [100], [20]]) 
    res_odd = stats.median_fun(data_odd)
    assert res_odd[0] == 20.0

    # Test even rows: [10, 20, 30, 40] -> Median is (20+30)/2 = 25
    data_even = np.array([[10], [40], [20], [30]])
    res_even = stats.median_fun(data_even)
    assert res_even[0] == 25.0

def test_std_calculation():
    # Data: [10, 20, 30] -> Mean: 20
    # Variance: ((10-20)^2 + (20-20)^2 + (30-20)^2) / 3 = (100 + 0 + 100) / 3 = 66.67
    # STD: sqrt(66.67) = 8.16
    data = np.array([[10], [20], [30]])
    header = ["test"]
    basic_data, _ = stats.basic_operation(data, header)
    
    # basic_data[2] is the STD row
    assert basic_data[2, 0] == 8.16

def test_correlation_shape():
    # Ensure a 3-column input produces a 3x3 correlation matrix
    data = np.random.rand(10, 3)
    header = ["a", "b", "c"]
    _, corre = stats.basic_operation(data, header)
    
    assert corre.shape == (3, 3)
