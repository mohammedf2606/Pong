import pygame
import time
from Colour import *

background_colour = colour.Gray
width = 600
height = 400
buttonWidth = 200
buttonHeight = 75
pygame.font.init()

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
screen.fill(background_colour)

pixelFont = pygame.font.SysFont("Minecraft", 144)
font = pygame.font.Font(None, 144)

text = pixelFont.render("Pong", True, colour.DarkOliveGreen)
start = pixelFont.render("Pong", True, colour.DarkOliveGreen)

def text_objects(text, font):
    textSurface = font.render(text, True, colour.Black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("Minecraft",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def floatText(text, colour, font):
    pixelFont = pygame.font.SysFont("Minecraft", font)
    printText = pixelFont.render(text, True, colour)
    return printText

running = True
startScreen = True
gameScreen = False
pauseScreen = False
endScreen = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            startScreen = False

        screen.fill(background_colour)

        while startScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    startScreen = False
                    running = False

                pygame.draw.rect(screen, colour.Gray, (width, height, 0, 0))
                text = floatText("Pong", colour.DarkOliveGreen, 144)
                screen.blit(text, ((width // 2) - text.get_width() // 2, (height // 4) - text.get_height() // 2))

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                pvetext = floatText("PvE", colour.Gray, 72)
                pvptext = floatText("PvP", colour.Gray, 72)

                if (width // 2) - (buttonWidth // 2) < mouse[0] < (width // 2) + (buttonWidth // 2) and (height - (2.65 * buttonHeight)) < mouse[1] < (height - (1.65 * buttonHeight)):
                    pygame.draw.rect(screen, colour.Red, (
                        (width // 2) - (buttonWidth // 2), (height - (2.75 * buttonHeight)), buttonWidth, buttonHeight))
                    screen.blit(pvetext, ((width // 2) - (pvetext.get_width() // 2), (height - (2.65 * buttonHeight))))

                    if click[0] == 1:
                        startScreen = False
                        gameScreen = True

                else:
                    pygame.draw.rect(screen, colour.DarkRed, (
                        (width // 2) - (buttonWidth // 2), (height - (2.75 * buttonHeight)), buttonWidth, buttonHeight))
                    text = floatText("PvE", colour.Gray, 72)
                    screen.blit(pvetext, ((width // 2) - (pvetext.get_width() // 2), (height - (2.65 * buttonHeight))))

                if (width // 2) - (buttonWidth // 2) < mouse[0] < (width // 2) + (buttonWidth // 2) and (height - (1.4 * buttonHeight)) < mouse[1] < (height - (0.4 * buttonHeight)):
                    pygame.draw.rect(screen, colour.Red, (
                        (width // 2) - (buttonWidth // 2), (height - (1.5 * buttonHeight)), buttonWidth, buttonHeight))
                    screen.blit(pvptext, ((width // 2) - (pvptext.get_width() // 2), (height - (1.4 * buttonHeight))))

                    if click[0] == 1:
                        startScreen = False
                        gameScreen = True

                else:
                    pygame.draw.rect(screen, colour.DarkRed, (
                        (width // 2) - (buttonWidth // 2), (height - (1.5 * buttonHeight)), buttonWidth, buttonHeight))
                    text = floatText("PvP", colour.Gray, 72)
                    screen.blit(pvptext, ((width // 2) - (pvptext.get_width() // 2), (height - (1.4 * buttonHeight))))

                pygame.display.update()
        
        while gameScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameScreen = False
                    running = False

                if event.type == pygame.KEYDOWN

                screen.fill(background_colour)

                pygame.display.update()

        while pauseScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pauseScreen = False
                    running = False
                screen.fill(background_colour)