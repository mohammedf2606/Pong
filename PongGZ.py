import pygame
import time
from Colour import *

background_Colour = Colour.Gray
width = 600
height = 400
buttonWidth = 200
buttonHeight = 75
pygame.font.init()

screen = pygame.display.set_mode((width, height), 0)
pygame.display.set_caption('Pong')
screen.fill(background_Colour)

pixelFont = pygame.font.SysFont("Minecraft", 144)
font = pygame.font.Font(None, 144)

text = pixelFont.render("Pong", True, Colour.DarkOliveGreen)
start = pixelFont.render("Pong", True, Colour.DarkOliveGreen)

l_score = 0
r_score = 0
limit = 5

def text_objects(text, font):
    textSurface = font.render(text, True, Colour.Black)
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

def floatText(text, Colour, font):
    pixelFont = pygame.font.SysFont("Minecraft", font)
    printText = pixelFont.render(text, True, Colour)
    return printText

running = True
menuScreen = True
gameScreen = False
pauseScreen = False
endScreen = False

PvP = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menuScreen = False

        screen.fill(background_Colour)

        while menuScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menuScreen = False
                    running = False

                pygame.draw.rect(screen, Colour.Gray, (width, height, 0, 0))
                text = floatText("Pong", Colour.DarkOliveGreen, 144)
                screen.blit(text, ((width // 2) - text.get_width() // 2, (height // 4) - text.get_height() // 2))

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                pvetext = floatText("PvE", Colour.Gray, 72)
                pvptext = floatText("PvP", Colour.Gray, 72)

                #PvE Button
                if (width // 2) - (buttonWidth // 2) < mouse[0] < (width // 2) + (buttonWidth // 2) and (height - (2.65 * buttonHeight)) < mouse[1] < (height - (1.65 * buttonHeight)):
                    pygame.draw.rect(screen, Colour.Red, (
                        (width // 2) - (buttonWidth // 2), (height - (2.75 * buttonHeight)), buttonWidth, buttonHeight))
                    screen.blit(pvetext, ((width // 2) - (pvetext.get_width() // 2), (height - (2.65 * buttonHeight))))

                    if click[0] == 1:
                        menuScreen = False
                        gameScreen = True
                        PvP = False

                else:
                    pygame.draw.rect(screen, Colour.DarkRed, (
                        (width // 2) - (buttonWidth // 2), (height - (2.75 * buttonHeight)), buttonWidth, buttonHeight))
                    text = floatText("PvE", Colour.Gray, 72)
                    screen.blit(pvetext, ((width // 2) - (pvetext.get_width() // 2), (height - (2.65 * buttonHeight))))

                #PvP Button
                if (width // 2) - (buttonWidth // 2) < mouse[0] < (width // 2) + (buttonWidth // 2) and (height - (1.4 * buttonHeight)) < mouse[1] < (height - (0.4 * buttonHeight)):
                    pygame.draw.rect(screen, Colour.Red, (
                        (width // 2) - (buttonWidth // 2), (height - (1.5 * buttonHeight)), buttonWidth, buttonHeight))
                    screen.blit(pvptext, ((width // 2) - (pvptext.get_width() // 2), (height - (1.4 * buttonHeight))))

                    if click[0] == 1:
                        menuScreen = False
                        gameScreen = True

                else:
                    pygame.draw.rect(screen, Colour.DarkRed, (
                        (width // 2) - (buttonWidth // 2), (height - (1.5 * buttonHeight)), buttonWidth, buttonHeight))
                    text = floatText("PvP", Colour.Gray, 72)
                    screen.blit(pvptext, ((width // 2) - (pvptext.get_width() // 2), (height - (1.4 * buttonHeight))))

                pygame.display.update()
        
        while gameScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameScreen = False
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameScreen = False
                        pauseScreen = True
                    if event.key == pygame.K_1:
                        gameScreen = False
                        endScreen = True

                if l_score == limit or r_score == 5:
                    gameScreen = False
                    endScreen = True

                screen.fill(background_Colour)

                pygame.display.update()

        while pauseScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pauseScreen = False
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameScreen = True
                        pauseScreen = False

                screen.fill(Colour.Mist)

                #Display "Pause"
                text = floatText("Game Paused", Colour.DimGray, 72)
                screen.blit(text, ((width // 2) - text.get_width() // 2, (height // 3) - (text.get_height() // 1.5)))

                #Display "Press SPACE to Resume"
                text1 = floatText("Press", Colour.SteelBlue, 48)
                screen.blit(text1, ((width // 2) - (text1.get_width() // 2), (height // 2) - (text1.get_height() // 2)))
                text2 = floatText("SPACE", Colour.Navy, 56)
                screen.blit(text2, ((width // 2) - (text2.get_width() // 2), (height // 2) + (text2.get_height() // 2)))
                text3 = floatText("to Resume", Colour.SteelBlue, 48)
                screen.blit(text3, ((width // 2) - (text3.get_width() // 2), (height // 2) + (text2.get_height() // 2) + (text3.get_height())))

                pygame.display.update()

        while endScreen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    endScreen = False
                    running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        menuScreen = True
                        endScreen = False

                screen.fill(Colour.Mist)

                # Display "Player 1 Win"
                if PvP and l_score == limit:
                    displayText = "Player 1 Wins"
                elif PvP and r_score == limit:
                    displayText = "Player 2 Wins"
                elif not PvP and l_score == limit:
                    displayText = "Player Wins"
                else:
                    displayText = "CPU Wins"


                text1 = floatText(displayText, Colour.Gold, 72)
                screen.blit(text1, ((width // 2) - text1.get_width() // 2, (height // 2) - (text1.get_height() // 2)))

                text2 = floatText("Press SPACE to Restart", Colour.Black, 24)
                screen.blit(text2, ((width // 2) - text2.get_width() // 2, (height // 3) + (text1.get_height() // 1) + (text2.get_height() // 0.75)))

                pygame.display.update()
