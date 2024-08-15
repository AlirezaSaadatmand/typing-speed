import pygame
from sys import exit
import random

from words import words

pygame.init()

WIDTH , HEIGHT =  1200 , 600
FPS = 60

# Letter that should be typed
letter = ""

# list of words
first_line_string = ""
second_line_string = ""

typed_string = "|"

# list of the pygame font
first_line_lst = []


speed = 0
all_letters = 0
right_letters = 0
wrong_letters = 0

def get_words():
    string = ""
    # for _ in range(10):
    #     word = random.choice(words)
    #     string += word + " "
    while len(string) < 50:
        word = random.choice(words)
        string += word + " "
    string_text = pygame.font.Font(None , 35)
    string_text = string_text.render(string , True , "white")
    string_text_rect = string_text.get_rect(topleft = (250 , HEIGHT / 2))
    
    return string[:-1] , [string_text , string_text_rect]

string , string_rect = get_words()

def draw():
    screen.blit(main_surface , main_surface_rect)
    screen.blit(string_rect[0] , string_rect[1])
    
    typed_font = pygame.font.Font(None , 35)
    typed_font = typed_font.render(typed_string , True, "green")
    typed_font_rect = typed_font.get_rect(topleft = (250 , HEIGHT / 2))
    
    screen.blit(typed_font , typed_font_rect)


screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
screen.fill((17 , 17 , 17))
clock =  pygame.time.Clock()

main_surface = pygame.Surface( (900 , 180) )
main_surface.fill((25 , 25 , 25))
main_surface_rect = main_surface.get_rect(center = (WIDTH / 2 , HEIGHT / 2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_BACKSPACE:
                typed_string = typed_string[:-2] + "|"
            else:
                typed_string = typed_string[:-1]+ event.unicode + "|"
    print(typed_string)
    
    draw()
    pygame.display.update()
    clock.tick(FPS)

