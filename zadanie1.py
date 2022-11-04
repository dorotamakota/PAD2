"""
ZADANIE 1.
Korzystając z poniższego kodu oraz pliku president_heights.csv utwórz tablicę zawierającą wzrost prezydentów USA.
Korzystając z pakietu NumPy podaj:
- średni wzrost
- odchylenie standardowe
- najwyższy oraz najniższy wzrost
- 25 i 75 kwantyl
- medianę.
"""

import numpy as np
import pandas as pd

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])

# Wartości zaokrąglono do liczb całkowitych
print("Średni wzrost: {}".format(int(np.average(heights))))

print("odchylenie standardowe: {}".format(int(np.std(heights))))

print("najwyższy wzrost: {}".format(int(np.max(heights))))

print("najniższy wzrost: {}".format(int(np.min(heights))))

print("25 kwantyl: {}".format(int(np.quantile(heights, 0.25))))

print("75 kwantyl: {}".format(int(np.quantile(heights, 0.75))))

print("mediana: {}".format(int(np.median(heights))))

