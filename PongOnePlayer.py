from Pong import *

def AI():
    if ball_pos[1] < Pong.paddle2_pos:
        while ball_pos[1] != Pong.paddle2_pos[1]:
            self.player2.center_y = self.player2.center_y - 3
    if ball_pos[1] > HALF_PAD_HEIGHT:
        while ball_pos[1] != HALF_PAD_HEIGHT:
            self.player2.center_y = self.player2.center_y + 3