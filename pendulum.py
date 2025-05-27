import math
import pygame
import numpy as np
from physics.rungekutta import *
from physics.pendulum_fct import *

class Pendulum:
    def __init__(self, l1, l2, d1, d2, m1, m2, i1, i2, g, pendulum_type, model, scale):
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
        self.angle1 = math.pi
        self.angle2 = math.pi - 0.01 #if double pendulum
        self.angularSpeed1 = 0
        self.angularSpeed2 = 0 #if double pendulum
    
    def update(self, dt):
        self.move_pendulum(dt)
    
    def move_pendulum(self, dt):
        steps = 1
        h = dt / steps
        if self.pendulum_type == 'Simple':
            for _ in range(steps):
                self.angle1, self.angularSpeed1 = rk4_simple_pendulum(f_simple_pendulum, (self.angle1, self.angularSpeed1), h, self.g, self.l1)
        elif self.pendulum_type == 'Double':
            if self.model == 'Classic':
                self.angle1, self.angularSpeed1, self.angle2, self.angularSpeed2 = rk4_double_pendulum(f_double_pendulum, (self.angle1, self.angularSpeed1, self.angle2, self.angularSpeed2), h, self.g, self.l1, self.l2, self.m1, self.m2)
            elif self.model == 'Physic':
                self.angle1, self.angularSpeed1, self.angle2, self.angularSpeed2 = rk4_double_physic_pendulum(f_double_physic_pendulum, (self.angle1, self.angularSpeed1, self.angle2, self.angularSpeed2), h, self.g, self.l1, self.l2, self.d1, self.d2, self.m1, self.m2, self.i1, self.i2)

    def draw(self, screen):
        scale = self.pixel_per_m
        origin_x, origin_y = 800, 600

        if self.pendulum_type == 'Simple':
            x1 = origin_x + scale * self.l1 * math.sin(self.angle1)
            y1 = origin_y + scale * self.l1 * math.cos(self.angle1)

            pygame.draw.line(screen, "white", (origin_x, origin_y), (int(x1), int(y1)), 2)
            pygame.draw.circle(screen, "red", (int(x1), int(y1)), 10)
        elif self.pendulum_type == 'Double':
            x1 = origin_x + scale * self.l1 * math.sin(self.angle1)
            y1 = origin_y + scale * self.l1 * math.cos(self.angle1)
            x2 = origin_x + scale * (self.l1 * math.sin(self.angle1) + self.l2 * math.sin(self.angle2))
            y2 = origin_y + scale * (self.l1 * math.cos(self.angle1) + self.l2 * math.cos(self.angle2))

            pygame.draw.line(screen, "white", (origin_x, origin_y), (int(x1), int(y1)), 2)
            pygame.draw.line(screen, "white", (int(x1), int(y1)), (int(x2), int(y2)), 2)
            pygame.draw.circle(screen, "red", (int(x1), int(y1)), 10)
            pygame.draw.circle(screen, "red", (int(x2), int(y2)), 10)