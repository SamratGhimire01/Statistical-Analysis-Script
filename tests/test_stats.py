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
    col_names = ["age", "salary"]
    
    # 2. Run your function
    result = stats.basic_operation(data, col_names, "console")
    
    # 3. Assertions (The "Checks")
    # Check Mean
    assert result["age"]["mean"] == 25.0
    assert result["salary"]["mean"] == 250.0
    
    # Check Median (Even rows case)
    assert result["age"]["median"] == 25.0
    
    # Check Correlation (Perfect linear relationship should be 1.0)
    # [0][1] is the correlation between age and salary
    assert result["correlation_matrix"][0][1] == 1.0

def test_median_odd_rows():
    # Test your custom medians function for odd rows
    data = np.array([[10], [20], [100]]) # Median should be 20
    res = stats.medians(data)
    
    assert res[0] == 20.0

def test_zero_variance_safety():
    # Test if correlation handles columns that don't change (std = 0)
    data = np.array([
        [10, 5],
        [20, 5],
        [30, 5]
    ])
    col_names = ["var", "const"]
    
    # This should not crash with ZeroDivisionError
    result = stats.basic_operation(data, col_names, "console")
    
    # The constant column correlation should be handled (usually 0.0 or NaN to 0.0)
    assert "correlation_matrix" in result
