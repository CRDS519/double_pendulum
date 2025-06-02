import pygame
import math
from pendulum import Pendulum

pygame.init()
width = 1600
height = 1200
screen = pygame.display.set_mode((width, height))
scale = min(width, height) * 0.4
pygame.display.set_caption('Pendulum')
clock = pygame.time.Clock()
running = True
fps = 60
dt = 1/fps
pendulum = Pendulum(
    math.pi - 0.01, math.pi - 0.01, # debut angles
    0.52, 0.51, # lengths of the rods
    0.275, 0.202, # distance from the joint to the center of mass
    0.337, 0.269, # masses of the rods
    0.03, 0.023, # moment of inertia of the rods around the joint
    9.81,'Double','Physic', scale
)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("teal")

    pendulum.update(dt)
    pendulum.draw(screen)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()