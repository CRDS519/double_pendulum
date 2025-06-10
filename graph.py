#!/usr/bin/env python3

import sys
import csv
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

from src.utils import pi_formatter
from src.pendulum import Pendulum

fps = 120

def read_simple(file):
    time = []
    x = []
    y = []
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        for i, row in enumerate(reader):
            time.append(float(i * 1/fps))
            x.append(float(row["X1"]))
            y.append(float(row["Y1"]))

    return (time, x, y)

def read_double(file):
    time = []
    x1 = []
    y1 = []
    x2 = []
    y2 = []
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=",")
        for i, row in enumerate(reader):
            time.append(float(i * 1/fps))
            x1.append(float(row["X1"]))
            y1.append(float(row["Y1"]))
            x2.append(float(row["X2"]))
            y2.append(float(row["Y2"]))

    return (time, x1, y1, x2, y2)

def cartesian_to_polar(x, y):
    return [np.arctan2(xi, yi) for xi, yi in zip(x, y)]

# ------------- PLOT MULTIPLE SIMPLE PENDULUMS -------------------
# simulation_time = 5 # in seconds
# steps = fps * simulation_time

# theta0 = np.pi/2

# for i in range(10):
#     thetai0 = theta0 + i * 0.01
#     pendulum = Pendulum(
#         pendulum_type="simple",
#         theta1=thetai0,
#         l1=0.5, m1=0.3
#     )

#     time = []
#     theta = []
#     dtheta = []
#     for j in range(steps):
#         time.append(j * 1/fps)
#         theta.append(pendulum.theta1)
#         dtheta.append(pendulum.dtheta1)
#         pendulum.update(1/fps)

#     plt.plot(time, theta, label="θ = " + str(round(thetai0, 3)))

# plt.xlabel("temps (en s)")
# plt.ylabel("θ (en rad)")
# plt.title("Influence des conditions initiales sur un pendule simple")
# ----------------------------------------------------------------

# ------------- PLOT SIMPLE PENDULUM PHASE DIAGRAM ---------------
# simulation_time = 5 # in seconds
# steps = fps * simulation_time

# theta0 = np.pi/2

# pendulum = Pendulum(
#     pendulum_type="simple",
#     theta1=theta0,
#     l1=0.5, m1=0.3
# )

# time = []
# theta = []
# dtheta = []
# for j in range(steps):
#     time.append(j * 1/fps)
#     theta.append(pendulum.theta1)
#     dtheta.append(pendulum.dtheta1)
#     pendulum.update(1/fps)

# plt.plot(theta, dtheta)

# plt.xlabel("θ (en rad)")
# plt.ylabel("dθ/dt (en rad/s)")
# plt.title("Diagramme de phase d'un pendule simple")
# ----------------------------------------------------------------

# ---------------- PLOT REAL DOUBLE PENDULUM ---------------------
# simulation_time = 15 # in seconds
# steps = fps * simulation_time
# time, x1, y1, x2, y2 = read_double(sys.argv[1])

# theta1 = cartesian_to_polar(x1, y1)
# theta2 = cartesian_to_polar(
#     [x2i - x1i for x1i, x2i in zip(x1, x2)],
#     [y2i - y1i for y1i, y2i in zip(y1, y2)]
# )

# plt.scatter(time[:steps], theta1[:steps], label="θ1")
# plt.scatter(time[:steps], theta2[:steps], label="θ2")

# plt.xlabel("temps (en s)")
# plt.ylabel("θ (en rad)")
# plt.title("Double pendule réel")
# ----------------------------------------------------------------

# ----------- PLOT REAL DOUBLE PENDULUM PHASE DIAGRAM ------------
# simulation_time = 3 # in seconds
# steps = fps * simulation_time
# time, x1, y1, x2, y2 = read_double(sys.argv[1])

# theta1 = cartesian_to_polar(x1, y1)
# theta2 = cartesian_to_polar(
#     [x2i - x1i for x1i, x2i in zip(x1, x2)],
#     [y2i - y1i for y1i, y2i in zip(y1, y2)]
# )

# dtheta1 = [0] + [(theta1[i+1] - theta1[i]) * fps for i in range(len(theta1) -1)]
# dtheta2 = [0] + [(theta2[i+1] - theta2[i]) * fps for i in range(len(theta2) -1)]

# # plt.plot(theta1[:steps], dtheta1[:steps])
# # plt.scatter(theta1[:steps], dtheta1[:steps], label="theta 1")
# plt.plot(theta2[:steps], dtheta2[:steps])
# plt.scatter(theta2[:steps], dtheta2[:steps], label="theta 2")

# # plt.xlabel("θ1 (en rad)")
# # plt.ylabel("dθ1/dt (en rad/s)")
# plt.xlabel("θ2 (en rad)")
# plt.ylabel("dθ2/dt (en rad/s)")
# plt.title("Diagramme de phase du pendule double réel")
# ----------------------------------------------------------------

# ------------- PLOT MULTIPLE DOUBLE PENDULUMS -------------------
# simulation_time = 15 # in seconds
# steps = fps * simulation_time

