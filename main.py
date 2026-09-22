import pygame
import random


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Trex Runner")
clock = pygame.time.Clock()
font = pygame.font.Font("font/ByteBounce.ttf", 40)
running = True
game_active = True
dt = 0
score = 0


def spawn_enemies(enemies_list):
    #tuples with 0 being the graphic and 1 the hitbox
    if enemies_list:
        for enemy in enemies_list:
            enemy[0].left -= 5
            enemy[1].midbottom = enemy[0].midbottom
            if enemy[0].bottom == 304:
                screen.blit(mushroom_surf, enemy[0])
                # pygame.draw.rect(screen , "red", enemy[1], 2)

            else:
                screen.blit(infected_surf, enemy[0])
                enemy[1].y -= 10
                # pygame.draw.rect(screen, "red", enemy[1], 2)

        return [enemy for enemy in enemies_list if enemy[0].right > -100]
    else:
        return[]


def check_collision(enemies_list):
    if enemies_list:
        for enemy in enemies_list:
            if player_hitbox.colliderect(enemy[1]):
                frozen_screen = screen.copy()
                game_active = False
                return game_active, frozen_screen
    return True, None

def increase_score(enemies_list, score):
        for enemy in enemies_list:
            if enemy[1].right <= player_hitbox.left and not enemy[2]:
                score +=1
                enemy[2]= True
        return score


def show_score(current_score):
    text_surface = font.render(f"Score: {current_score}", False, "Yellow")
    score = text_surface.get_rect(midtop=(400, 50))
    screen.blit(text_surface, score)


def game_over(current_score, highscore):
    game_over_surface = font.render("GAME OVER", False, "Yellow")
    game_over = game_over_surface.get_rect(center=(400,100))

    text_surface = font.render(f"Your score was: {current_score}", False, "Yellow")
    score = text_surface.get_rect(center=(400, 140))

    highscore_surface = font.render(f"Your Highscore is: {highscore}", False, "Yellow")
    highest_score = text_surface.get_rect(center=(400, 180))

    start_game_surface = font.render("Press space to restart", False, "Yellow")
    start_game= start_game_surface.get_rect(center=(400,220))

    overlay = pygame.Surface((800, 400), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 210))

    screen.blit(frozen_screen, (0, 0))
    screen.blit(overlay, (0, 0))
    screen.blit(game_over_surface, game_over)
    screen.blit(start_game_surface, start_game)
    screen.blit(text_surface, score)
    screen.blit(highscore_surface, highest_score)


#animations

def player_animated():
    global player_index, player_surf

    keys = pygame.key.get_pressed()

    if player.bottom < 300:
        player_surf = player_jump_frame
    elif keys[pygame.K_s]:
        player_index += 0.2
        if player_index >= len(player_duck_animation):
            player_index = 0

        player_surf = player_duck_animation[int(player_index)]
    else:
        player_index += 0.2
        if player_index >= len(player_animation):
            player_index = 0

        player_surf = player_animation[int(player_index)]

test_surface = pygame.image.load("graphics/background.jpg").convert()
background = pygame.transform.scale(test_surface, (800,400))


player_sprite_small = pygame.image.load("sprites/kuro/base/move.png").convert_alpha()
player_sprite = pygame.transform.scale_by(player_sprite_small, 3)
player_index = 0

player_animation = [
    player_sprite.subsurface(0,0,72,72),
    player_sprite.subsurface(72,0,72,72),
    player_sprite.subsurface(144,0,72,72),
    player_sprite.subsurface(216,0,72,72),
    player_sprite.subsurface(288,0,72,72),
    player_sprite.subsurface(360,0,72,72),
]

player_jump_small = pygame.image.load("sprites/kuro/base/jump.png").convert_alpha()
player_jump = pygame.transform.scale_by(player_jump_small, 3)

player_jump_frame = player_jump.subsurface(144,0,72,72)

player_duck_small = pygame.image.load("sprites/kuro/base/dash.png").convert_alpha()
scale_factor = 3
player_duck = pygame.transform.scale_by(player_duck_small, scale_factor)

player_duck_animation = [
    player_duck.subsurface(0*scale_factor,0,24*scale_factor,24*scale_factor),
    player_duck.subsurface(24*scale_factor,0,24*scale_factor,24*scale_factor),
    player_duck.subsurface(48*scale_factor,0,24*scale_factor,24*scale_factor),
    player_duck.subsurface(72*scale_factor,0,24*scale_factor,24*scale_factor),
    player_duck.subsurface(96*scale_factor,0,24*scale_factor,24*scale_factor),
    player_duck.subsurface(120*scale_factor,0,24*scale_factor,24*scale_factor),
]

player_surf = player_animation[player_index]
player = player_surf.get_rect(midbottom = (80,316))
player_hitbox = pygame.Rect(0,0,50,50)

player_gravity = 0
player_x_offset = 0

