import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
import sys

# side length of the square grid
gridLength = 200
spacing = 20
# number of row or column lines
rowCol = gridLength // spacing
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
        self.head = cube(
            (rowCol//2, rowCol//2), (0, -1))
        self.body.append(self.head)

    def move(self, key):

        # Sets the turn location and direction in the turns hash.
        if key[pygame.K_LEFT] and self.head.vel[0] != -1 and self.head.vel[1] != 0:
            self.turns[self.head.pos[:]] = [-1, 0]

        elif key[pygame.K_RIGHT] and self.head.vel[0] != 1 and self.head.vel[1] != 0:
            self.turns[self.head.pos[:]] = [1, 0]

        elif key[pygame.K_UP] and self.head.vel[0] != 0 and self.head.vel[1] != -1:
            self.turns[self.head.pos[:]] = [0, -1]

        elif key[pygame.K_DOWN] and self.head.vel[0] != 0 and self.head.vel[1] != 1:
            self.turns[self.head.pos[:]] = [0, 1]

        # performes the snake movement
        for i, o, in enumerate(self.body):
            p = o.pos[:]
            if p in self.turns:
                o.vel = self.turns[p]
                o.move()
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if o.pos[0] <= 0 and o.vel[0] == - 1:
                    o.pos = (rowCol - 1, o.pos[1])
                elif o.pos[0] >= rowCol-1 and o.vel[0] == 1:
                    o.pos = (0, o.pos[1])
                elif o.pos[1] <= 0 and o.vel[1] == -1:
                    o.pos = (o.pos[0], rowCol - 1)
                elif o.pos[1] >= rowCol-1 and o.vel[1] == 1:
                    o.pos = (o.pos[0], 0)
                else:
                    o.move()

    def addCube(self):
        tmp = self.body[-1]
        x = tmp.pos[0]
        y = tmp.pos[1]
        xV = tmp.vel[0]
        yV = tmp.vel[1]

        tail = cube((x - xV, y-yV), (xV, yV), (255, 0, 255))

        self.body.append(tail)

    def draw(self, surface):
        for i, o in enumerate(self.body):
            o.draw(surface)


def drawGrid(surface, spacing):
    for lines in range(rowCol):
        pygame.draw.line(surface, (255, 255, 255),
                         (0, (lines + 1) * spacing), (gridLength, (lines + 1) * spacing))
        pygame.draw.line(surface, (255, 255, 255),
                         ((lines + 1) * spacing, 0), ((lines + 1) * spacing, gridLength))


def redrawWindow(surface):
    surface.fill((0, 0, 0))
    snack.draw(surface)
    snake.draw(surface)
    drawGrid(displaySurface, spacing)
    pygame.display.update()


def randSnackLoc(snake):
    while True:
        x = random.randrange(rowCol)
        y = random.randrange(rowCol)
        if len(list(filter(lambda z: z.pos == (x, y), snake.body))) > 0:
            continue
        else:
            break

    return (x, y)


def noCollision(snake):
    posList = []

    for x in range(len(snake.body)):
        posList.append(snake.body[x].pos)

    return len(posList) == len(set(posList))


def main():
    global snake, snack

    pygame.init()
    clock = pygame.time.Clock()
    pygame.display.set_caption('SsSsSsSsnake')
    drawGrid(displaySurface, spacing)

    snake = snake()
    snack = cube(randSnackLoc(snake), (0, 0), (0, 255, 0))

    snack.draw(displaySurface)
    snake.draw(displaySurface)

    while True:
        pygame.time.delay(50)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if noCollision(snake):
            snake.move(pygame.key.get_pressed())
            if snake.body[0].pos == snack.pos:
                snake.addCube()
                snack = cube(randSnackLoc(snake), (0, 0), (0, 255, 0))
        redrawWindow(displaySurface)


main()
