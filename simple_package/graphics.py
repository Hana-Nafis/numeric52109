"""
graphics.py
---------------
Module for plotting data visualizations for the simple_package.
Currently includes a function to plot histograms with mean and median lines clearly marked. 
Uses matplotlib for plotting.
"""

try:
    import matplotlib.pyplot as plt
except ImportError:
    raise ImportError("The matplotlib package is required for plotting. Please install it.")

def plot_histogram(data, mean, median):
    """Plot a histogram of the data with mean and median marked."""
    plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
    plt.axvline(mean, color='red', linestyle='dashed', label=f'Mean: {mean:.2f}')
    plt.axvline(median, color='green', linestyle='dashed', label=f'Median: {median:.2f}')
    plt.title('Histogram of Data')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.show()