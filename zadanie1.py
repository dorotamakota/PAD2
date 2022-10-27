import numpy as np
import pandas as pd

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
print("Średni wzrost:")
print(np.average(heights))

print("odchylenie standardowe:")
print(np.std(heights))

print("najwyższy wzrost:")
print(np.max(heights))

print("najniższy wzrost:")
print(np.min(heights))

print("25 kwantyl:")
print(np.quantile(heights, 0.25))

print("75 kwantyl:")
print(np.quantile(heights, 0.75))

print("mediana:")
print(np.median(heights))
