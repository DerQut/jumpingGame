import game
import pygame
from pygame.locals import *

level = game.World(3200, 2560, 0.9, -640, -740, True, -2)

player1 = game.Player(level, (abs(level.camera_pos_x) + 0.5*1920 - 20), 780, 30, 60, (0, 0, 0), pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_LSHIFT, 4, 6, 0.25)

#player2 = game.Player(level, (abs(level.camera_pos_x) + 0.5*1920 + 20), 780, 30, 60, (255, 255, 0), pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 1.2, 2.5, 0.03)

danger_left = game.Danger(level, 640, 740, 40, 1080, "gas", (225, 20, 20), 0)
danger_right = game.Danger(level, 2520, 740, 40, 1080, "gas", (225, 20, 20), 0)
danger_floor = game.Danger(level, 640, 1780, 1920, 40, "gas", (225, 20, 20), 0)

x = level.camera_pos_x*-1

spawn_platform = [
    game.WorldObject(level, x, 1620, 600, 40, (30, 30, 30), 0),
    game.WorldObject(level, x+600, 1620, 600, 40, (30, 30, 30), 0),
    game.WorldObject(level, x+1200, 1620, 600, 40, (30, 30, 30), 0),
    game.WorldObject(level, x+1800, 1620, 540, 40, (30, 30, 30), 0),
]

while len(spawn_platform) < 30:
    spawn_platform.append(game.JumpPad(level, x+10, 1600, 80, 20, (200, 200, 255), 12, True, 0)),

    x = x + 90

spawn_scrolling = game.ScrollingGroup(level, spawn_platform, 3000, 3000, 1520, 640, 2560,
                                      0, 10000, level.scrolling_speed, 0, True)
spawn_scrolling.can_be_summoned = False


basic_bubble_platform_1 = [
    game.JumpPad(level, 5, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 95, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 185, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 275, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 365, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 455, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 545, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, -5, 20, 635, 40, (30, 30, 30), 0),

    game.ScoreBubble(level, 120, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -225, 30, 30, (50, 75, 255), 10),

    game.ScoreBubble(level, 300, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -225, 30, 30, (50, 75, 255), 10),

    game.ScoreBubble(level, 480, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -225, 30, 30, (50, 75, 255), 10),
]

basic_bubble_platform_sg_1 = game.ScrollingGroup(level, basic_bubble_platform_1, 3000, 3000, 1600-225, 640, 2560, 0, 1000, level.scrolling_speed)
basic_bubble_platform_sg_1.teleport(basic_bubble_platform_sg_1.hub_x, basic_bubble_platform_sg_1.hub_y)

basic_bubble_platform_2 = [
    game.JumpPad(level, 5, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 95, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 185, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 275, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 365, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 455, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 545, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, -5, 20, 635, 40, (30, 30, 30), 0),

    game.ScoreBubble(level, 120, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -225, 30, 30, (50, 75, 255), 10),

    game.ScoreBubble(level, 300, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -225, 30, 30, (50, 75, 255), 10),

    game.ScoreBubble(level, 480, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -225, 30, 30, (50, 75, 255), 10),
]

basic_bubble_platform_sg_2 = game.ScrollingGroup(level, basic_bubble_platform_2, 3000, 3000, 1600-225, 640, 2560, 0, 1000, level.scrolling_speed)
basic_bubble_platform_sg_2.teleport(basic_bubble_platform_sg_2.hub_x, basic_bubble_platform_sg_2.hub_y)

basic_bubble_platform_3 = [
    game.JumpPad(level, 5, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 95, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 185, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 275, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 365, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 455, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 545, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, -5, 20, 635, 40, (30, 30, 30), 0),

    game.ScoreBubble(level, 120, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 120, -225, 30, 30, (50, 75, 255), 10),

    game.ScoreBubble(level, 300, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 300, -225, 30, 30, (50, 75, 255), 10),

    game.ScoreBubble(level, 480, -45, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -90, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -135, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -180, 30, 30, (50, 75, 255), 10),
    game.ScoreBubble(level, 480, -225, 30, 30, (50, 75, 255), 10),
]

basic_bubble_platform_sg_3 = game.ScrollingGroup(level, basic_bubble_platform_3, 3000, 3000, 1600-225, 640, 2560, 0, 1000, level.scrolling_speed)
basic_bubble_platform_sg_3.teleport(basic_bubble_platform_sg_3.hub_x, basic_bubble_platform_sg_3.hub_y)



basic_jump_platform_1 = [
    game.JumpPad(level, 5, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 95, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, 180, -200, 200, 220, (30, 30, 30), 0),

    game.JumpPad(level, 385, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 475, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, 0, 20, 560, 40, (30, 30, 30), 0)
]

basic_jump_platform_sg_1 = game.ScrollingGroup(level, basic_jump_platform_1, 3000, 3000, 1600-200, 640, 2560, 0, 1000, level.scrolling_speed)
basic_jump_platform_sg_1.teleport(basic_jump_platform_sg_1.hub_x, basic_jump_platform_sg_1.hub_y)


basic_jump_platform_2 = [
    game.JumpPad(level, 5, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 95, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, 180, -200, 200, 220, (30, 30, 30), 0),

    game.JumpPad(level, 385, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 475, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, 0, 20, 560, 40, (30, 30, 30), 0)
]

basic_jump_platform_sg_2 = game.ScrollingGroup(level, basic_jump_platform_2, 3000, 3000, 1600-200, 640, 2560, 0, 1000, level.scrolling_speed)
basic_jump_platform_sg_2.teleport(basic_jump_platform_sg_2.hub_x, basic_jump_platform_sg_2.hub_y)


basic_jump_platform_3 = [
    game.JumpPad(level, 5, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 95, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, 180, -200, 200, 220, (30, 30, 30), 0),

    game.JumpPad(level, 385, 0, 80, 20, (200, 200, 255), 12, True, 0),
    game.JumpPad(level, 475, 0, 80, 20, (200, 200, 255), 12, True, 0),

    game.WorldObject(level, 0, 20, 560, 40, (30, 30, 30), 0)
]

basic_jump_platform_sg_3 = game.ScrollingGroup(level, basic_jump_platform_3, 3000, 3000, 1600-200, 640, 2560, 0, 1000, level.scrolling_speed)
basic_jump_platform_sg_3.teleport(basic_jump_platform_sg_3.hub_x, basic_jump_platform_sg_3.hub_y)
