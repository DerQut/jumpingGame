import game
import pygame
from pygame.locals import *

level = game.World(3200, 2560, 0.9, -640, -740, True, -0.5)

player1 = game.Player(level, (abs(level.camera_pos_x) + 0.5*1920 - 20), 780, 30, 60, (0, 0, 0), pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_LSHIFT, 1.2, 2.5, 0.03)

#player2 = game.Player(level, (abs(level.camera_pos_x) + 0.5*1920 + 20), 780, 30, 60, (255, 255, 0), pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 1.2, 2.5, 0.03)


x = level.camera_pos_x
size = 80
amount = 40

spawn_platform = []

while len(spawn_platform) < amount * 3:
    spawn_platform.append(game.WorldObject(level, x, 1620, size+10, 40, (30, 30, 30), 0))
    spawn_platform.append(game.JumpPad(level, x+5, 1600, size, 20, (200, 200, 255), 4, True, 0))
    spawn_platform.append(game.ScoreBubble(level, x+45, 1450, 25, 25, (50, 75, 255), 10))

    x = x + size + 5

spawn_scrolling = game.ScrollingGroup(level, spawn_platform, 3000, 3000, 1520, 320, 2560,
                                      0, 10000, level.scrolling_speed, 0, True)
spawn_scrolling.can_be_summoned = False


test_structure = [
    game.WorldObject(level, 0, 200, 450, 400, (40, 40, 40), 0),

    game.WorldObject(level, 0, 150, 90, 50, (40, 40, 40), 0),
    game.WorldObject(level, 180, 150, 90, 50, (40, 40, 40), 0),
    game.WorldObject(level, 360, 150, 90, 50, (40, 40, 40), 0),

    game.Danger(level, 5, 130, 80, 20, "spike", (240, 30, 30), 0),
    game.Danger(level, 185, 130, 80, 20, "spike", (240, 30, 30), 0),
    game.Danger(level, 365, 130, 80, 20, "spike", (240, 30, 30), 0),

    game.JumpPad(level, 95, 180, 80, 20, (200, 200, 255), 4, True, 0),
    game.JumpPad(level, 275, 180, 80, 20, (200, 200, 255), 4, True, 0),
    game.ScoreBubble(level, 110, 120, 25, 25, (50, 75, 255), 10),
    game.ScoreBubble(level, 110, 80, 25, 25, (50, 75, 255), 10),
    game.ScoreBubble(level, 110, 40, 25, 25, (50, 75, 255), 10),
]

test_scrolling = game.ScrollingGroup(level, test_structure, 3000, 3000, 1500, 320, 2560, 0, 1000, level.scrolling_speed)
test_scrolling.teleport(test_scrolling.hub_x, test_scrolling.hub_y)




test_structure_copy = [
    game.WorldObject(level, 0, 200, 450, 400, (40, 40, 40), 0),

    game.WorldObject(level, 0, 150, 90, 50, (40, 40, 40), 0),
    game.WorldObject(level, 180, 150, 90, 50, (40, 40, 40), 0),
    game.WorldObject(level, 360, 150, 90, 50, (40, 40, 40), 0),

    game.Danger(level, 5, 130, 80, 20, "spike", (240, 30, 30), 0),
    game.Danger(level, 185, 130, 80, 20, "spike", (240, 30, 30), 0),
    game.Danger(level, 365, 130, 80, 20, "spike", (240, 30, 30), 0),

    game.JumpPad(level, 95, 180, 80, 20, (200, 200, 255), 4, True, 0),
    game.JumpPad(level, 275, 180, 80, 20, (200, 200, 255), 4, True, 0),

    game.ScoreBubble(level, 110, 120, 25, 25, (50, 75, 255), 10),
    game.ScoreBubble(level, 110, 80, 25, 25, (50, 75, 255), 10),
    game.ScoreBubble(level, 110, 40, 25, 25, (50, 75, 255), 10),
]

test_scrolling_copy = game.ScrollingGroup(level, test_structure_copy, 3000, 3000, 1520, 320, 2560, 0, 1000, level.scrolling_speed)
test_scrolling_copy.teleport(test_scrolling_copy.hub_x, test_scrolling_copy.hub_y)


danger_left = game.Danger(level, 640, 740, 40, 1080, "gas", (225, 20, 20), 0)
danger_right = game.Danger(level, 2520, 740, 40, 1080, "gas", (225, 20, 20), 0)
danger_floor = game.Danger(level, 640, 1780, 1920, 40, "gas", (225, 20, 20), 0)
