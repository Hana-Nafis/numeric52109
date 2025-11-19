###
## Test file for the package simple_package
## Execute as 'python test_sp.py'
###

"""
test_sp.py
---------------
Test script for verifying functionality of the simple_package.
Tests basic and advanced mathematical operations, statistics functions, and data visualization.

This file can be run directly:
    python test_sp.py

It generates random test data, prints results, and displays a histogram for verification purposes.
"""

import simple_package as sp
import numpy as np

if __name__ == '__main__':

    ## Define two numbers
    a = 1;
    b = 2;
    
    # Test basic operations
    print(f"The sum of {a} and {b} is {sp.add(a,b)}")
    print(f"The product of {a} and {b} is {sp.multiply(a,b)}")

    # Test complex operations
    print(f"The sine of {a} is {sp.sine(a)}")
    print(f"The logarithm of {b} is {sp.logarithm(b)}")

    # Test statistics functions
    data = np.random.randint(0,101,100)
    sp.print_statistics(data)
    sp.plot_statistics(data)

    

    
    
