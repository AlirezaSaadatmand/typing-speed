import pygame
from sys import exit
import random
import pyautogui

from words import words

WIDTH , HEIGHT =  1200 , 600
FPS = 60

speed = 0
all_letters = 0
right_letters = 0
wrong_letters = 0


def get_words():
    string = ""
    lst = []
    for _ in range(10):
        word = random.choice(words)
        string += word + " "
        text = pygame.font.Font(None , 30)
        text = text.render("word" , True , "white")
        lst.append(text)
    return lst , string[:-1]


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock =  pygame.time.Clock()



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
    

    
    pygame.display.update()
    clock.tick(FPS)
