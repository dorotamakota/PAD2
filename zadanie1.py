"""
ZADANIE 1.
Korzystając z poniższego kodu oraz pliku president_heights.csv utwórz tablicę zawierającą wzrost prezydentów USA.
Korzystając z pakietu NumPy podaj:
- średni wzrost
- odchylenie standardowe
- najwyższy oraz najniższy wzrost
- 25 i 75 kwantyl
- medianę.

Wartości zaokrąglono do liczb całkowitych.
"""

import numpy as np
import pandas as pd

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

print("Średni wzrost: " + str(int(np.average(heights))))

print("odchylenie standardowe: " + str(int(np.std(heights))))

print("najwyższy wzrost: " + str(int(np.max(heights))))

print("najniższy wzrost: " + str(int(np.min(heights))))

print("25 kwantyl: " + str(int(np.quantile(heights, 0.25))))

print("75 kwantyl: " + str(int(np.quantile(heights, 0.75))))

print("mediana: " + str(int(np.median(heights))))

