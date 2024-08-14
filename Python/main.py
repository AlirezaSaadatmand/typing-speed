import pygame
from sys import exit
import random
import pyautogui

from words import words

WIDTH , HEIGHT =  1300 , 650
FPS = 60

# Letter that should be typed
letter = ""

speed = 0
all_letters = 0
right_letters = 0
wrong_letters = 0


def get_words():
    word_lst = []
    lst = []
    for _ in range(10):
        word = random.choice(words)
        word_lst.append(word)
        text = pygame.font.Font(None , 30)
        text = text.render("word" , True , "white")
        lst.append(text)
    return lst , word_lst


pygame.init()
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
    
    screen.blit(main_surface , main_surface_rect)
    
    pygame.display.update()
    clock.tick(FPS)
