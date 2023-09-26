import pygame
from pygame.locals import *
import numpy

import game

import worlds.test_level
import worlds.lv_hedge_jump


if __name__ == '__main__':

    session = game.Game(1920, 1080, DOUBLEBUF | FULLSCREEN)

    while session.running:
        clock = pygame.time.Clock()
        clock.tick(150)
        session.run()
