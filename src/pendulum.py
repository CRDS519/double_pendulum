import csv
import math
import pygame
import numpy as np

from src.utils import check, cartesian_to_polar
from src.physics.rungekutta import *
from src.physics.pendulum_fct import *

valid_types = {"simple", "double"}
valid_models = {"classic","physic", "tracked"}

class Pendulum:
    def __init__(
            self,
            pendulum_type = None,
            model = "classic",
            theta1 = None,
            theta2 = None,
            dtheta1 = 0,
            dtheta2 = 0,
            l1 = None, # in meter
            l2 = None,
            d1 = None, # distance from the pivot to the center of mass
            d2 = None,
            m1 = None, # in kg
            m2 = None,
            i1 = None, # inertia of the first rod
            i2 = None,
            f1 = 0, # friction factor
            f2 = 0,
            g = 9.81,
            scale = 480, # pixels per meter
            color = "red",
            file = None # path of the csv
    ):
        if pendulum_type not in valid_types:
            raise ValueError(f"valid pendulum types are {valid_types}, not '{pendulum_type}'")
        if model not in valid_models:
            raise ValueError(f"valid models are {valid_models}, not '{model}'")

        if model != "tracked":
            if pendulum_type == "simple":
                if check([theta1, l1, m1]):
                    raise ValueError("invalid arguments for a simple pendulum")
                self.theta1 = theta1
                self.l1 = l1
                self.m1 = m1

            if pendulum_type == "double":
                if check([theta1, theta2, l1, l2, m1, m2]):
                    raise ValueError("invalid arguments for a double pendulum")
                self.theta1 = theta1
                self.theta2 = theta2
                self.l1 = l1
                self.l2 = l2
                self.m1 = m1
                self.m2 = m2

                if model == "physic":
                    if check([d1, d2, i1, i2]):
                        raise ValueError("invalid arguments for a double pendulum")
                    self.d1 = d1
                    self.d2 = d2
                    self.i1 = i1
                    self.i2 = i2
        else:
            if not file:
                raise ValueError("missing a file for a tracked pendulum")

            x1 = []
            y1 = []
            x2 = []
            y2 = []
            with open(file, "r") as f:
                reader = csv.DictReader(f, delimiter=",")
                for row in reader:
                    x1.append(float(row["X1"]))
                    y1.append(float(row["Y1"]))
                    if pendulum_type == "double":
                        x2.append(float(row["X2"]))
                        y2.append(float(row["Y2"]))

            self.theta1_list = cartesian_to_polar(x1, y1)
            self.theta1 = self.theta1_list[0]

            if not l1:
                raise ValueError("missing l1 for the tracked pendulum")
            self.l1 = l1

            if pendulum_type == "double":
                if not l2:
                    raise ValueError("missing l1 for the tracked pendulum")
                self.theta2_list = cartesian_to_polar(
                    [x2i - x1i for x1i, x2i in zip(x1, x2)],
                    [y2i - y1i for y1i, y2i in zip(y1, y2)]
                )
                self.theta2 = self.theta2_list[0]
                self.l2 = l2

        self.index = 0 # current frame

        self.dtheta1 = dtheta1
        self.dtheta2 = dtheta2
        self.f1 = f1
        self.f2 = f2
        self.g = g

        self.origin_x = 800
        self.origin_y = 600

        self.pendulum_type = pendulum_type
        self.scale  = scale
        self.model = model
        self.color = color

    def update(self, dt):
        if self.model == "tracked":
            self.index = (self.index % (len(self.theta1_list) -1)) + 1

        if self.pendulum_type == "simple":
            if self.model == "tracked":
                self.theta1 = self.theta1_list[self.index]
                return

            if self.model == "classic":
                f = f_simple_pendulum
                rk4 = rk4_simple_pendulum
                args = (self.g, self.l1, self.m1, self.f1)
            else:
                f = f_simple_physic_pendulum
                rk4 = rk4_simple_physic_pendulum
                args = (self.g, self.l1, self.d1, self.m1, self.i1, self.f1)

            state = (self.theta1, self.dtheta1)
            new_state = rk4(f, state, dt, *args)
            self.theta1, self.dtheta1 = new_state
        elif self.pendulum_type == "double":
            if self.model == "tracked":
                self.theta1 = self.theta1_list[self.index]
                self.theta2 = self.theta2_list[self.index]
                return

            if self.model == "classic":
                f = f_double_pendulum
                rk4 = rk4_double_pendulum
                args = (self.g, self.l1, self.l2, self.m1, self.m2, self.f1, self.f2)
            elif self.model == "physic":
                f = f_double_physic_pendulum
                rk4 = rk4_double_physic_pendulum
                args = (self.g, self.l1, self.l2, self.d1, self.d2, self.m1, self.m2, self.i1, self.i2, self.f1, self.f2)

            state = (self.theta1, self.dtheta1, self.theta2, self.dtheta2)
            new_state = rk4(f, state, dt, *args)
            self.theta1, self.dtheta1, self.theta2, self.dtheta2 = new_state

    def to_screen(self, x_m, y_m):
        scale = self.scale
        return int(self.origin_x + scale*x_m), int(self.origin_y + scale*y_m)

    def draw(self, screen):
        self.origin_x = screen.get_width() /2
        self.origin_y = screen.get_height() /2

        if self.pendulum_type == "simple":
            x1, y1 = self.to_screen(self.l1*math.sin(self.theta1), self.l1*math.cos(self.theta1))

            pygame.draw.line(screen, "white", (self.origin_x, self.origin_y), (int(x1), int(y1)), 2)
            pygame.draw.circle(screen, self.color, (int(x1), int(y1)), 10)
        else: # self.pendulum_type == "double":
            x1, y1 = self.to_screen(self.l1*math.sin(self.theta1), self.l1*math.cos(self.theta1))
            x2, y2 = self.to_screen((self.l1 * math.sin(self.theta1) + self.l2 * math.sin(self.theta2)), (self.l1 * math.cos(self.theta1) + self.l2 * math.cos(self.theta2)))

            pygame.draw.line(screen, "white", (self.origin_x, self.origin_y), (int(x1), int(y1)), 2)
            pygame.draw.line(screen, "white", (int(x1), int(y1)), (int(x2), int(y2)), 2)
            pygame.draw.circle(screen, self.color, (int(x1), int(y1)), 10)
            pygame.draw.circle(screen, self.color, (int(x2), int(y2)), 10)
