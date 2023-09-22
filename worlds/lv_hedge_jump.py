import game
import pygame
from pygame.locals import *

level = game.World(2560, 2560, 0.9, -320, -740, True, -0.5)

player1 = game.Player(level, 400, 780, 30, 60, (0, 0, 0),
                      pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_LSHIFT, 1.2, 2.5, 0.03)

player2 = game.Player(level, 400, 780, 30, 60, (255, 255, 0),
                      pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 1.2, 2.5, 0.03)


x = level.camera_pos_x
size = 80
amount = 40

spawn_platform = []

while len(spawn_platform) < amount * 2:
    spawn_platform.append(game.WorldObject(level, x, 1620, size+10, 40, (30, 30, 30), 0))
    spawn_platform.append(game.JumpPad(level, x+5, 1600, size, 20, (200, 200, 255), 4, True, 0))
    x = x + size + 5

spawn_scrolling = game.ScrollingGroup(level, spawn_platform, 3000, 3000, 320, 10000,
                                      0, 10000, level.scrolling_speed)

test_structure = [
    game.WorldObject(level, 0, 200, 200, 50, (40, 40, 40), 0),

    game.WorldObject(level, 0, 150, 40, 50, (40, 40, 40), 0),
    game.WorldObject(level, 80, 150, 40, 50, (40, 40, 40), 0),
    game.WorldObject(level, 160, 150, 40, 50, (40, 40, 40), 0),

    game.Danger(level, 40, 190, 40, 10, "spike", (240, 30, 30), 0)
]

test_scrolling = game.ScrollingGroup(level, test_structure, 3000, 3000, 320, 10000,
                                     0, 1000, level.scrolling_speed)
test_scrolling.teleport(1520, 1520)
test_scrolling.x_velocity = level.scrolling_speed


danger_left = game.Danger(level, 320, 740, 40, 1080, "gas", (225, 20, 20), 0)
danger_right = game.Danger(level, 2200, 740, 40, 1080, "gas", (225, 20, 20), 0)
danger_floor = game.Danger(level, 320, 1780, 1920, 40, "gas", (225, 20, 20), 0)