# theta1_0 = np.pi/2
# theta2_0 = 0

# for i in range(10):
#     theta1_i0 = theta1_0 + i * 0.01
#     pendulum = Pendulum(
#         pendulum_type="double",
#         theta1=theta1_i0, theta2=theta2_0,
#         l1=0.5, l2=0.5,
#         m1=0.3, m2=0.3
#     )

#     time = []
#     theta1 = []
#     dtheta1 = []
#     theta2 = []
#     dtheta2 = []
#     for j in range(steps):
#         time.append(j * 1/fps)
#         theta1.append(pendulum.theta1)
#         dtheta1.append(pendulum.dtheta1)
#         theta2.append(pendulum.theta2)
#         dtheta2.append(pendulum.dtheta2)
#         pendulum.update(1/fps)

#     # plt.plot(time, theta1, label="θ1 = " + str(round(theta1_i0, 3)))
#     plt.plot(time, theta2, label="θ1 = " + str(round(theta1_i0, 3)))

# plt.xlabel("temps (en s)")
# # plt.ylabel("θ1 (en rad)")
# plt.ylabel("θ2 (en rad)")
# plt.title("Influence des conditions initiales sur un pendule double")
# ----------------------------------------------------------------

# ------------- PLOT MULTIPLE FAKE DOUBLE PENDULUMS --------------
# simulation_time = 15 # in seconds
# steps = fps * simulation_time

# theta1_0 = np.pi/2
# theta2_0 = 0

# r = lambda a: random.gauss(0, a)

# for i in range(5):
#     theta1_i0 = theta1_0 + r(1) * 0.01
#     theta2_i0 = theta2_0 + r(1) * 0.01
#     pendulum = Pendulum(
#         pendulum_type="double", model="physic",
#         theta1=theta1_i0, theta2=theta2_i0,
#         l1=0.52, l2=0.51,
#         d1=0.275, d2=0.202,
#         m1=0.337, m2=0.269,
#         i1=0.03, i2=0.023,
#         f1=0.005, f2=0.005
#     )

#     time = []
#     theta1 = []
#     dtheta1 = []
#     theta2 = []
#     dtheta2 = []
#     for j in range(steps):
#         time.append(j * 1/fps)
#         theta1.append(pendulum.theta1)
#         dtheta1.append(pendulum.dtheta1)
#         theta2.append(pendulum.theta2)
#         dtheta2.append(pendulum.dtheta2)

#         pendulum.update(1/fps)

#         pendulum.theta1 += r(2) * 0.01
#         pendulum.dtheta1 += r(1) * 0.01
#         pendulum.theta2 += r(2) * 0.01
#         pendulum.dtheta2 += r(1) * 0.01

#     label = "θ1 = " + str(round(theta1_i0, 3)) + " et θ2 = " + str(round(theta2_i0, 3))
#     plt.scatter(time, theta1, label=label, s=10)
#     # plt.scatter(time, theta2, label=label, s=10)

# plt.xlabel("temps (en s)")
# plt.ylabel("θ1 (en rad)")
# # plt.ylabel("θ2 (en rad)")
# plt.title("Influence des conditions initiales sur le pendule double réel")
# ----------------------------------------------------------------

# --------------------- PLOT SIMPLE PENDULUM ---------------------
# simulation_time = 3 # in seconds
# steps = fps * simulation_time
# time, x, y = read_simple(sys.argv[1])

# theta = cartesian_to_polar(x, y)
# dtheta = [0] + [(theta[i+1] - theta[i]) * fps for i in range(len(theta) -1)]

# plt.scatter(time[:steps], theta[:steps])

# plt.xlabel("temps (en s)")
# plt.ylabel("θ (en rad)")
# plt.title("Pendule simple réel")
# ----------------------------------------------------------------

# -------------- PLOT DOUBLE PENDULUM PHASE DIAGRAM --------------
# simulation_time = 15 # in seconds
# steps = fps * simulation_time

# theta1_0 = np.pi/2
# theta2_0 = 0

# pendulum = Pendulum(
#     pendulum_type="double",
#     theta1=theta1_0, theta2=theta2_0,
#     l1=0.5, l2=0.5,
#     m1=0.3, m2=0.3
# )

# time = []
# theta1 = []
# dtheta1 = []
# theta2 = []
# dtheta2 = []
# for j in range(steps):
#     time.append(j * 1/fps)
#     theta1.append(pendulum.theta1)
#     dtheta1.append(pendulum.dtheta1)
#     theta2.append(pendulum.theta2)
#     dtheta2.append(pendulum.dtheta2)
#     pendulum.update(1/fps)

# plt.plot(theta1, dtheta1, label="θ1")
# plt.plot(theta2, dtheta2, label="θ2")

# plt.xlabel("θ (en rad)")
# plt.ylabel("dθ/dt (en rad/s)")
# plt.title("Diagramme de phase d'un pendule double")
# ----------------------------------------------------------------

# -------------- PLOT DOUBLE PENDULUM PHASE DIAGRAM --------------
# simulation_time = 15 # in seconds
# steps = fps * simulation_time

