import game
import pygame
from pygame.locals import *


def basic_jump_struct():
    jump = [
        game.WorldObject(level, 2 * (PAD_SIZE_X + 10), -225, 315, 650, FLOOR_COLOUR, 0),

        game.WorldObject(level, -5, PAD_SIZE_Y, 4 * (PAD_SIZE_X + 10) + 327, 40, FLOOR_COLOUR, 0),

        game.JumpPad(level, 0, 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, PAD_SIZE_X + 10, 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 325 + 2 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 325 + 3 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),

        game.ScoreBubble(level, 0.5 * (PAD_SIZE_X + 10) - BUBBLE_SIZE * 0.5, -150, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 1.25 * (PAD_SIZE_X + 10) - BUBBLE_SIZE * 0.5, -250, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 2 * (PAD_SIZE_X + 10), -350, BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 2 * (PAD_SIZE_X + 10) + 0.5 * 315 - 0.5 * BUBBLE_SIZE, -400, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 2 * (PAD_SIZE_X + 10) + 295 - 0.5 * BUBBLE_SIZE, -350, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 325 + 2.75 * (PAD_SIZE_X + 10) - 10 - 0.5 * BUBBLE_SIZE, -250, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 325 + 3.5 * (PAD_SIZE_X + 10) - 0.5 * BUBBLE_SIZE, -150, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10)
    ]

    return jump


def lamp_struct():
    lamp = [
        game.JumpPad(level, 0, 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, PAD_SIZE_X + 10, 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 2 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 3 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 4 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 5 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 6 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),

        game.JumpPad(level, 2 * (PAD_SIZE_X + 10), -300, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, -PAD_STRENGTH, True, 0),
        game.JumpPad(level, 3 * (PAD_SIZE_X + 10), -300, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, -PAD_STRENGTH, True, 0),
        game.JumpPad(level, 4 * (PAD_SIZE_X + 10), -300, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, -PAD_STRENGTH, True, 0),

        game.ScoreBubble(level, 4 * (PAD_SIZE_X + 10) - 1.5 * PAD_SIZE_X, -187, BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR,
                         10, 0),
        game.ScoreBubble(level, 3.5 * (PAD_SIZE_X + 10) - 0.5 * BUBBLE_SIZE, -75, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10, 0),
        game.ScoreBubble(level, 3.5 * (PAD_SIZE_X + 10) - 0.5 * BUBBLE_SIZE, -150, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10, 0),
        game.ScoreBubble(level, 3.5 * (PAD_SIZE_X + 10) - 0.5 * BUBBLE_SIZE, -225, BUBBLE_SIZE, BUBBLE_SIZE,
                         BUBBLE_COLOUR, 10, 0),
        game.ScoreBubble(level, 4 * (PAD_SIZE_X + 10), -112, BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10, 0),

        game.WorldObject(level, -5, PAD_SIZE_Y, 4 * (PAD_SIZE_X + 10), 40, FLOOR_COLOUR, 0),
        game.WorldObject(level, -5 + 4 * (PAD_SIZE_X + 10), PAD_SIZE_Y, 3 * (PAD_SIZE_X + 10) + 1, 40, FLOOR_COLOUR, 0),

        game.WorldObject(level, 2 * (PAD_SIZE_X + 10) - 5, -400, 3 * (PAD_SIZE_X + 10), 100, FLOOR_COLOUR, 0)
    ]
    return lamp


