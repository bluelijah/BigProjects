import random #for random
import os #for clearing screen
import pygame
import random
pygame.init()

screen_width = 1400
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Rock Paper Scissors')

bg_size = (1400, 900)
bg = pygame.image.load("rpsBG.jpeg")
img = pygame.transform.scale(img, bg_size)




