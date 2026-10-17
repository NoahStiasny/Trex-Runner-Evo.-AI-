import pygame

class Player:
    def __init__(self,assets, network=None, fitness=None):
        self.network = network
        self.fitness = fitness

        self.gravity = 0
        self.x_offset = 0
        self.alive = True
        self.score = 0
        self.survival_frames = 0
        self.passed_obstacles = set()

        #create player visual
        self.rect = pygame.Rect(0, 0, 72, 72)
        self.rect.midbottom = (80, 316)
        #create player hitbox and offset it so it matches visual
        self.hitbox = pygame.Rect(0, 0, 50, 50)
        self.hitbox.midbottom = self.rect.midbottom
        self.hitbox.y -= 12

        #animation state
        self.assets = assets
        self.current_action = "run"
        self.index = 0
        self.surface = assets.run_animation[self.index]

    def update_player(self):

        #gravity
        self.gravity += 1
        self.rect.bottom += self.gravity

        if self.rect.bottom >=316:
            self.rect.bottom = 316
            self.gravity = 0

        self.hitbox.midbottom = self.rect.midbottom
        self.hitbox.y -= 12
        self.hitbox.x += self.x_offset


    def take_action(self, action):
        #adapting movement controls for Neural Network frame wise decision making
        #running
        if action == "run":
            self.hitbox.size = (50, 50)
            self.x_offset = 0
            self.current_action = "run"
        #jump
        elif action == "jump":
            self.hitbox.size = (50, 50)
            self.x_offset = 0
            if self.rect.bottom >= 316:
                self.gravity = -19

            self.current_action = "jump"
        #duck
        elif action == "duck":
            if self.rect.bottom >= 316:
                self.hitbox.size = (60, 43)
                self.x_offset = 10
                self.current_action = "duck"


    def animation(self):
        if self.rect.bottom < 316:
            self.surface = self.assets.jump_animation
        elif self.current_action == "duck":
            self.index +=0.2
            if self.index >= len(self.assets.duck_animation):
                self.index = 0
            self.surface = self.assets.duck_animation[int(self.index)]
        else:
            self.index += 0.2
            if self.index >= len(self.assets.run_animation):
                self.index = 0
            self.surface = self.assets.run_animation[int(self.index)]


    def show(self, screen):
        screen.blit(self.surface, self.rect)