def bubble_struct():
    bubble = [
        game.JumpPad(level, 0, 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, PAD_SIZE_X + 10, 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 2 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 3 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 4 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 5 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),
        game.JumpPad(level, 6 * (PAD_SIZE_X + 10), 0, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0),

        game.WorldObject(level, -5, PAD_SIZE_Y, 7 * (PAD_SIZE_X + 10) + 5, 40, FLOOR_COLOUR, 0),

        game.ScoreBubble(level, 1.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75, BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 1.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 1.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - 2 * (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 1.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - 3 * (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),

        game.ScoreBubble(level, 3.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75, BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 3.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 3.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - 2 * (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 3.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - 3 * (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),

        game.ScoreBubble(level, 5.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75, BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 5.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 5.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - 2 * (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),
        game.ScoreBubble(level, 5.5 * PAD_SIZE_X + 10 - BUBBLE_SIZE * 0.5, -75 - 3 * (BUBBLE_SIZE + 25), BUBBLE_SIZE, BUBBLE_SIZE, BUBBLE_COLOUR, 10),

    ]
    return bubble


level = game.World(3200, 2560, 1, -640, -740, True, -4)

player1 = game.Player(level, (abs(level.camera_pos_x) + 0.5*1920 - 50), 780, 50, 100, (0, 0, 0), pygame.K_SPACE, pygame.K_a, pygame.K_d, pygame.K_LSHIFT, 5, 8, 0.25)

player2 = game.Player(level, (abs(level.camera_pos_x) + 0.5*1920 + 50), 780, 50, 100, (255, 255, 0), pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, 5, 8, 0.25)

danger_left = game.Danger(level, 640, 740, 40, 1080, "gas", (225, 20, 20), 0)
danger_right = game.Danger(level, 2520, 740, 40, 1080, "gas", (225, 20, 20), 0)

BUBBLE_SIZE = 40
BUBBLE_COLOUR = (200, 200, 220)

PAD_SIZE_X = 100
PAD_SIZE_Y = 20
PAD_COLOUR = (220, 220, 255)
PAD_STRENGTH = 12.5

PAD_SPAWN_Y = 1420

FLOOR_COLOUR = (30, 30, 30)

x = level.camera_pos_x*-1

spawn_platform = [
    game.WorldObject(level, x, 1420 + PAD_SIZE_Y, 633, 40, (30, 30, 30), 0),
    game.WorldObject(level, x+633, 1420 + PAD_SIZE_Y, 633, 40, (30, 30, 30), 0),
    game.WorldObject(level, x+1266, 1420 + PAD_SIZE_Y, 634, 40, (30, 30, 30), 0),
    game.WorldObject(level, x+1900, 1420 + PAD_SIZE_Y, 635, 40, (30, 30, 30), 0),
]

while len(spawn_platform) < 27:
    spawn_platform.append(game.JumpPad(level, x+5, PAD_SPAWN_Y, PAD_SIZE_X, PAD_SIZE_Y, PAD_COLOUR, PAD_STRENGTH, True, 0)),

    x = x + PAD_SIZE_X+10

spawn_scrolling = game.ScrollingGroup(level, spawn_platform, 3000, 3000, 1520, 640, 2560,
                                      0, 10000, level.scrolling_speed, 0, True)
spawn_scrolling.can_be_summoned = False


basic_bubble_platform_sg_1 = game.ScrollingGroup(level, bubble_struct(), 3000, 3000, PAD_SPAWN_Y-75-3*(BUBBLE_SIZE+25), 640, 2560, 0, 1000, level.scrolling_speed)
basic_bubble_platform_sg_1.teleport(basic_bubble_platform_sg_1.hub_x, basic_bubble_platform_sg_1.hub_y)

basic_bubble_platform_sg_2 = game.ScrollingGroup(level, bubble_struct(), 3000, 3000, PAD_SPAWN_Y-75-3*(BUBBLE_SIZE+25), 640, 2560, 0, 1000, level.scrolling_speed)
basic_bubble_platform_sg_1.teleport(basic_bubble_platform_sg_1.hub_x, basic_bubble_platform_sg_1.hub_y)


basic_jump_platform_sg_1 = game.ScrollingGroup(level, basic_jump_struct(), 3000, 3000, PAD_SPAWN_Y-400, 640, 2560, 0, 1000, level.scrolling_speed)
basic_jump_platform_sg_1.teleport(3000, 3000)

basic_jump_platform_sg_2 = game.ScrollingGroup(level, basic_jump_struct(), 3000, 3000, PAD_SPAWN_Y-400, 640, 2560, 0, 1000, level.scrolling_speed)
basic_jump_platform_sg_2.teleport(3000, 3000)


lamp_sg_1 = game.ScrollingGroup(level, lamp_struct(), 3000, 3000, PAD_SPAWN_Y-400, 640, 2560, 0, 1000, level.scrolling_speed)
lamp_sg_1.teleport(3000, 3000)

lamp_sg_2 = game.ScrollingGroup(level, lamp_struct(), 3000, 3000, PAD_SPAWN_Y-400, 640, 2560, 0, 1000, level.scrolling_speed)
lamp_sg_2.teleport(3000, 3000)
