import pygame
from sys import exit
import random

from words import words

pygame.init()

WIDTH , HEIGHT =  1200 , 600
FPS = 60

typed_string = "|"

# list of the pygame font
first_line_lst = []

# mistakes 
mistakes = []

speed = 0
all_letters = 0
right_letters = 0
wrong_letters = 0

def get_words():
    string = ""
    while len(string) < 50:
        word = random.choice(words)
        string += word + " "
    string_text = pygame.font.Font(None , 35)
    string_text = string_text.render(string , True , "white")
    string_text_rect = string_text.get_rect(topleft = (250 , HEIGHT / 2))
    
    return string[:-1] , [string_text , string_text_rect]

string , string_rect = get_words()

typed_font = pygame.font.Font(None , 35)

def draw(typed_font):
    screen.blit(main_surface , main_surface_rect)
    screen.blit(string_rect[0] , string_rect[1])
    
    typed_font = typed_font.render(typed_string , True, "green")
    typed_font_rect = typed_font.get_rect(topleft = (250 , HEIGHT / 2))
    
    screen.blit(typed_font , typed_font_rect)
    
    for mis in mistakes:
        screen.blit(mis[0] , mis[1])


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
                if string[len(typed_string) - 1] == event.unicode:
                    typed_string = typed_string[:-1] + event.unicode + "|"
                else:
                    typed_string = typed_string[:-1] + "|"
                    mis = pygame.font.Font(None , 35)
                    mis = mis.render(string[len(typed_string) - 2] , True , "red")
                    if not mistakes:
                        distance = pygame.font.Font.size(typed_font , typed_string)[0] - 14
                    else:
                        distance = pygame.font.Font.size(typed_font , typed_string)[0] - 14 
                    mis_rect = mis.get_rect(topleft = (250 + distance , HEIGHT / 2))
                    mistakes.append([mis , mis_rect , len(typed_string) - 1])

    
    draw(typed_font)
    pygame.display.update()
    clock.tick(FPS)