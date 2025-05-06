import pygame
from pathlib import Path
#inicializa o pygame e o mixer
pygame.init()
pygame.mixer.init()

#Função para achar as pastas que envolve o game
ASSETS_PATH = Path("assets")
SOUND_PATH = ASSETS_PATH / "sounds"
IMAGE_PATH = ASSETS_PATH / "imagens"

#Tamanho da janela e nome do game
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Galaxy Battlefront')

#Função para carregar os sons
def load_sounds(filename):
    return pygame.mixer.Sound(str(SOUND_PATH / filename))

sound_missil = load_sounds("sound_missil.mp3")
sound_explosion = load_sounds("sound_explosion.mp3")
sound_collision = load_sounds("sound_collision.mp3")
sound_collision.set_volume(0.1)
sound_menu = load_sounds("sound_menu.mp3")

#Função para carregar as imagens
def load_img(filename, imgsize=None):
    img = pygame.image.load(str(IMAGE_PATH / filename))
    if imgsize:
        img = pygame.transform.scale(img, imgsize)
    return img

img_background = load_img("bg_Game.png")
player_ship = load_img("localShips.png", (80, 80)) #define o tamanho da imagem
enemy_ship = load_img("enemyShips.png", (60, 60)) #define o tamanho da imagem
shots = load_img("spaceMissil.png")
img_menu = load_img("bg_Menu.jpg")

#Opções do menu
MENU_OPTION = ["Start Game", "Sound", "Exit"]
#Config som menu
sound_on = True

def toggle_sound():
    global sound_on
    sound_on = not sound_on
    if sound_on:
        pygame.mixer_music.play(-1)
    else:
        pygame.mixer_music.stop()
