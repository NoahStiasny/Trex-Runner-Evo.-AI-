import pygame
import numpy as np
import random
from player import Player
from assets import Assets
from obstacles import Obstacles
from neural_network import NeuralNetwork

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Trex Runner")
clock = pygame.time.Clock()
font = pygame.font.Font("font/ByteBounce.ttf", 40)
running = True
game_active = True
dt = 0
score = 0
enemy_list=[]
player_list = []
generation = 1

actions = {
                0: "run",
                1: "jump",
                2: "duck"
            }


def check_collision(enemies_list, players_list):
    if enemies_list:
        for enemy in enemies_list:
            for player in players_list:
                if player.hitbox.colliderect(enemy.hitbox)and player.alive == True:
                    player.alive= False



def check_game_status(players_list):
    if all(not player.alive for player in players_list):
        frozen_screen = screen.copy()
        return False, frozen_screen

    return True, None

def increase_score(enemies_list, players_list):
    for enemy in enemies_list:
        for player in players_list:
            if not player.alive:
                continue
            if enemy.hitbox.right <= player.hitbox.left:
                if enemy not in player.passed_obstacles:
                    player.score += 1
                    player.passed_obstacles.add(enemy)


def show_score(players_list, generation_count):
    best_score = 0
    for player in players_list:
            if player.score > best_score:
                best_score = player.score
    text_surface = font.render(f"Score: {best_score}", False, "Yellow")
    score = text_surface.get_rect(midtop=(300, 50))
    screen.blit(text_surface, score)

    generation_surface = font.render(f"Generation: {generation_count}", False, "Yellow")
    generation = generation_surface.get_rect(midtop=(500, 50))
    screen.blit(generation_surface, generation)


def game_over(current_score, highscore):
    game_over_surface = font.render("GAME OVER", False, "Yellow")
    game_over = game_over_surface.get_rect(center=(400,100))

    text_surface = font.render(f"Your score was: {current_score}", False, "Yellow")
    score = text_surface.get_rect(center=(400, 140))

    highscore_surface = font.render(f"Your Highscore is: {highscore}", False, "Yellow")
    highest_score = highscore_surface.get_rect(center=(400, 180))

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


def reset_game():
    global enemy_list, game_active, score, player_list, generation

    player_list = mutation()
    score = 0
    enemy_list = []
    game_active = True
    generation +=1

def get_game_state(player, enemies_list):
    closest_distance = 1.0
    closest_enemy = None
    enemy_type = 0

    for enemy in enemies_list:
        current_distance = (enemy.hitbox.left - player.hitbox.right) / 800

        if enemy.hitbox.right <= player.hitbox.left:
            continue

        if current_distance < closest_distance:
            closest_distance = current_distance
            closest_enemy = enemy

            if enemy.enemy_type == "mushroom":
                enemy_type = 0
            else:
                enemy_type = 1

    player_height = player.hitbox.top/400
    vertical_velocity =player.gravity/20

    return np.array([closest_distance,enemy_type,player_height,vertical_velocity])

def calculate_fitness(players_list):
    for player in players_list:
        fitness_score = player.survival_frames / 60 + 10 * player.score
        player.fitness = fitness_score
    fitness_ranking = sorted(players_list, key=lambda player: player.fitness, reverse=True)
    return fitness_ranking

def select_parents():
    fitness_ranking = calculate_fitness(player_list)
    top_five = fitness_ranking[:5]
    return top_five

def mutate_array(array, mutation_rate = 0.1, mutation_strength = 0.1):
    mutation = np.random.normal(0, mutation_strength, array.shape)
    mask = np.random.random(array.shape) < mutation_rate

    mutated_array = array +(mask * mutation)

    return mutated_array

def mutation():
    new_population = []
    parents = select_parents()
    for player in parents:
        weights1 = player.network.weights1
        weights2 = player.network.weights2
        biases1 = player.network.biases1
        biases2 = player.network.biases2

        w_b_list = [weights1,weights2,biases1,biases2]

        for i in range(9):
            mutated_list = []
            for entry in w_b_list:
                mutated_list.append(mutate_array(entry))
            new_population.append(Player(assets=assets, network=NeuralNetwork(weights_1= mutated_list[0],weights_2=mutated_list[1], biases_1=mutated_list[2], biases_2=mutated_list[3])))

        new_population.append(Player(assets=assets, network=NeuralNetwork(weights_1=weights1,weights_2=weights2,biases_1=biases1,biases_2=biases2)))
    return new_population


test_surface = pygame.image.load("graphics/background.jpg").convert()
background = pygame.transform.scale(test_surface, (800,400))

assets = Assets()

for i in range(50):
    player_list.append(Player(assets=assets, network=NeuralNetwork()))

enemy_timer = pygame.USEREVENT +1
pygame.time.set_timer(enemy_timer,1200)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                reset_game()

        #if event.type == pygame.KEYDOWN and player1.rect.bottom >=316:
            #jump
         #   if event.key == pygame.K_w:
           #     player1.take_action("jump")
            #duck
          #  if event.key == pygame.K_s:
            #    player1.take_action("duck")

        #while s is pressed stay ducked
        #if event.type == pygame.KEYUP:
          #  if event.key == pygame.K_s:
#                player1.take_action("run")

        if event.type == pygame.KEYDOWN and game_active == False:
            if event.key == pygame.K_SPACE:
                reset_game()

        if game_active:
            if event.type == enemy_timer :
                enemy_x = random.randint(900, 1300)
                if random.randint(0,2):
                    enemy_list.append(Obstacles(assets=assets,enemy_type="mushroom", x_position=enemy_x))
                else:
                    enemy_list.append(Obstacles(assets=assets, enemy_type="infected", x_position=enemy_x))

    if game_active:
        screen.blit(background,(0,0))


        for player in player_list:
            state = get_game_state(player, enemy_list)
            if not player.alive:
                continue
            prediction = player.network.predict(state)

            player.take_action(actions[prediction])

            player.update_player()
            player.animation()
            player.show(screen)
            player.survival_frames += 1

        if enemy_list:
            for enemy in enemy_list:
                enemy.update()
                enemy.animation()
                enemy.show(screen)

            enemy_list = [
                    enemy for enemy in enemy_list
                    if enemy.rect.right >= 0
                ]

        check_collision(enemy_list, player_list)

        increase_score(enemy_list, player_list)

        show_score(player_list, generation)

        game_active, frozen_screen = check_game_status(player_list)

        best_score = max(player.score for player in player_list)

        if not game_active:
            reset_game()

    else:
        with open("highscore.txt", "r") as data:
            highscore = int(data.readline())

        with open("highscore.txt", "w") as data:
            if best_score > highscore:
                data.write(str(best_score))
            else:
                data.write(str(highscore))

        game_over(best_score, highscore)

    pygame.display.flip()
    dt = clock.tick(60)

pygame.quit()



