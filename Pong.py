import random
import pygame, sys
from pygame.locals import *
from Color import *

pygame.init()
fps = pygame.time.Clock()

# globals
WIDTH = 600
HEIGHT = 400
ballRadius = 10
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0

# canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Pong')


# helper function that spawns a ball, returns a position vector and a velocity vector
# if right is True, spawn to the right, else spawn to the left
def ball_init(right):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH // 2, HEIGHT // 2]
    horz = 4
    vert = random.choice([-3, 3])

    if right == False:
        horz = - horz

    ball_vel = [horz, -vert]


# define event handlers
def init():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, l_score, r_score  # these are floats
    global score1, score2  # these are ints
    paddle1_pos = [HALF_PAD_WIDTH - 1, HEIGHT // 2]
    paddle2_pos = [WIDTH + 1 - HALF_PAD_WIDTH, HEIGHT // 2]
    l_score = 0
    r_score = 0
    if random.randrange(0, 2) == 0:
        ball_init(True)
    else:
        ball_init(False)


# draw function of canvas
def draw(canvas):
    global paddle1_pos, paddle2_pos, ball_pos, ball_vel, l_score, r_score

    canvas.fill(Color.Gray)
    pygame.draw.line(canvas, Color.White, [WIDTH // 2, 0], [WIDTH // 2, HEIGHT], 1)
    pygame.draw.line(canvas, Color.White, [PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1)
    pygame.draw.line(canvas, Color.White, [WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1)
    pygame.draw.circle(canvas, Color.White, [WIDTH // 2, HEIGHT // 2], 70, 1)

    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] > HALF_PAD_HEIGHT and paddle1_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HALF_PAD_HEIGHT and paddle1_vel > 0:
        paddle1_pos[1] += paddle1_vel
    elif paddle1_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle1_vel < 0:
        paddle1_pos[1] += paddle1_vel

    if paddle2_pos[1] > HALF_PAD_HEIGHT and paddle2_pos[1] < HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HALF_PAD_HEIGHT and paddle2_vel > 0:
        paddle2_pos[1] += paddle2_vel
    elif paddle2_pos[1] == HEIGHT - HALF_PAD_HEIGHT and paddle2_vel < 0:
        paddle2_pos[1] += paddle2_vel

    # update ball
    ball_pos[0] += int(ball_vel[0])
    ball_pos[1] += int(ball_vel[1])

    # draw paddles and ball
    pygame.draw.circle(canvas, Color.White, ball_pos, ballRadius, 0)
    pygame.draw.polygon(canvas, Color.White , [[paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT],
                                        [paddle1_pos[0] - HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle1_pos[0] + HALF_PAD_WIDTH, paddle1_pos[1] - HALF_PAD_HEIGHT]], 0)
    pygame.draw.polygon(canvas, Color.White, [[paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT],
                                        [paddle2_pos[0] - HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] + HALF_PAD_HEIGHT],
                                        [paddle2_pos[0] + HALF_PAD_WIDTH, paddle2_pos[1] - HALF_PAD_HEIGHT]], 0)

    # ball collision check on top and bottom walls
    if int(ball_pos[1]) <= ballRadius:
        ball_vel[1] = - ball_vel[1]
    if int(ball_pos[1]) >= HEIGHT + 1 - ballRadius:
        ball_vel[1] = -ball_vel[1]

    # ball collison check on gutters or paddles
    if int(ball_pos[0]) <= ballRadius + PAD_WIDTH and int(ball_pos[1]) in range(paddle1_pos[1] - HALF_PAD_HEIGHT,
                                                                                 paddle1_pos[1] + HALF_PAD_HEIGHT, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.05
        ball_vel[1] *= 1.05
    elif int(ball_pos[0]) <= 0:
        r_score += 1
        pygame.time.wait(1500)
        ball_init(True)

    if int(ball_pos[0]) >= WIDTH + 1 - ballRadius - PAD_WIDTH and int(ball_pos[1]) in range(
            paddle2_pos[1] - HALF_PAD_HEIGHT, paddle2_pos[1] + HALF_PAD_HEIGHT, 1):
        ball_vel[0] = -ball_vel[0]
        ball_vel[0] *= 1.05
        ball_vel[1] *= 1.05
    elif int(ball_pos[0]) >= WIDTH:
        l_score += 1
        pygame.time.wait(1500)
        ball_init(False)

    # update scores
    myfont1 = pygame.font.SysFont("Comic Sans MS", 36)
    label1 = myfont1.render(str(l_score), True, (255, 255, 0))
    label1_rect = label1.get_rect()
    label1_rect.left = (WIDTH // 2) - 40
    canvas.blit(label1, label1_rect)

    myfont2 = pygame.font.SysFont("Comic Sans MS", 36)
    label2 = myfont2.render(str(r_score), True, (255, 255, 0))
    label2_rect = label2.get_rect()
    label2_rect.right = (WIDTH // 2) + 40
    canvas.blit(label2, label2_rect)


# keydown handler
def keydown(event):
    global paddle1_vel, paddle2_vel

    if event.key == K_UP:
        paddle2_vel = -8
    elif event.key == K_DOWN:
        paddle2_vel = 8
    elif event.key == K_w:
        paddle1_vel = -8
    elif event.key == K_s:
        paddle1_vel = 8


# keyup handler
def keyup(event):
    global paddle1_vel, paddle2_vel

    if event.key in (K_w, K_s):
        paddle1_vel = 0
    elif event.key in (K_UP, K_DOWN):
        paddle2_vel = 0


init()

# game loop
while True:

    draw(window)

    for event in pygame.event.get():

        if event.type == KEYDOWN:
            keydown(event)
        elif event.type == KEYUP:
            keyup(event)
        elif event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)