# theta1_0 = np.pi/2
# theta2_0 = 0

# pendulum = Pendulum(
#     pendulum_type="double",
#     theta1=theta1_0, theta2=theta2_0,
#     l1=0.5, l2=0.5,
#     m1=0.3, m2=0.3
# )

# time = []
# theta1 = []
# dtheta1 = []
# theta2 = []
# dtheta2 = []
# for j in range(steps):
#     time.append(j * 1/fps)
#     theta1.append(pendulum.theta1)
#     dtheta1.append(pendulum.dtheta1)
#     theta2.append(pendulum.theta2)
#     dtheta2.append(pendulum.dtheta2)
#     pendulum.update(1/fps)

# plt.plot(theta1, dtheta1, label="θ1")
# plt.plot(theta2, dtheta2, label="θ2")

# plt.xlabel("θ (en rad)")
# plt.ylabel("dθ/dt (en rad/s)")
# plt.title("Diagramme de phase d'un pendule double")
# ----------------------------------------------------------------

# ------------------ PLOT PHYSIC COMPARAISON ---------------------
# simulation_time = 15 # in seconds
# steps = fps * simulation_time

# time, x1, y1, x2, y2 = read_double(sys.argv[1])
# ttheta1 = cartesian_to_polar(x1, y1)
# ttheta2 = cartesian_to_polar(
#     [x2i - x1i for x1i, x2i in zip(x1, x2)],
#     [y2i - y1i for y1i, y2i in zip(y1, y2)]
# )

# theta1_0 = ttheta1[0]
# theta2_0 = ttheta2[0]

# pendulum = Pendulum(
#     pendulum_type="double", model="physic",
#     theta1=theta1_0, theta2=theta2_0,
#     l1=0.5, l2=0.5,
#     d1=0.275, d2=0.202,
#     m1=0.3, m2=0.3,
#     i1=0.0291, i2=0.0144
# )

# time = []
# theta1 = []
# dtheta1 = []
# theta2 = []
# dtheta2 = []
# for j in range(steps):
#     time.append(j * 1/fps)
#     theta1.append(pendulum.theta1)
#     dtheta1.append(pendulum.dtheta1)
#     theta2.append(pendulum.theta2)
#     dtheta2.append(pendulum.dtheta2)
#     pendulum.update(1/fps)

# plt.plot(time, theta1[:steps], label="simulation")
# plt.scatter(time, ttheta1[:steps], label="réel")

# plt.xlabel("temps (en s)")
# plt.ylabel("θ1 (en rad)")
# plt.title("Comparaison pendule double réel/simulé")
# ----------------------------------------------------------------

# ------------------ PLOT CLASSIC COMPARAISON --------------------
# simulation_time = 15 # in seconds
# steps = fps * simulation_time

# time, x1, y1, x2, y2 = read_double(sys.argv[1])
# ttheta1 = cartesian_to_polar(x1, y1)
# ttheta2 = cartesian_to_polar(
#     [x2i - x1i for x1i, x2i in zip(x1, x2)],
#     [y2i - y1i for y1i, y2i in zip(y1, y2)]
# )

# theta1_0 = ttheta1[0]
# theta2_0 = ttheta2[0]

# pendulum = Pendulum(
#     pendulum_type="double",
#     theta1=theta1_0, theta2=theta2_0,
#     l1=0.5, l2=0.5,
#     m1=0.3, m2=0.3
# )

# time = []
# theta1 = []
# dtheta1 = []
# theta2 = []
# dtheta2 = []
# for j in range(steps):
#     time.append(j * 1/fps)
#     theta1.append(pendulum.theta1)
#     dtheta1.append(pendulum.dtheta1)
#     theta2.append(pendulum.theta2)
#     dtheta2.append(pendulum.dtheta2)
#     pendulum.update(1/fps)

# plt.plot(time, theta1[:steps], label="simulation")
# plt.scatter(time, ttheta1[:steps], label="réel")

# plt.xlabel("temps (en s)")
# plt.ylabel("θ1 (en rad)")
# plt.title("Comparaison pendule double réel/simulé")
# ----------------------------------------------------------------

# ------------------ DEFAULT PYPLOT CONFIG -----------------------
# plt.gca().xaxis.set_major_locator(MultipleLocator(0.1))
# plt.gca().yaxis.set_major_locator(MultipleLocator(0.1))

plt.gca().xaxis.set_major_locator(MultipleLocator(1))

plt.gca().yaxis.set_major_locator(MultipleLocator(np.pi / 4))
plt.gca().yaxis.set_major_formatter(FuncFormatter(pi_formatter))
plt.ylim(-np.pi, np.pi)

# plt.gca().yaxis.set_major_locator(MultipleLocator(1))

# plt.gca().xaxis.set_major_locator(MultipleLocator(np.pi / 4))
# plt.gca().xaxis.set_major_formatter(FuncFormatter(pi_formatter))
# plt.xlim(-np.pi, np.pi)
# ----------------------------------------------------------------

# plt.legend()
plt.show()
