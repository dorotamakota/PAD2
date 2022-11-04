"""
EX 1.
"""

import numpy as np
import pandas as pd

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

print("Mean height: {}".format(np.average(heights)))

print("Standard deviation: {}".format(np.std(heights)))

print("Maximum height: {}".format(np.max(heights)))

print("Minimum height: {}".format(np.min(heights)))

print("25th percentile: {}".format(np.quantile(heights, 0.25)))

print("75th percentile: {}".format(np.quantile(heights, 0.75)))

print("Median: {}".format(np.median(heights)))

