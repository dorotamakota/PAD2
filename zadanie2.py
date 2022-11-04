"""
EX 2.
"""

import numpy as np

data = np.genfromtxt('Zadanie_2.csv', delimiter=';', dtype="int")

print("eigenvalues and right eigenvectors of general arrays:")
print(np.linalg.eig(data))

print("inverted matrix:")
print(np.linalg.inv(data))
