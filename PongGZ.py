import pygame
import sys
from pygame.locals import *
import time
from Colour import *

pygame.init()
fps = pygame.time.Clock()

background_Colour = Colour.Mist
width = 1920
height = 1080
buttonwidth = 200
buttonheight = 75
ballRadius = 10
PAD_width = 8
PAD_height = 160
HALF_PAD_width = PAD_width // 2
HALF_PAD_height = PAD_height // 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0
limit = 5

running = True
menuScreen = True
gameScreen = False
pauseScreen = False
endScreen = False

PvP = True

pygame.font.init()

screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption('Pong')
screen.fill(background_Colour)

pixelFont = pygame.font.SysFont("Minecraft", 144)
font = pygame.font.Font(None, 144)

text = pixelFont.render("Pong", True, Colour.DarkOliveGreen)
start = pixelFont.render("Pong", True, Colour.DarkOliveGreen)

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

def ball_init(right):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [width // 2, height // 2]
    horz = 6
    vert = random.choice([-3, 3])

    if right == False:
        horz = - horz

    ball_vel = [horz, -vert]

# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, l_score, r_score  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_width - 1, height // 2]
    paddle2_pos = [width + 1 - HALF_PAD_width, height // 2]
    l_score = 0
    r_score = 0
    if random.randrange(0, 2) == 0:
        ball_init(True)
    else:
        ball_init(False)

# draw function of canvas
def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score

    canvas.fill(Colour.Gray)
    pygame.draw.line(canvas, Colour.White, [width // 2, 0], [width // 2, height], 1)
    pygame.draw.line(canvas, Colour.White, [PAD_width, 0], [PAD_width, height], 1)
    pygame.draw.line(canvas, Colour.White, [width - PAD_width, 0], [width - PAD_width, height], 1)

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] > HALF_PAD_height and paddle1_pos[1] < height - HALF_PAD_height:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HALF_PAD_height and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == height - HALF_PAD_height and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel

    if paddle2_pos[1] > HALF_PAD_height and paddle2_pos[1] < height - HALF_PAD_height:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_height and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == height - HALF_PAD_height and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel

    # update ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    # draw paddles and ball
    pygame.draw.circle(canvas, Colour.White, ball_pos, ballRadius, 0)
    pygame.draw.polygon(canvas, Colour.White , [[paddle1_pos[0] - HALF_PAD_width, paddle1_pos[1] - HALF_PAD_height],
                                        [paddle1_pos[0] - HALF_PAD_width, paddle1_pos[1] + HALF_PAD_height],
                                        [paddle1_pos[0] + HALF_PAD_width, paddle1_pos[1] + HALF_PAD_height],
                                        [paddle1_pos[0] + HALF_PAD_width, paddle1_pos[1] - HALF_PAD_height]], 0)
    pygame.draw.polygon(canvas, Colour.White, [[paddle2_pos[0] - HALF_PAD_width, paddle2_pos[1] - HALF_PAD_height],
                                        [paddle2_pos[0] - HALF_PAD_width, paddle2_pos[1] + HALF_PAD_height],
                                        [paddle2_pos[0] + HALF_PAD_width, paddle2_pos[1] + HALF_PAD_height],
                                        [paddle2_pos[0] + HALF_PAD_width, paddle2_pos[1] - HALF_PAD_height]], 0)

    # ball collision check on top and bottom walls
    if int(ball_pos[1]) <= ballRadius:
        ball_vel[1] = - ball_vel[1]
    if int(ball_pos[1]) >= height + 1 - ballRadius:
        ball_vel[1] = -ball_vel[1]

    # ball collison check on gutters or paddles
    if int(ball_pos[0]) <= ballRadius + PAD_width and int(ball_pos[1]) in range(paddle1_pos[1] - (HALF_PAD_height+15),
                                                                                 paddle1_pos[1] + (HALF_PAD_height+15), 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.04
        ball_vel[1] = 1.04*ball_vel[1] + paddle1_vel*0.25
    elif int(ball_pos[0]) <= 0:
        r_score += 1
        pygame.time.wait(1200)
        ball_init(True)

    if int(ball_pos[0]) >= width + 1 - ballRadius - PAD_width and int(ball_pos[1]) in range(
            paddle2_pos[1] - (HALF_PAD_height+15), paddle2_pos[1] + (HALF_PAD_height+15), 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.04
        ball_vel[1] = 1.04*ball_vel[1] + paddle2_vel*0.25
    elif int(ball_pos[0]) >= width:
        l_score += 1
        pygame.time.wait(1200)
        ball_init(False)

    # update scores
    myfont1 = pygame.font.SysFont("Minecraft", 56)
    label1 = myfont1.render(str(l_score), True, Colour.White)
    label1_rect = label1.get_rect()
    label1_rect.left = (width // 2) - 50
    canvas.blit(label1, label1_rect)

    myfont2 = pygame.font.SysFont("Minecraft", 56)
    label2 = myfont2.render(str(r_score), True, Colour.White)
    label2_rect = label2.get_rect()
    label2_rect.right = (width // 2) + 50
    canvas.blit(label2, label2_rect)

# keydown handler
def keydown(event):
    global paddle1_vel, paddle2_vel, gameScreen, pauseScreen

    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8
    elif event.key == K_SPACE:
        gameScreen = False
        pauseScreen = True


# keyup handler
def keyup(event):
    global paddle1_vel, paddle2_vel

    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0

init()

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

                pygame.draw.rect(screen, Colour.Mist, (width, height, 0, 0))
                text = floatText("Pong", Colour.Chartreuse, 144)
                screen.blit(text, ((width // 2) - text.get_width() // 2, (height // 4) - text.get_height() // 2))

                mouse = pygame.mouse.get_pos()
                click = pygame.mouse.get_pressed()

                pvetext = floatText("PvE", Colour.Mist, 72)
                pvptext = floatText("PvP", Colour.Mist, 72)

                #PvE Button
                if (width // 2) - (buttonwidth // 2) < mouse[0] < (width // 2) + (buttonwidth // 2) and (height - (2.65 * buttonheight)) < mouse[1] < (height - (1.65 * buttonheight)):
                    pygame.draw.rect(screen, Colour.Red, (
                        (width // 2) - (buttonwidth // 2), (height - (2.75 * buttonheight)), buttonwidth, buttonheight))
                    screen.blit(pvetext, ((width // 2) - (pvetext.get_width() // 2), (height - (2.65 * buttonheight))))

                    if click[0] == 1:
                        menuScreen = False
                        gameScreen = True
                        PvP = False

                else:
                    pygame.draw.rect(screen, Colour.DarkRed, (
                        (width // 2) - (buttonwidth // 2), (height - (2.75 * buttonheight)), buttonwidth, buttonheight))
                    text = floatText("PvE", Colour.Black, 72)
                    screen.blit(pvetext, ((width // 2) - (pvetext.get_width() // 2), (height - (2.65 * buttonheight))))

                #PvP Button
                if (width // 2) - (buttonwidth // 2) < mouse[0] < (width // 2) + (buttonwidth // 2) and (height - (1.4 * buttonheight)) < mouse[1] < (height - (0.4 * buttonheight)):
                    pygame.draw.rect(screen, Colour.Red, (
                        (width // 2) - (buttonwidth // 2), (height - (1.5 * buttonheight)), buttonwidth, buttonheight))
                    screen.blit(pvptext, ((width // 2) - (pvptext.get_width() // 2), (height - (1.4 * buttonheight))))

                    if click[0] == 1:
                        menuScreen = False
                        gameScreen = True

                else:
                    pygame.draw.rect(screen, Colour.DarkRed, (
                        (width // 2) - (buttonwidth // 2), (height - (1.5 * buttonheight)), buttonwidth, buttonheight))
                    text = floatText("PvP", Colour.Black, 72)
                    screen.blit(pvptext, ((width // 2) - (pvptext.get_width() // 2), (height - (1.4 * buttonheight))))

                pygame.display.update()
        
        while gameScreen:

            draw(screen)

            if PvP:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameScreen = False
                        running = False

                    if event.type == pygame.KEYDOWN:
                        keydown(event)

                    if event.type == KEYUP:
                        keyup(event)

                if l_score == limit or r_score == limit:
                    gameScreen = False
                    endScreen = True

                pygame.display.update()
                fps.tick(60)

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
                        l_score = 0
                        r_score = 0

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
