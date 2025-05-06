import pygame
import sys
from pygame import mixer
from random import randint
from menu import menu
from config import (
    window, img_background, player_ship, enemy_ship, shots,
    sound_missil, sound_explosion, sound_collision
)

#Inicializa pygame e mixer
pygame.init()
mixer.init()

#Chama menu na função principal
result = menu()
if result == "exit": #Caso usuario escolha fechar o jogo retorna fim da aplicação
    pygame.quit()
    sys.exit()

#Musica de fundo do GAME junto com um loop infinito.
pygame.mixer_music.stop()
pygame.mixer_music.load("assets/sounds/sound_game.mp3")
pygame.mixer_music.play(-1)

#Variaveis usadas no projeto
game_state = {
    "target_shot": False,
    "localplayer_x": 360,
    "localplayer_y": 480,
    "speed_ship": 12,
    "enemy_x": randint(5, 716),
    "enemy_y": -100,
    "speed_enemy": 10,
    "missil_x": 315,
    "missil_y": 440,
    "speed_missil": 25,
    "bg_y": 0,
    "paused": False,
    "running": True
}

#Função para pausar/retomar música do GAME ao pressionar "P"
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state["running"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if pygame.mixer_music.get_busy():
                    pygame.mixer_music.pause()
                else:
                    pygame.mixer_music.unpause()

#Define as setas para controlar as movimentações do player(nave)
def update():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        game_state["localplayer_y"] = max(9, game_state["localplayer_y"] - game_state["speed_ship"])
    if keys[pygame.K_DOWN]:
        game_state["localplayer_y"] = min(510, game_state["localplayer_y"] + game_state["speed_ship"])
    if keys[pygame.K_LEFT]:
        game_state["localplayer_x"] = max(5, game_state["localplayer_x"] - game_state["speed_ship"])
    if keys[pygame.K_RIGHT]:
        game_state["localplayer_x"] = min(716, game_state["localplayer_x"] + game_state["speed_ship"])
    if keys[pygame.K_SPACE] and not game_state["target_shot"]: #Pressionar ESPAÇO atira nos inimigos
        sound_missil.play() #Chama o som ao atirar
        game_state["target_shot"] = True
        game_state["missil_x"], game_state["missil_y"] = game_state["localplayer_x"] + 30, game_state["localplayer_y"]

    if game_state["target_shot"]:
        game_state["missil_y"] -= game_state["speed_missil"]
        if game_state["missil_y"] < 0:
            game_state["target_shot"] = False

    game_state["enemy_y"] += game_state["speed_enemy"]
    if game_state["enemy_y"] > 500:
        game_state["enemy_y"], game_state["enemy_x"] = randint(-100, -40), randint(5, 716) #Define onde os inimigos vão aparecer

    check_collision()

    game_state["bg_y"] += 5 #Velocidade da imagem background do game
    if game_state["bg_y"] >= img_background.get_height():
        game_state["bg_y"] = 0

#Função para checar a colisão do player(NAVE)
def check_collision():
    player_rect = player_ship.get_rect(topleft=(game_state["localplayer_x"], game_state["localplayer_y"]))
    enemy_rect = enemy_ship.get_rect(topleft=(game_state["enemy_x"], game_state["enemy_y"]))
    tiro_rect = shots.get_rect(topleft=(game_state["missil_x"], game_state["missil_y"]))

    if player_rect.colliderect(enemy_rect) or enemy_rect.y > 500:
        sound_collision.play()
        game_state["enemy_y"], game_state["enemy_x"] = randint(-1000, -100), randint(5, 716)

    elif tiro_rect.colliderect(enemy_rect):
        sound_explosion.set_volume(0.6)
        sound_explosion.play()
        game_state["enemy_y"], game_state["enemy_x"] = randint(-1000, -100), randint(5, 716)
        game_state["target_shot"] = False

#Função para chamar a imagem de fundo e as naves(players)
def draw():
    bg_height = img_background.get_height()
    window.blit(img_background, (0, game_state["bg_y"]))
    window.blit(img_background, (0, game_state["bg_y"] - bg_height))

    window.blit(player_ship, (game_state["localplayer_x"], game_state["localplayer_y"]))
    window.blit(enemy_ship, (game_state["enemy_x"], game_state["enemy_y"]))

    if game_state["target_shot"]:
        window.blit(shots, (game_state["missil_x"], game_state["missil_y"]))

    pygame.display.update()

#Define o fps do game para 60 para evitar que a imagem fique "teleportando"
clock = pygame.time.Clock()
while game_state["running"]:
    handle_events()
    if not game_state["paused"]:
        update()
    draw()
    clock.tick(60)
