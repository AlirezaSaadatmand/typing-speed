import pygame
from sys import exit
import random
import time

from words import words

pygame.init()

WIDTH, HEIGHT = 1200, 600
FPS = 60

typed_string = ""

finished = False

start_time = 0
end_time = 0

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
    string_text = pygame.font.Font(None, 35)
    string_text = string_text.render(string, True, "white")
    string_text_rect = string_text.get_rect(topleft=(250, HEIGHT / 2 - 50))

    return string, [string_text, string_text_rect]


string, string_rect = get_words()
letter = string[0]

typed_font = pygame.font.Font(None, 35)


def check_speed():

    global start_time, end_time, speed

    if not finished:

        speed = round((right_letters / 5) / ((time.time() - start_time) / 60))

        if start_time == 0 and typed_string:
            start_time = time.time()
        return


def draw(typed_font):
    screen.blit(main_surface, main_surface_rect)
    screen.blit(speed_surface, speed_surface_rect)
    screen.blit(string_rect[0], string_rect[1])

    speed_font = pygame.font.Font(None, 35)
    speed_font = speed_font.render(str(speed), True, "white")
    speed_font_rect = speed_font.get_rect(
        center=(WIDTH / 2 + 400, HEIGHT / 2 + 100))

    screen.blit(speed_font, speed_font_rect)

    typed_font = typed_font.render(typed_string, True, "green")
    typed_font_rect = typed_font.get_rect(topleft=(250, HEIGHT / 2 - 50))

    screen.blit(typed_font, typed_font_rect)

    for mis in mistakes:
        screen.blit(mis[0], mis[1])


screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

main_surface = pygame.Surface((900, 180))
main_surface.fill((25, 25, 25))
main_surface_rect = main_surface.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 50))


speed_surface = pygame.Surface((100, 50))
speed_surface.fill((25, 25, 25))
speed_surface_rect = speed_surface.get_rect(
    center=(WIDTH / 2 + 400, HEIGHT / 2 + 100))

result_surface = pygame.Surface((780, 150))
result_surface.fill((25, 25, 25))
result_surface_rect = result_surface.get_rect(
    topleft=(WIDTH / 2 - 450, HEIGHT / 2 + 75))


while True:
    screen.fill((17, 17, 17))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and not finished:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_BACKSPACE:
                if mistakes:
                    mistakes = mistakes[:-1]
                elif typed_string:
                    typed_string = typed_string[:-1]
                    letter = string[len(typed_string)]

            else:
                all_letters += 1
                if letter == event.unicode:
                    right_letters += 1
                    typed_string += event.unicode
                    letter = string[len(typed_string)]
                else:
                    wrong_letters += 1
                    mis1 = pygame.font.Font(None, 35)
                    mis = mis1.render(
                        string[len(typed_string) + len(mistakes)], True, "red")
                    distance = pygame.font.Font.size(
                        typed_font, string[:len(typed_string)])[0]

                    for i in range(len(mistakes)):
                        distance += pygame.font.Font.size(
                            mistakes[i][3], string[len(typed_string) + i])[0]

                    mis_rect = mis.get_rect(
                        topleft=(250 + distance, HEIGHT / 2 - 50))
                    mistakes.append([mis, mis_rect, event.unicode, mis1])
                    letter = string[len(typed_string) + len(mistakes)]

    if typed_string == string[:-1]:
        finished = True

    if finished:
        screen.blit(result_surface, result_surface_rect)

        big_speed_text = pygame.font.Font(None, 70)
        big_speed_text = big_speed_text.render(str(speed), True, "white")
        big_speed_text_rect = big_speed_text.get_rect(
            center=(WIDTH / 2 - 375, HEIGHT / 2 + 150)
        )
        screen.blit(big_speed_text, big_speed_text_rect)
        if not end_time:
            end_time = time.time()
            end_time = round(end_time - start_time)

        time_result = pygame.font.Font(None, 25)
        time_result = time_result.render(f"Time : {end_time}", True, "white")
        time_result_rect = time_result.get_rect(
            center=(WIDTH / 2 - 225, HEIGHT / 2 + 150))

        screen.blit(time_result, time_result_rect)
    else:
        draw(typed_font)
        check_speed()
    pygame.display.update()
    clock.tick(FPS)
