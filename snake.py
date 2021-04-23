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

    def __init__(self, pos, vel, color=(255, 0, 0)):
        self.pos = pos
        self.vel = vel
        self.color = color

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (spacing *
                         self.pos[0], spacing * self.pos[1], spacing, spacing))

    def move(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1])


class snake(object):
    body = []
    turns = {}

    def __init__(self):
        self.head = cube((4, 4), (1, 0))
        self.body.append(self.head)

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.turns[self.head.pos[:]] = [-1, 0]

        elif key[pygame.K_RIGHT]:
            self.turns[self.head.pos[:]] = [1, 0]

        elif key[pygame.K_UP]:
            self.turns[self.head.pos[:]] = [0, -1]

        elif key[pygame.K_DOWN]:
            self.turns[self.head.pos[:]] = [0, 1]

        for i, o, in enumerate(self.body):
            p = o.pos[:]

            if p in self.turns:
                o.vel = self.turns[p]
                o.move()
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                o.move()

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


    drawGrid(displaySurface, spacing)

    s.draw(displaySurface)

    while True:
        clock.tick(10)
        s.move()
        redrawWindow(displaySurface)


    pass


main()