enemy_timer = pygame.USEREVENT +1
pygame.time.set_timer(enemy_timer,1200)

mushroom_timer = pygame.USEREVENT +2
pygame.time.set_timer(mushroom_timer, 200)

infected_timer = pygame.USEREVENT +3
pygame.time.set_timer(infected_timer, 200)

enemy_list = []


mushroom_surface_small = pygame.image.load("sprites/Forest_Monsters_FREE/Mushroom/Mushroom without VFX/Mushroom-Run.png").convert_alpha()
mushroom_surface = pygame.transform.scale_by(mushroom_surface_small, 1.6)
mushroom_index = 0

mushroom_animation = [
    mushroom_surface.subsurface(0,0,80*1.6,64*1.6),
    mushroom_surface.subsurface(80*1.6,0,80*1.6,64*1.6),
    mushroom_surface.subsurface(160*1.6,0,80*1.6,64*1.6),
    mushroom_surface.subsurface(240*1.6,0,80*1.6,64*1.6),
    mushroom_surface.subsurface(320*1.6,0,80*1.6,64*1.6),
    mushroom_surface.subsurface(400*1.6,0,80*1.6,64*1.6),
    mushroom_surface.subsurface(480*1.6,0,80*1.6,64*1.6),
    mushroom_surface.subsurface(560*1.6,0,80*1.6,64*1.6),
]

mushroom_surf = mushroom_animation[mushroom_index]

infected_surface_small = pygame.image.load("sprites/FlyingForestEnemies_FREE/Enemy3/Enemy3-Movement-In-Animation/Enemy3-Fly.png").convert_alpha()
scaling_fac = 1.5
infected_surface =pygame.transform.scale_by(infected_surface_small, scaling_fac)
infected_index = 0

infected_animation = [
    infected_surface.subsurface(0,0,64*scaling_fac,64*scaling_fac),
    infected_surface.subsurface(64*scaling_fac,0,64*scaling_fac,64*scaling_fac),
    infected_surface.subsurface(128*scaling_fac,0,64*scaling_fac,64*scaling_fac),
    infected_surface.subsurface(192*scaling_fac,0,64*scaling_fac,64*scaling_fac),
    infected_surface.subsurface(256*scaling_fac,0,64*scaling_fac,64*scaling_fac),
    infected_surface.subsurface(320*scaling_fac,0,64*scaling_fac,64*scaling_fac),
    infected_surface.subsurface(384*scaling_fac,0,64*scaling_fac,64*scaling_fac),
    infected_surface.subsurface(448*scaling_fac,0,64*scaling_fac,64*scaling_fac),
]

infected_surf = infected_animation[infected_index]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and player.bottom >=316:
            #jump
            if event.key == pygame.K_w:
                player_gravity = -19
            #duck
            if event.key == pygame.K_s:
                player_hitbox.update(0,0,60,43)
                player_x_offset = 10

        #while s is pressed stay ducked
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                player_hitbox.update(0,0,50,50)
                player_x_offset = 0

        if event.type == pygame.KEYDOWN and game_active == False:
            if event.key == pygame.K_SPACE:
                game_active = True
                score= 0
                enemy_list = []
        if game_active:
            if event.type == enemy_timer :
                enemy_x = random.randint(900, 1300)
                if random.randint(0,2):
                    enemy_list.append([mushroom_surf.get_rect(midbottom=(enemy_x,304)),pygame.Rect(0,0,50,50), False])
                else:
                    enemy_list.append([infected_surf.get_rect(midbottom = (enemy_x,270)),pygame.Rect(0,0,60,80), False])

            if event.type == mushroom_timer:
                mushroom_index += 1
                if mushroom_index >= len(mushroom_animation):
                    mushroom_index = 0

                mushroom_surf = mushroom_animation[int(mushroom_index)]

            if event.type == infected_timer:
                infected_index += 1
                if infected_index >= len(infected_animation):
                    infected_index = 0

                infected_surf = infected_animation[int(infected_index)]

    if game_active:
        screen.blit(background,(0,0))

        #implement exponetnial gravity for falling
        player_gravity += 1
        player.bottom += player_gravity


        if player.bottom >= 316:
            player.bottom = 316
            player_gravity = 0
        player_animated()
        screen.blit(player_surf, player)
        # offset the player hitbox to match the actual ground height
        player_hitbox.midbottom = player.midbottom

        player_hitbox.y += -12
        player_hitbox.x += player_x_offset

        enemy_list = spawn_enemies(enemy_list)

        game_active, frozen_screen = check_collision(enemy_list)

        # pygame.draw.rect(screen, "red", player_hitbox, 2)

        score = increase_score(enemy_list, score)

        show_score(score)

    else:
        with open("highscore.txt", "r") as data:
            highscore = int(data.readline())

        with open("highscore.txt", "w") as data:
            if score > highscore:
                data.write(str(score))
            else:
                data.write(str(highscore))

        game_over(score, highscore)


    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()



