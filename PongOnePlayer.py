from Pong import *

def AI():
    if ball_pos[1] < Pong.paddle2_pos[1]:
        while ball_pos[1] != Pong.paddle2_pos[1]:
            Pong.paddle2_pos[1] += 3
    elif ball_pos[1] < Pong.paddle2_pos[1]:
        while ball_pos[1] != Pong.paddle2_pos[1]:
            Pong.paddle2_pos[1] += 3