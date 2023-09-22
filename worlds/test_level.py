import game
import pygame
from pygame.locals import *

level = game.World(2560, 2560, 1, -320, -740, False)

danger_1 = game.Danger(level, 1600, 960+740, 60, 40, (225, 20, 20), 0)

floor = game.WorldObject(level, 320, 1740, 1920, 80, (12, 12, 12), 0)
wall_1 = game.WorldObject(level, 320, 740, 5, 1080, (12, 12, 12), 0)
wall_2 = game.WorldObject(level, 2235, 740, 5, 1080, (12, 12, 12), 0)

platform_1 = game.WorldObject(level, 600, 1680, 40, 60, (30, 30, 30), 0)
platform_2 = game.WorldObject(level, 1000, 1680, 40, 60, (30, 30, 30), 0)

player1 = game.Player(level, 400, 780, 30, 60, (0, 0, 0),
                      pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_LSHIFT, 1.2, 2.5, 0.03)

player2 = game.Player(level, 400, 780, 30, 60, (255, 255, 0),
                      pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 1.1, 2.5, 0.03)

pad1 = game.JumpPad(level, 1360, 1740, 80, 20, (230, 230, 255),
                    4, True, 0)
pad2 = game.JumpPad(level, 1360, 1540, 80, 20, (230, 230, 255),
                    -4, True, 0)

scrolling_group_1 = game.ScrollingGroup(level, [platform_1, platform_2], 1000, 1480, 320, 2240, 740, 1820, -2)

