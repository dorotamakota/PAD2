"""
ZADANIE 4.
Wykonaj następujące operacje:
- Dodaj A i B
- Odejmij B od A
- Pomnóż wektor A przez skalar a=4
- Oblicz iloczyn skalarny wektorów A i B
- Znajdź długość wektora B
Te operacje można wykonać „ręcznie” w Pythonie, ale postaraj się znaleźć odpowiednie funkcje NumPy.
"""
import numpy as np
import math

A = [0, 3, 2, 5]
B = [0, 3, 1, 4]

print("Dodaj A i B:")
print(np.add(A, B))

print("Obejmij B od A:")
print(np.subtract(B, A))

print("Pomnóż wektor A przez skalar a=4:")
print(np.multiply(A, 4))

print("Oblicz iloczyn skalarny wektorów A i B:")
print(np.dot(A, B))

print("Znajdź długość wektora B:")
print("matematycznie, pythonowo:")
suma_kwadratow = 0
for element in B:
    suma_kwadratow += element**2
# pierwiastek sumy kwadratów:
print(math.sqrt(suma_kwadratow))
print("numpy'owo:")
print(np.sqrt(np.sum(np.square(B))))
