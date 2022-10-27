import numpy as np

data = np.genfromtxt('Zadanie_2.csv', delimiter=';', dtype="int")

print("macierz oryginalna:")
print(data)
print("wartości i wektory własne (eigenvalues and right eigenvectors of general arrays):")
print(np.linalg.eig(data))
print("macierz odwrócona:")
print(np.linalg.inv(data))
