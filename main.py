import pygame
import math
from pendulum import Pendulum

pygame.init()
width = 1600
height = 1200
screen = pygame.display.set_mode((1600, 1200))
scale = min(width, height) * 0.4
pygame.display.set_caption('Pendulum')
clock = pygame.time.Clock()
running = True
fps = 60
dt = 1/fps
pendulum = Pendulum(0.5, 0.5, 0.25, 0.25, 10, 10, 0, 0, 9.81,'Double','Classic', scale)

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