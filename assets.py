import random
import pygame


def play_random_sound(list):
    if len(list):
        list[random.randint(0, len(list)-1)].play()


pygame.mixer.init()

sfx_jump = [
    pygame.mixer.Sound("assets/sounds/jump_whoosh_01.wav"),
    pygame.mixer.Sound("assets/sounds/jump_whoosh_02.wav"),
    pygame.mixer.Sound("assets/sounds/jump_whoosh_03.wav"),
    pygame.mixer.Sound("assets/sounds/jump_whoosh_04.wav"),
    pygame.mixer.Sound("assets/sounds/jump_whoosh_05.wav")
]

sfx_pad = [
    pygame.mixer.Sound("assets/sounds/bouncer_low_01.wav"),
    pygame.mixer.Sound("assets/sounds/bouncer_low_02.wav"),
    pygame.mixer.Sound("assets/sounds/bouncer_low_03.wav"),
    pygame.mixer.Sound("assets/sounds/bouncer_low_04.wav"),
]

sfx_death_gas = [
    pygame.mixer.Sound("assets/sounds/gas_death_01.wav"),
    pygame.mixer.Sound("assets/sounds/gas_death_02.wav")
]

sfx_stabbed = [
    pygame.mixer.Sound("assets/sounds/stabbed_01.wav"),
    pygame.mixer.Sound("assets/sounds/stabbed_02.wav")
]