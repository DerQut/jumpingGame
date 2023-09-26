import random
import pygame

pygame.font.init()

font = pygame.font.SysFont("Arial", 60)

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
    pygame.mixer.Sound("assets/sounds/bouncer_low_04.wav")
]

sfx_death_gas = [
    pygame.mixer.Sound("assets/sounds/gas_death_01.wav"),
    pygame.mixer.Sound("assets/sounds/gas_death_02.wav")
]

sfx_stabbed = [
    pygame.mixer.Sound("assets/sounds/stabbed_01.wav"),
    pygame.mixer.Sound("assets/sounds/stabbed_02.wav")
]

sfx_score_bubble = [
    pygame.mixer.Sound("assets/sounds/Score_Bubble1.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble2.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble3.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble4.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble5.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble6.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble7.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble8.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble9.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble10.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble11.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble12.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble13.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble14.wav"),
    pygame.mixer.Sound("assets/sounds/Score_Bubble15.wav"),
]

sfx_multiplier_end = [
    pygame.mixer.Sound("assets/sounds/resource_time_out_2_01.wav"),
    pygame.mixer.Sound("assets/sounds/resource_time_out_2_02.wav")
]