import pygame

class Obstacles:
    def __init__(self, assets, enemy_type, x_position):
        self.enemy_type = enemy_type
        self.assets = assets
        self.x_position = x_position

        self.speed = 5
        self.state = False
        self.index = 0

        if self.enemy_type == "mushroom":
            self.hitbox = pygame.Rect(0,0,50,50)
            self.visual = self.assets.mushroom_animation[self.index]
            self.rect = self.visual.get_rect(midbottom=(self.x_position,304))
            self.hitbox.midbottom = self.rect.midbottom
            self.animation_frames = self.assets.mushroom_animation


        elif self.enemy_type == "infected":
            self.hitbox = pygame.Rect(0, 0, 60, 80)
            self.visual = self.assets.infected_animation[self.index]
            self.rect = self.visual.get_rect(midbottom = (self.x_position,265))
            self.hitbox.midbottom = self.rect.midbottom
            self.animation_frames = self.assets.infected_animation

    def update(self):
        self.rect.left -= self.speed
        if self.enemy_type == "mushroom":
            self.hitbox.midbottom = self.rect.midbottom
        else:
            self.hitbox.center = self.rect.center


    def animation(self):
        #update animation with frames rather than pygame timer
        self.index += 0.2

        if self.index >= len(self.animation_frames):
            self.index = 0

        self.visual = self.animation_frames[int(self.index)]

    def show(self, screen):
        screen.blit(self.visual, self.rect)