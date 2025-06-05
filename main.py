import pygame
import math
from pendulum import Pendulum

pygame.init()
width = 1600
height = 1200
origin = (width, height)
screen = pygame.display.set_mode(origin)
scale = min(width, height) * 0.4
pygame.display.set_caption('Pendulum')
clock = pygame.time.Clock()
running = True
fps = 60
dt = 1/fps

def restart():
    n = 1

    new_pendulums1 = [Pendulum(
        math.pi/2, math.pi - 0.00000001*i, # debut angles
        0.52, 0.51, # lengths of the rods
        0.275, 0.202, # distance from the joint to the center of mass
        0.337, 0.269, # masses of the rods
        0.03, 0.023, # moment of inertia of the rods around the joint
        9.81, 'Double', 'Physic', scale, 0.005, 0.005, 'red'
    ) for i in range(n)]

    new_pendulums2 = [Pendulum(
        math.pi/2, math.pi - 0.00000001*i, # debut angles
        0.52, 0.51, # lengths of the rods
        0.275, 0.202, # distance from the joint to the center of mass
        0.337, 0.269, # masses of the rods
        0.03, 0.023, # moment of inertia of the rods around the joint
        9.81, 'Double', 'Classic', scale, 0.005, 0.005, 'green'
    ) for i in range(n)]
    return new_pendulums1, new_pendulums2

pendulums1, pendulums2 = restart()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                pendulums1, pendulums2 = restart()
    
    screen.fill("black")

    for pendulum in pendulums2:
        pendulum.update(dt)
        pendulum.draw(screen)
    for pendulum in pendulums1:
        pendulum.update(dt)
        pendulum.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()