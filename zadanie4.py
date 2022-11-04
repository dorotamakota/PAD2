"""
EX 4.
"""
import numpy as np
import math

A = [0, 3, 2, 5]
B = [0, 3, 1, 4]

print(f"Add A and B: {np.add(A, B)}")

print(f"Subtract B from A: {np.subtract(B, A)}")

print(f"Multiply the vector A by the scalar a = 4: {np.multiply(A, 4)}")

print(f"Calculate the dot product of vectors A and B: {np.dot(A, B)}")

sum_sq = 0
for element in B:
    sum_sq += element**2
print(f"Find the length of vector B (math, py): {math.sqrt(sum_sq)}")

print(f"Find the length of vector B (numpy): {np.sqrt(np.sum(np.square(B)))}")
