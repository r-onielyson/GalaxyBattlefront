import pygame
from config import MENU_OPTION, window, toggle_sound, img_menu

#Loop musica do menu
pygame.mixer_music.load("assets/sounds/sound_menu.mp3")
pygame.mixer_music.play(-1)

#Função do menu
def draw_menu(menu_option, font_title, font_option, font_demo):

    window.blit(img_menu, (0, 0)) #Carrega a imagem de fundo do menu

    title = font_title.render("Galaxy Battlefront", True, (255, 165, 0)) #Titulo do Menu
    window.blit(title, (window.get_width() / 2 - title.get_width() / 2, 100))

    #Define fontes, tamanho e cores usados no menu
    for i, option in enumerate(MENU_OPTION):
        color = (255, 255, 0) if i == menu_option else (255, 255, 255)
        text = font_option.render(option, True, color)
        window.blit(text, (window.get_width() / 2 - text.get_width() / 2, 240 + 50 * i))

    demo_text = font_demo.render("Version: Demo", True, (255, 255, 255))
    window.blit(demo_text, (window.get_width() - demo_text.get_width() - 10, 10))

    pygame.display.flip()

#Menu Principal
def menu():

    menu_option = 0

    #Define fonte e tamanho dos textos exibidos no menu
    font_title = pygame.font.SysFont("Lucida Sans Typewriter", 50)
    font_option = pygame.font.SysFont("Lucida Sans Typewriter", 30)
    font_demo = pygame.font.SysFont("Lucida Sans Typewriter", 20)

    #Loop Menu
    while True:
        draw_menu(menu_option, font_title, font_option, font_demo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    menu_option = (menu_option + 1) % len(MENU_OPTION)
                elif event.key == pygame.K_UP:
                    menu_option = (menu_option - 1) % len(MENU_OPTION)
                elif event.key == pygame.K_RETURN:
                    selected_option = MENU_OPTION[menu_option]
                    if selected_option == "Start Game":
                        return "start"
                    elif selected_option == "Sound":
                        toggle_sound()
                    elif selected_option == "Exit":
                        return "exit"

