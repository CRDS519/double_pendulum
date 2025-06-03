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

pendulum_type = 'Double'
model = 'Physic'

def restart():
    new_pendulums = [Pendulum(
        0, math.pi - 0.00001*i, # debut angles
        0.52, 0.51, # lengths of the rods
        0.275, 0.202, # distance from the joint to the center of mass
        0.337, 0.269, # masses of the rods
        0.03, 0.023, # moment of inertia of the rods around the joint
        9.81, pendulum_type, model, scale, 0
    ) for i in range(1)]
    return new_pendulums

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
        pendulum.update(dt)
        pendulum.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()