#!/usr/bin/env python3

import sys
import math
import pygame

from src.pendulum import Pendulum

fps = 120
width = 1600
height = 1200

origin = (width, height)
scale = min(width, height) * 0.4
dt = 1/fps

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Pendulum")
screen = pygame.display.set_mode(origin)

running = True

def restart():
    n = 1

    # new_pendulums = [Pendulum(
    #     pendulum_type="double", model="physic",
    #     theta1=math.pi/2, theta2=math.pi - 0.00000001*i,
    #     l1=0.52, l2=0.51,
    #     d1=0.275, d2=0.202,
    #     m1=0.337, m2=0.269,
    #     i1=0.03, i2=0.023,
    #     f1=0.005, f2=0.005,
    #     color="red"
    # ) for i in range(n)] + [Pendulum(
    #     pendulum_type="double", model="classic",
    #     theta1=math.pi/2, theta2=math.pi - 0.00000001*i,
    #     l1=0.52, l2=0.51,
    #     m1=0.337, m2=0.269,
    #     f1=0.005, f2=0.005,
    #     color="green"
    # ) for i in range(n)]

    # return new_pendulums

    tracked = Pendulum(
        pendulum_type="double", model="tracked",
        l1=0.52, l2=0.51,
        file=sys.argv[1], color="yellow",
    )

    theta1 = tracked.theta1
    theta2 = tracked.theta2

    simulated = Pendulum(
        pendulum_type="double", model="physic",
        theta1=theta1, theta2=theta2,
        l1=0.52, l2=0.51,
        d1=0.275, d2=0.202,
        m1=0.33685, m2=0.26945,
        i1=0.003, i2=0.003,
        # f1=0.005, f2=0.005,
        color="red"
    )

    return [tracked, simulated]

pendulums = restart()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pendulums = restart()

    screen.fill("black")

    for pendulum in pendulums:
        pendulum.draw(screen)
        pendulum.update(dt)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
