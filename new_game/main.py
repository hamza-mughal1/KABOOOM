import os
from os import listdir
from os.path import isfile, join
import math
import random
import pygame
pygame.init()

pygame.display.set_caption("kaboom")

BG_COLOR = (255,255,255)
WIDTH, HEIGHT = 1000,800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH,HEIGHT))

def main(window, fps):
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(fps)



if __name__ == "__main__":
    main(window, FPS)
