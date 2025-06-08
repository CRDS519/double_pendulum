import math
import pygame
import numpy as np

from src.physics.rungekutta import *
from src.physics.pendulum_fct import *

class Pendulum:
    def __init__(self, angle1, angle2, l1, l2, d1, d2, m1, m2, i1, i2, g, pendulum_type, model, scale, friction1, friction2, color):
        valid_types = {'Simple', 'Double'}
        valid_models = {'Classic', 'Physic'}
        if pendulum_type not in valid_types:
            raise ValueError(f"pendulum_type doit être dans {valid_types}, pas '{pendulum_type}'")
        if model not in valid_models:
            raise ValueError(f"Pour un pendule double, model doit être dans {valid_models}, pas '{model}'")

        self.angle1 = angle1
        self.angle2 = angle2 #if double pendulum
        self.l1 = l1 #in m
        self.l2 = l2 #if double pendulum
        self.pixel_per_m  = scale
        self.d1 = d1 #if physic pendulum
        self.d2 = d2 #if double physic pendulum
        self.m1 = m1
        self.m2 = m2 #if double pendulum
        self.i1 = i1 #if physic pendulum
        self.i2 = i2 #if double physic pendulum
        self.g = g
        self.pendulum_type = pendulum_type # Simple/Double
        self.model = model # Classic/Physic
        self.angularSpeed1 = 0
        self.angularSpeed2 = 0 #if double pendulum

        self.origin_x = 800
        self.origin_y = 600

        self.friction1 = friction1
        self.friction2 = friction2

        self.color = color

    def update(self, dt):
        self.move_pendulum(dt)

    def move_pendulum(self, dt):
        if self.pendulum_type == 'Simple':
            if self.model == 'Classic':
                f = f_simple_pendulum
                rk4 = rk4_simple_pendulum
                args = (self.g, self.l1, self.m1, self.friction1)
            else:
                f = f_simple_physic_pendulum
                rk4 = rk4_simple_physic_pendulum
                args = (self.g, self.l1, self.d1, self.m1, self.i1, self.friction1)

            state = (self.angle1, self.angularSpeed1)
            new_state = rk4(f, state, dt, *args)
            self.angle1, self.angularSpeed1 = new_state
        elif self.pendulum_type == 'Double':
            if self.model == 'Classic':
                f = f_double_pendulum
                rk4 = rk4_double_pendulum
                args = (self.g, self.l1, self.l2, self.m1, self.m2, self.friction1, self.friction2)
            else:  # self.model == 'Physic'
                f = f_double_physic_pendulum
                rk4 = rk4_double_physic_pendulum
                args = (self.g, self.l1, self.l2, self.d1, self.d2, self.m1, self.m2, self.i1, self.i2, self.friction1, self.friction2)

            state = (self.angle1, self.angularSpeed1, self.angle2, self.angularSpeed2)
            new_state = rk4(f, state, dt, *args)
            self.angle1, self.angularSpeed1, self.angle2, self.angularSpeed2 = new_state

    def to_screen(self, x_m, y_m):
        scale = self.pixel_per_m
        return int(self.origin_x + scale*x_m), int(self.origin_y + scale*y_m)

    def draw(self, screen):
        self.origin_x = screen.get_width() /2
        self.origin_y = screen.get_height() /2

        if self.pendulum_type == 'Simple':
            x1, y1 = self.to_screen(self.l1*math.sin(self.angle1), self.l1*math.cos(self.angle1))

            pygame.draw.line(screen, "white", (self.origin_x, self.origin_y), (int(x1), int(y1)), 2)
            pygame.draw.circle(screen, self.color, (int(x1), int(y1)), 10)
        elif self.pendulum_type == 'Double':
            x1, y1 = self.to_screen(self.l1*math.sin(self.angle1), self.l1*math.cos(self.angle1))
            x2, y2 = self.to_screen((self.l1 * math.sin(self.angle1) + self.l2 * math.sin(self.angle2)), (self.l1 * math.cos(self.angle1) + self.l2 * math.cos(self.angle2)))

            pygame.draw.line(screen, "white", (self.origin_x, self.origin_y), (int(x1), int(y1)), 2)
            pygame.draw.line(screen, "white", (int(x1), int(y1)), (int(x2), int(y2)), 2)
            pygame.draw.circle(screen, self.color, (int(x1), int(y1)), 10)
            pygame.draw.circle(screen, self.color, (int(x2), int(y2)), 10)
