###
## simple_package - Module statistics.py
## Basic statistics calculations
###

## Here I need functions to take in data and do the
## following:
##
## 1) Calculate the mean, median, and standard deviation. 
##
## 2) Display the result with a clear and pretty print 
##    statement.
##
## 3) Plot a histogram of the data, with the mean and median 
##    marked on the plot. This should be part of a new Python
##    file in the package, called graphics.py.
##
## 4) Remember to provide a mechanism for checking that the input
##    is a numpy array or a list (if a list, you must convert it
##    to a numpy array).
##
## 5) Also, do something and/or throw an exception/message if the
##    numpy and matplotlib packages are not installed.
##

"""
statistics.py
----------------
Functions for calculating and displaying simple statistics.
Includes mean, median, std deviation, and histogram plotting.
"""

try:
    import numpy as np
except ImportError:
    raise ImportError("The numpy package is required for statistics calculations. Please install it.")

try:
    from . import PrettyPrint as pp
except ImportError:
    raise ImportError("PrettyPrint module not found. Ensure PrettyPrint.py is inside the package.")

def validate_input(data):
    """Validate that the input is a list or numpy array."""
    if not isinstance(data, (list, np.ndarray)):
        raise TypeError("Input data must be a list or numpy array.")
    return np.array(data)

def calculate_statistics(data):
    """Calculate mean, median, and standard deviation of the data."""
    data_array = validate_input(data)
    
    mean = np.mean(data_array)
    median = np.median(data_array)
    std_dev = np.std(data_array)
    
    return mean, median, std_dev

def print_statistics(data):
    """Calculate and pretty print the statistics of the data."""
    mean, median, std_dev = calculate_statistics(data)
    
    pp.pprint(f"Mean: {mean}")
    pp.pprint(f"Median: {median}")
    pp.pprint(f"Standard Deviation: {std_dev}")

def plot_statistics(data):
    """Plot histogram of the data with mean and median marked."""
    try: 
        from .graphics import plot_histogram  
    except ImportError:
        raise ImportError("The graphics module is required for plotting statistics. Please ensure it is available.")
    
    data_array = validate_input(data)
    mean, median, _ = calculate_statistics(data_array)
    plot_histogram(data_array, mean, median)