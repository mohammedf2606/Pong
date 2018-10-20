import pygame
import time
from Color import *

background_colour = Color.Gray
width = 800
height = 450
buttonWidth = 200
buttonHeight = 75
pygame.font.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
screen.fill(background_colour)

pixelFont = pygame.font.SysFont("Minecraft", 144)
font = pygame.font.Font(None, 144)

text = pixelFont.render("Pong", True, Color.DarkOliveGreen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.draw.rect(screen, Color.Gray, (width, height, 0, 0))
        screen.blit(text, ((width // 2) - text.get_width() // 2, (height // 3) - text.get_height() // 2))
        pygame.draw.rect(screen, Color.Red, ((width // 2) - (buttonWidth // 2), (height - (height // 3)) - (buttonHeight), buttonWidth, buttonHeight))

        pygame.display.flip()

