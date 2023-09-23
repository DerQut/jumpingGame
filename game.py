import random

import pygame
import numpy

import assets


class Game:

    def __init__(self, window_size_x, window_size_y, window_flags):

        self.window_size_x = window_size_x
        self.window_size_y = window_size_y
        self.window_flags = window_flags

        self.screen = pygame.display.set_mode((self.window_size_x, self.window_size_y), self.window_flags)

        self.running = True

    def run(self):

        self.screen.fill((128, 128, 128))

        for world in World.all:

            if world.active:

                world.optimise()

                for scrolling_group in world.scrolling_groups:
                    scrolling_group.move()

                for world_object in world.world_objects:
                    if world_object.active:

                        if world_object.obj_type == "player":
                            if world_object.alive:
                                world_object.score_sound_check()
                                world_object.collision_check()
                                world_object.walk()
                                world_object.crouch()

                        elif world_object.obj_type == "pad":
                            if world_object.is_on:
                                world_object.force_jump()

                        elif world_object.obj_type == "danger":
                            world_object.collide_kill()

                        elif world_object.obj_type == "bubble":
                            world_object.give_score()

                world.render()
                self.screen.blit(world.surface, (world.camera_pos_x, world.camera_pos_y))

                break

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.WINDOWCLOSE:
                self.running = False

            for player in Player.all_players:
                if player.world.active:
                    player.control_check(event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                for world in World.all:
                    if world.active:
                        for scrolling_group in world.scrolling_groups:
                            scrolling_group.teleport(320, 1600)
                            scrolling_group.x_velocity = -0.5
                        break

        pygame.display.update(pygame.rect.Rect(0, 0, 1920, 1080))


class WorldObject:

    all = []
    all_rects = []

    def __init__(self, world, x_cord, y_cord, x_size, y_size, colour, gravity=0.01, x_velocity=0.00, y_velocity=0.00, has_collision=True):

        self.world = world

        self.x_cord = x_cord
        self.y_cord = y_cord

        self.x_size = x_size
        self.y_size = y_size

        self.gravity = gravity

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.rect = pygame.rect.Rect(self.x_cord, self.y_cord, self.x_size, self.y_size)

        self.colour = colour

        self.id = len(WorldObject.all)

        self.has_collision = has_collision
        if not self.has_collision:
            self.id = self.id * -1

        WorldObject.all.append(self)
        WorldObject.all_rects.append(self.rect)

        #why isn't this in the Player class wtf
        self.can_jump = False

        self.can_gravity_pull = gravity

        self.active = True

        self.obj_type = "object"

        world.world_objects.append(self)

    def __repr__(self):
        return f"game.WorldObject at ({self.x_cord}, {self.y_cord}) with an ID of {self.id}"

    def blind_move(self):
        self.y_cord = self.y_cord + self.y_velocity
        self.x_cord = self.x_cord + self.x_velocity

        self.rect.update(self.x_cord, self.y_cord, self.x_size, self.y_size)

    def smart_move(self):

        x_space = self.x_velocity
        y_space = self.y_velocity
        self.can_gravity_pull = True

        for obj in self.world.world_objects:

            if numpy.sign(obj.id) > 0 and obj.active:

                if self.x_velocity > 0 and obj.rect.left >= self.rect.right:
                    if obj.rect.left - self.rect.right < x_space:
                        if (obj.rect.top <= self.rect.top < obj.rect.bottom) or (obj.rect.top > self.rect.bottom > obj.rect.bottom):
                            x_space = obj.rect.left - self.rect.right

                elif self.x_velocity < 0 and self.rect.left >= obj.rect.right:
                    if obj.rect.right - self.rect.left > x_space:
                        if (obj.rect.top <= self.rect.top < obj.rect.bottom) or (obj.rect.top > self.rect.bottom > obj.rect.bottom):
                            x_space = obj.rect.right - self.rect.left

                if self.y_velocity > 0 and obj.rect.top >= self.rect.bottom:
                    if obj.rect.top - self.rect.bottom < y_space:
                        if (obj.rect.left < self.rect.right < obj.rect.right) or (obj.rect.left < self.rect.left < obj.rect.right):
                            y_space = obj.rect.top - self.rect.bottom

                elif self.y_velocity < 0 and self.rect.top >= obj.rect.bottom:
                    if obj.rect.bottom - self.rect.top > y_space:
                        if (obj.rect.left < self.rect.right < obj.rect.right) or (obj.rect.left < self.rect.left < obj.rect.right):
                            y_space = obj.rect.bottom - self.rect.top

        if y_space == self.y_velocity:
            self.y_cord = self.y_cord + self.y_velocity
        else:
            self.y_cord = self.y_cord + y_space
            self.can_gravity_pull = False
            self.can_jump = True
            self.y_velocity = 0.00

        if x_space == self.x_velocity:
            self.x_cord = self.x_cord + self.x_velocity
        else:
            self.x_cord = self.x_cord + x_space
            self.x_velocity = 0.00

        self.rect.update(self.x_cord, self.y_cord, self.x_size, self.y_size)

    def apply_gravity(self):

        if self.can_gravity_pull:

            self.y_velocity = self.y_velocity + self.gravity * self.world.global_gravity
            self.can_jump = False


class Player(WorldObject):

    all_players = []

    def __init__(self, world, x_cord, y_cord, x_size, y_size, colour, jump_key, left_key, right_key, crouch_key, walking_speed, jump_height, gravity, x_velocity=0.00, y_velocity=0.00):
        super().__init__(world, x_cord, y_cord, x_size, y_size, colour, gravity, x_velocity, y_velocity)

        self.jump_key = jump_key
        self.left_key = left_key
        self.right_key = right_key
        self.crouch_key = crouch_key

        self.jump_height = jump_height

        self.walking_speed = walking_speed
        self.can_jump = False
        self.left_key_pressed = False
        self.right_key_pressed = False
        self.crouch_key_pressed = False

        self.base_x_size = x_size
        self.base_y_size = y_size
        self.base_walking_speed = walking_speed
        self.base_gravity = gravity

        self.id = self.id * -1

        self.alive = True

        self.score = 0
        self.score_cache = 0
        self.score_bubble_chain = 0
        self.score_multiplier = 1
        self.time_since_last_bubble = 1

        self.obj_type = "player"

        Player.all_players.append(self)

    def die(self):

        if self.alive:
            self.alive = False
            self.y_size = 0.25*self.y_size
            self.y_velocity = -1
            self.x_velocity = 0

            self.rect.update(self.x_cord, self.y_cord, self.x_size, self.y_size)

    def walk(self):

        if self.right_key_pressed and not self.left_key_pressed:
            self.x_velocity = self.walking_speed
        elif self.left_key_pressed and not self.right_key_pressed:
            self.x_velocity = self.walking_speed * -1

        else:
            if self.x_velocity > 0:
                self.x_velocity = self.x_velocity - 0.02 * self.walking_speed
                if self.x_velocity < 0:
                    self.x_velocity = 0
            elif self.x_velocity < 0:
                self.x_velocity = self.x_velocity + 0.02 * self.walking_speed
                if self.x_velocity > 0:
                    self.x_velocity = 0

    def crouch(self):
        if self.crouch_key_pressed:
            if self.y_size > 0.5 * self.base_y_size:
                self.y_size = self.y_size - 0.05 * self.base_y_size
                self.y_cord = self.y_cord + 0.05 * self.base_y_size

                self.walking_speed = 0.5*self.base_walking_speed
                self.gravity = 2*self.base_gravity

            self.rect.update(self.x_cord, self.y_cord, self.x_size, self.y_size)

        else:
            if self.y_size < self.base_y_size:
                self.y_size = self.y_size + 0.05 * self.base_y_size
                self.y_cord = self.y_cord - 0.05 * self.base_y_size

                self.walking_speed = self.base_walking_speed
                self.gravity = self.base_gravity

            self.rect.update(self.x_cord, self.y_cord, self.x_size, self.y_size)

    def control_check(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == self.right_key:
                self.right_key_pressed = True

            if event.key == self.left_key:
                self.left_key_pressed = True

            if event.key == self.crouch_key:
                self.crouch_key_pressed = True

            if event.key == self.jump_key:
                if self.can_jump and self.alive:
                    self.y_velocity = -1 * self.jump_height
                    assets.play_random_sound(assets.sfx_jump)
                    self.can_jump = False

        if event.type == pygame.KEYUP:
            if event.key == self.right_key:
                self.right_key_pressed = False

            if event.key == self.left_key:
                self.left_key_pressed = False

            if event.key == self.crouch_key:
                self.crouch_key_pressed = False

    def collision_check(self):

        for obj in self.world.world_objects:

            if obj.id > 0:

                if self.rect.colliderect(obj.rect):

                    if self.rect.left < obj.rect.left < self.rect.right:
                        self.x_cord = obj.rect.left - self.x_size

                    elif self.rect.left < obj.rect.right < self.rect.right:
                        self.x_cord = obj.rect.right

                    elif self.rect.bottom > obj.rect.top > self.rect.top:
                        self.y_cord = obj.rect.top - self.y_size

                    elif self.rect.bottom > obj.rect.bottom > self.rect.top:
                        self.y_cord = obj.rect.bottom

                    self.rect.update(self.x_cord, self.y_cord, self.x_size, self.y_size)

        for obj in self.world.world_objects:
            if obj.id > 0:
                if self.rect.colliderect(obj.rect):
                    self.die()
                    break

    def score_sound_check(self):

        if self.time_since_last_bubble == 0:
            if self.score_bubble_chain%5 == 0 and self.score_bubble_chain:
                self.score_multiplier = self.score_multiplier + 1
            if self.score_bubble_chain <= 15:
                assets.sfx_score_bubble[self.score_bubble_chain-1].play()
            else:
                if self.score_bubble_chain % 2 == 0:
                    assets.sfx_score_bubble[13].play()
                elif (self.score_bubble_chain-15) % 4 == 0:
                    assets.sfx_score_bubble[14].play()
                else:
                    assets.sfx_score_bubble[12].play()

        elif self.time_since_last_bubble == 100:
            print(self.score, self.score_multiplier, self.score_cache)
            self.score = self.score + self.score_cache * self.score_multiplier
            self.score_bubble_chain = 0
            self.score_cache = 0

            if self.score_multiplier > 1:
                assets.play_random_sound(assets.sfx_multiplier_end)

            self.score_multiplier = 1

            print(self.score)

        self.time_since_last_bubble = self.time_since_last_bubble+1


class JumpPad(WorldObject):

    all_pads = []

    def __init__(self, world, x_cord, y_cord, x_size, y_size, colour, jump_height, is_on=True, gravity=0, x_velocity=0, y_velocity=0):
        super().__init__(world, x_cord, y_cord, x_size, y_size, colour, gravity, x_velocity, y_velocity)

        self.is_on = is_on
        self.jump_height = jump_height

        self.obj_type = "pad"

        JumpPad.all_pads.append(self)

    def force_jump(self):

        for player in Player.all_players:
            if self.is_on and ((abs(player.rect.bottom - self.rect.top) < 3 and self.jump_height > 0) or (abs(player.rect.top - self.rect.bottom) < 3 and self.jump_height < 0)):
                if (self.rect.left < player.rect.right < self.rect.right) or (self.rect.right > player.rect.left > self.rect.left):
                    player.y_velocity = -1 * self.jump_height * self.world.global_gravity
                    assets.play_random_sound(assets.sfx_pad)


class Danger(WorldObject):

    all_dangers = []

    def __init__(self, world, x_cord, y_cord, x_size, y_size, danger_type, colour, gravity=0, x_velocity=0, y_velocity=0):
        super().__init__(world, x_cord, y_cord, x_size, y_size, colour, gravity, x_velocity, y_velocity)

        self.id = self.id * -1
        self.danger_type = danger_type
        self.obj_type = "danger"
        Danger.all_dangers.append(self)

    def collide_kill(self):

        for player in Player.all_players:
            if player.alive:
                if self.rect.colliderect(player.rect):
                    player.die()

                    if self.danger_type == "gas":
                        assets.play_random_sound(assets.sfx_death_gas)
                    elif self.danger_type == "spike":
                        assets.play_random_sound(assets.sfx_stabbed)


class World:
    all = []

    def __init__(self, x_size, y_size, global_gravity=1, camera_pos_x=0, camera_pos_y=0, active=False, scrolling_speed=0):

        self.x_size = x_size
        self.y_size = y_size
        self.global_gravity = global_gravity
        self.active = active

        self.surface = pygame.surface.Surface((self.x_size, self.y_size))

        self.world_objects = []

        self.camera_pos_x = camera_pos_x
        self.camera_pos_y = camera_pos_y

        self.scrolling_speed = scrolling_speed
        self.scrolling_groups = []

        World.all.append(self)

    def render(self):

        self.surface.fill((128, 128, 128))

        for obj in self.world_objects:

            obj.apply_gravity()

            if numpy.sign(obj.id) < 1:
                obj.smart_move()
            else:
                obj.blind_move()

            if obj.active:
                self.surface.fill(obj.colour, obj.rect)

    def optimise(self):
        for world_object in self.world_objects:
            if world_object.obj_type != "bubble":
                if (world_object.rect.right < self.camera_pos_x * -1) or (world_object.rect.left > self.camera_pos_x * -1 + 1920):
                    world_object.active = False
                else:
                    world_object.active = True


class ScrollingGroup:

    def __init__(self, level, objects, hub_x, hub_y, spawn_y, left_boundary, right_boundary, upper_boundary, lower_boundary, x_velocity=0, y_velocity=0, is_first=False):

        self.objects = objects

        self.is_first = is_first

        self.spawn_y = spawn_y

        self.hub_x = hub_x
        self.hub_y = hub_y

        self.x_velocity = x_velocity
        self.y_velocity = y_velocity

        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.lower_boundary = lower_boundary
        self.upper_boundary = upper_boundary

        self.level = level

        self.can_be_summoned = True
        self.can_summon = True

        if len(self.objects):
            i = 1
            self.big_rect = objects[0].rect

            while i < len(objects):
                self.big_rect = pygame.Rect.union(self.big_rect, self.objects[i].rect)
                i = i + 1

        self.level.scrolling_groups.append(self)

    def move(self):
        for obj in self.objects:

            obj.x_cord = obj.x_cord + self.x_velocity
            obj.y_cord = obj.y_cord + self.y_velocity

            obj.rect.update(obj.x_cord, obj.y_cord, obj.x_size, obj.y_size)

        self.recalculate_rect()

        if 0 >= (self.big_rect.right - self.right_boundary) >= -1:
            if self.can_summon:
                ScrollingGroup.spawn_new_scrolling_group(self.level)
                self.can_summon = False

        if self.big_rect.right < self.left_boundary:
            print("BOUNDARY BREACHED")
            self.teleport(self.hub_x, self.hub_y)
            print(self.big_rect.right, self.left_boundary)
            if not self.is_first:
                self.can_be_summoned = True

    def teleport(self, x, y):

        x_offset = x - self.big_rect.left
        y_offset = y - self.big_rect.top

        for obj in self.objects:
            obj.x_cord = obj.x_cord + x_offset
            obj.y_cord = obj.y_cord + y_offset

            obj.rect.update(obj.x_cord, obj.y_cord, obj.x_size, obj.y_size)

        self.recalculate_rect()
        self.x_velocity = 0
        self.y_velocity = 0

    def recalculate_rect(self):
        if len(self.objects):
            i = 1
            self.big_rect = self.objects[0].rect

            while i < len(self.objects):
                self.big_rect = pygame.Rect.union(self.big_rect, self.objects[i].rect)
                i = i + 1

    @classmethod
    def spawn_new_scrolling_group(cls, level):

        if len(level.scrolling_groups):

            candidates = 0
            for sg in level.scrolling_groups:
                if sg.can_be_summoned and not sg.is_first:
                    candidates = candidates + 1

            if candidates:

                while True:

                    random_num = random.randint(0, len(level.scrolling_groups)-1)

                    if (not level.scrolling_groups[random_num].is_first) and level.scrolling_groups[random_num].can_be_summoned:

                        level.scrolling_groups[random_num].teleport(level.scrolling_groups[random_num].right_boundary, level.scrolling_groups[random_num].spawn_y)
                        level.scrolling_groups[random_num].x_velocity = level.scrolling_speed
                        level.scrolling_groups[random_num].can_be_summoned = False
                        level.scrolling_groups[random_num].can_summon = True
                        print("DONE", level.scrolling_groups[random_num].big_rect.left)
                        break

class ScoreBubble(WorldObject):

    all_bubbles = []

    def __init__(self, world, x_cord, y_cord, x_size, y_size, colour, score, gravity=0, x_velocity=0, y_velocity=0):
        super().__init__(world, x_cord, y_cord, x_size, y_size, colour, gravity, x_velocity, y_velocity)

        self.score = score

        self.id = self.id * -1

        self.obj_type = "bubble"

        self.can_give_score = True

        ScoreBubble.all_bubbles.append(self)

    def give_score(self):

        for player in Player.all_players:
            if self.rect.colliderect(player.rect) and player.alive and self.can_give_score and player.world.active:
                player.score_cache = player.score_cache + self.score
                player.score_bubble_chain = player.score_bubble_chain + 1
                player.time_since_last_bubble = 0
                self.can_give_score = False
                self.active = False
