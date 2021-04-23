import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

# side length of the square grid
gridLength = 500
spacing = 20
displaySurface = pygame.display.set_mode((gridLength, gridLength))


class cube(object):

    def __init__(self, pos=(80, 80), vel=(20, 0), color=(255, 0, 0)):
        self.pos = pos
        self.vel = vel
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.pos[0] + 2,
                         self.pos[1] + 2, spacing - 2, spacing - 2))

    def move(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])


class snake(object):
    body = []
    turns = {}

    def __init__(self):
        self.head = cube()
        self.body.append(self.head)

    def move(self, keys):

        for key in keys:
            if keys[pygame.K_LEFT]:
                self.turns[self.head.pos[:]] = [-20, 0]

            elif keys[pygame.K_RIGHT]:
                self.turns[self.head.pos[:]] = [20, 0]

            elif keys[pygame.K_UP]:
                self.turns[self.head.pos[:]] = [0, -20]

            elif keys[pygame.K_DOWN]:
                self.turns[self.head.pos[:]] = [0, 20]

        for i, o, in enumerate(self.body):
            p = o.pos[:]

            if p in self.turns:
                o.vel = self.turns[p]
                o.move()
                if i == len(self.body)-1:
                    self.turns.pop(p)
                

    def draw(self, surface):
        for i, o in enumerate(self.body):
            o.draw(surface)


def drawGrid(surface, spacing):

    lineGuides = gridLength // spacing

    dist = 0

    for lines in range(lineGuides):
        dist += spacing
        pygame.draw.line(surface, (255, 255, 255),
                         (0, dist), (gridLength, dist))
        pygame.draw.line(surface, (255, 255, 255),
                         (dist, 0), (dist, gridLength))


def redrawWindow(surface):
    surface.fill((0, 0, 0))
    s.draw(surface)
    drawGrid(displaySurface, spacing)
    pygame.display.update()


def main():
    global s
    s = snake()
    clock = pygame.time.Clock()

    pygame.init()
 
    pygame.display.set_caption('SsSsSsSsnake')

    running = True

    drawGrid(displaySurface, spacing)

    s.draw(displaySurface)

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            clock.tick(10)
            keys = pygame.key.get_pressed()
            s.move(keys)
            redrawWindow(displaySurface)


    pygame.quit()

    pass


main()
