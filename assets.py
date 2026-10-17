import pygame

class Assets:
    def __init__(self):
        self.run_animation = self.load_run_animation()
        self.jump_animation = self.load_jump_animation()
        self.duck_animation = self.load_duck_animation()
        self.mushroom_animation = self.load_mushroom_animation()
        self.infected_animation = self.load_infected_animation()


    def load_run_animation(self):
        player_sprite_small = pygame.image.load("sprites/kuro/base/move.png").convert_alpha()
        player_sprite = pygame.transform.scale_by(player_sprite_small, 3)

        player_run_animation = [
            player_sprite.subsurface(0, 0, 72, 72),
            player_sprite.subsurface(72, 0, 72, 72),
            player_sprite.subsurface(144, 0, 72, 72),
            player_sprite.subsurface(216, 0, 72, 72),
            player_sprite.subsurface(288, 0, 72, 72),
            player_sprite.subsurface(360, 0, 72, 72),
        ]

        return player_run_animation

    def load_duck_animation(self):
        player_duck_small = pygame.image.load("sprites/kuro/base/dash.png").convert_alpha()
        scale_factor = 3
        player_duck = pygame.transform.scale_by(player_duck_small, scale_factor)

        player_duck_animation = [
            player_duck.subsurface(0 * scale_factor, 0, 24 * scale_factor, 24 * scale_factor),
            player_duck.subsurface(24 * scale_factor, 0, 24 * scale_factor, 24 * scale_factor),
            player_duck.subsurface(48 * scale_factor, 0, 24 * scale_factor, 24 * scale_factor),
            player_duck.subsurface(72 * scale_factor, 0, 24 * scale_factor, 24 * scale_factor),
            player_duck.subsurface(96 * scale_factor, 0, 24 * scale_factor, 24 * scale_factor),
            player_duck.subsurface(120 * scale_factor, 0, 24 * scale_factor, 24 * scale_factor),
        ]
        return player_duck_animation

    def load_jump_animation(self):
        player_jump_small = pygame.image.load("sprites/kuro/base/jump.png").convert_alpha()
        player_jump = pygame.transform.scale_by(player_jump_small, 3)

        player_jump_animation = player_jump.subsurface(144, 0, 72, 72)
        return player_jump_animation

    def load_mushroom_animation(self):
        mushroom_surface_small = pygame.image.load(
            "sprites/Forest_Monsters_FREE/Mushroom/Mushroom without VFX/Mushroom-Run.png").convert_alpha()
        mushroom_surface = pygame.transform.scale_by(mushroom_surface_small, 1.6)

        mushroom_animation = [
            mushroom_surface.subsurface(0, 0, 80 * 1.6, 64 * 1.6),
            mushroom_surface.subsurface(80 * 1.6, 0, 80 * 1.6, 64 * 1.6),
            mushroom_surface.subsurface(160 * 1.6, 0, 80 * 1.6, 64 * 1.6),
            mushroom_surface.subsurface(240 * 1.6, 0, 80 * 1.6, 64 * 1.6),
            mushroom_surface.subsurface(320 * 1.6, 0, 80 * 1.6, 64 * 1.6),
            mushroom_surface.subsurface(400 * 1.6, 0, 80 * 1.6, 64 * 1.6),
            mushroom_surface.subsurface(480 * 1.6, 0, 80 * 1.6, 64 * 1.6),
            mushroom_surface.subsurface(560 * 1.6, 0, 80 * 1.6, 64 * 1.6),
        ]
        return mushroom_animation

    def load_infected_animation(self):
        infected_surface_small = pygame.image.load(
            "sprites/FlyingForestEnemies_FREE/Enemy3/Enemy3-Movement-In-Animation/Enemy3-Fly.png").convert_alpha()
        scaling_fac = 1.5
        infected_surface = pygame.transform.scale_by(infected_surface_small, scaling_fac)

        infected_animation = [
            infected_surface.subsurface(0, 0, 64 * scaling_fac, 64 * scaling_fac),
            infected_surface.subsurface(64 * scaling_fac, 0, 64 * scaling_fac, 64 * scaling_fac),
            infected_surface.subsurface(128 * scaling_fac, 0, 64 * scaling_fac, 64 * scaling_fac),
            infected_surface.subsurface(192 * scaling_fac, 0, 64 * scaling_fac, 64 * scaling_fac),
            infected_surface.subsurface(256 * scaling_fac, 0, 64 * scaling_fac, 64 * scaling_fac),
            infected_surface.subsurface(320 * scaling_fac, 0, 64 * scaling_fac, 64 * scaling_fac),
            infected_surface.subsurface(384 * scaling_fac, 0, 64 * scaling_fac, 64 * scaling_fac),
            infected_surface.subsurface(448 * scaling_fac, 0, 64 * scaling_fac, 64 * scaling_fac),
        ]
        return infected_animation