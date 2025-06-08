#!/usr/bin/env python3

import sys
import csv
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

from src.utils import pi_formatter

def read_double(file):
    time = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        for row in reader:
            time.append(float(row["Time"]))
            x1.append(float(row["X1"]))
            y1.append(float(row["Y1"]))
            x2.append(float(row["X2"]))
            y2.append(float(row["Y2"]))

    return (time, x1, y1, x2, y2)

def cartesian_to_polar(x, y):
    return [np.arctan2(xi, yi) for xi, yi in zip(x, y)]

time, x1, y1, x2, y2 = read_double(sys.argv[1])

theta1 = cartesian_to_polar(x1, y1)
theta2 = cartesian_to_polar(
    [x2i - x1i for x1i, x2i in zip(x1, x2)],
    [y2i - y1i for y1i, y2i in zip(y1, y2)]
)

plt.scatter(time, theta1, label="theta 1")
plt.scatter(time, theta2, label="theta 2")

plt.legend()

plt.gca().xaxis.set_major_locator(MultipleLocator(1))

plt.gca().yaxis.set_major_locator(MultipleLocator(np.pi / 4))
plt.gca().yaxis.set_major_formatter(FuncFormatter(pi_formatter))
plt.ylim(-np.pi, np.pi)

plt.show()
