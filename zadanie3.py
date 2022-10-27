import matplotlib as matplotlib
import numpy as np
import pandas as pd

# use pandas to extract rainfall inches as a NumPy array
rainfall = pd.read_csv("Seattle2014.csv")["PRCP"].values
inches = rainfall / 254.0  # 1/10mm -> inches
inches.shape()

print("nie padało:")

print("padało:")

print("spadło powyżej 0.5 cali deszczu:")

print("spadło poniżej 0.2 cali deszczu, ale padało:")

print("mediana opadów w deszczowe dni w 2014 roku:")

print("mediana opadów latem w 2014 roku (czyli dni pomiędzy dniem 172 a 262):")

print("maksymalne opady latem 2014 roku:")

print("maksymalne opady poza latem 2014 roku (czyli wiosna, jesień i zima):")
