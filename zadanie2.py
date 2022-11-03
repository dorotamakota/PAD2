"""
ZADANIE 2.
Wgraj dane z pliku Zadanie_2.csv.
Znajdź wektory własne, oraz wartości własne dla zawartej w pliku macierzy
Oblicz macierz odwrotną dla macierzy z pliku
"""

import numpy as np

data = np.genfromtxt('Zadanie_2.csv', delimiter=';', dtype="int")

print("wartości i wektory własne (eigenvalues and right eigenvectors of general arrays):")
print(np.linalg.eig(data))

print("macierz odwrócona:")
print(np.linalg.inv(data))
