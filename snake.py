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

    def __init__(self, x, y, xV, yV, color=(255, 0, 0)):
        self.x = x
        self.y = y
        self.xV = xV
        self.yV = yV
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (spacing * self.x,
                         spacing * self.y, spacing, spacing))

    def move(self):
        self.x += self.xV
        self.y += self.yV


class snake(object):
    body = []
    turns = {}

    def __init__(self):
        self.head = cube(4, 4, 1, 0)
        self.body.append(self.head)

    def move(self, keys):

        for key in keys:
            pos = (self.head.x, self.head.y)
            if keys[pygame.K_LEFT]:
                self.turns[pos] = [-1, 0]
            elif keys[pygame.K_RIGHT]:
                self.turns[pos] = [1, 0]
            elif keys[pygame.K_UP]:
                self.turns[pos] = [0, -1]
            elif keys[pygame.K_DOWN]:
                self.turns[pos] = [0, 1]

        for i, o in enumerate(self.body):
            p = (o.x, o.y)
            if p in self.turns:
                o.xV = self.turns[0]
                o.yV = self.turns[1]
                o.move()
                if i == len(self.body)-1:
                    self.turns.pop(p, None)
            

    def draw(self, surface):
        for i, c in enumerate(self.body):
            c.draw(surface)


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
