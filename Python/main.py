import pygame
from sys import exit
import random
import pyautogui

from words import words

for _ in range(10):
    print(random.choice(words))

size = pyautogui.size()
WIDTH , HEIGHT =  size
FPS = 60

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
