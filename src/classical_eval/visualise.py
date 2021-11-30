import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from util import *
import numpy as np
from minimax import *
import pygame as p
import sys
WHITE = (255, 255, 255)
Dimension = 6
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
Log_width = 600
COLUMN_COUNT = 6
ROW_COUNT = 6
running = True
pieces = ["green", "red"]
Square_size = 150
width = COLUMN_COUNT * Square_size
height = (ROW_COUNT+1) * Square_size
size = (width, height)
RADIUS = int(Square_size/2 - 5)

player_score = 0
alpha_score = 0

# global running, screen
# game.current_player = 'H'
p.init()
myfont = p.font.SysFont("monospace", 75)
mediumfont = p.font.SysFont("monospace", 35)
labelfont = p.font.SysFont("monospace", 20)
screen = p.display.set_mode(size)
p.display.set_caption("Connect 4")
p.display.update()
path_chosen = ""


class GamePlay():
    def __init__(self) -> None:
        self.state = 'intro'
        self.player = 1

    def intro(self):
        global game
        global board
        board = np.zeros((6, 6))

        # print("reached")
        screen.fill((0, 0, 0))

        label = myfont.render("Welcome to the game", 1, RED)
        running = True
        while(running):
            screen.blit(label, (40, 10))
            p.display.flip()

            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                    sys.exit()
                mouse = p.mouse.get_pos()
                if e.type == p.MOUSEBUTTONDOWN:

                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        self.player = 1
                        self.state = 'level'
                        running = False
                        return
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        self.player = -1
                        self.state = 'level'
                        running = False
                        return
            screen.blit(mediumfont.render(
                "Choose to go first or second", 1, RED), (125, 300))
            screen.blit(labelfont.render("First", 1, RED), (170, 400))
            p.draw.rect(screen, RED, (150, 450, 100, 50))
            screen.blit(labelfont.render("Second", 1, BLUE), (560, 400))
            p.draw.rect(screen, BLUE, (550, 450, 100, 50))
            p.display.update()

    def main_play(self):
        running = True
        global player_score
        global alpha_score
        screen.fill((0, 0, 0))
        while running:
            val_moves = get_valid_moves(board)
            for e in p.event.get():

                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN and self.player == 1:
                    pos = p.mouse.get_pos()
                    move = ((pos[1]//Square_size)-1, (pos[0]//Square_size))
                    check = True
                    self.player *= -1

                    while check:
                        if move in val_moves:
                            # print("Enter valid move")
                            gameover, winner = make_move(board, move, 1)
                            # print(board)
                            check = False
                            # print(move)
                        if gameover:
                            if winner == None:
                                alpha_score += 0.5
                                player_score += 0.5
                                label = myfont.render(
                                    "Draw", 1, RED)
                            elif winner == -1:
                                label = myfont.render(
                                    "Alpha wins", 1, RED)
                            else:
                                player_score += 1

                                label = myfont.render(
                                    "You win", 1, RED)
                            running = False
                elif self.player == -1:

                    move = minimax_util(board, -1, depth_chosen)
                    gameover, winner = make_move(board, (move[0], move[1]), -1)
                    self.player *= -1
                    if gameover:
                        if winner == None:
                            label = mediumfont.render(
                                "Draw", 1, RED)
                            alpha_score += 0.5
                            player_score += 0.5

                        elif winner == -1:
                            alpha_score += 1
                            label = myfont.render("Alpha wins", 1, RED)
                        else:
                            player_score += 1
                            label = mediumfont.render(
                                "You win", 1, RED)
                        running = False
            piecedisplay(screen, board)
            p.display.flip()

            if running == False:
                screen.blit(label, (250, 10))
                p.display.flip()
                p.time.wait(4000)
                self.state = 'exit_screen'
                return

    def level(self):
        screen.fill((0, 0, 0))
        running = True
        global depth_chosen
        while(running):

            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                mouse = p.mouse.get_pos()
                if e.type == p.MOUSEBUTTONDOWN:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        depth_chosen = 1
                        self.state = 'main_play'
                        return
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        depth_chosen = 2
                        self.state = 'main_play'
                        return
                    elif 150+100 > mouse[0] > 150 and 650+50 > mouse[1] > 650:
                        depth_chosen = 3
                        self.state = 'main_play'
                        return
                    elif 550+100 > mouse[0] > 550 and 650+50 > mouse[1] > 650:
                        depth_chosen = 4
                        self.state = 'main_play'
                        return
            screen.blit(labelfont.render("Depth 1", 1, RED), (155, 400)
                        )
            p.draw.rect(screen, RED, (150, 450, 100, 50))
            screen.blit(labelfont.render("Depth 2", 1, BLUE), (555, 400))
            p.draw.rect(
                screen, BLUE, (550, 450, 100, 50))
            screen.blit(labelfont.render("Depth 3", 1, GREEN), (155, 600))
            p.draw.rect(
                screen, GREEN, (150, 650, 100, 50))
            screen.blit(labelfont.render("Depth 4", 1, WHITE), (555, 600))
            p.draw.rect(
                screen, WHITE, (550, 650, 100, 50))
            screen.blit(labelfont.render(
                "Note that Depth 4 might take a lot of time", 1, RED), (150, 800))
            p.display.update()

    def exit_screen(self):
        screen.fill((0, 0, 0))
        global player_score
        global alpha_score
        label_player_score = labelfont.render(str(player_score), 1, RED)
        label_alpha_score = labelfont.render(str(alpha_score), 1, RED)
        while True:
            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                mouse = p.mouse.get_pos()

                if e.type == p.MOUSEBUTTONDOWN:
                    if 250+100 > mouse[0] > 250 and 750+50 > mouse[1] > 750:
                        self.state = 'intro'
                        return
                    elif 525+100 > mouse[0] > 525 and 750+50 > mouse[1] > 750:
                        sys.exit()
            screen.blit(myfont.render("Game Score", 1, RED), (240, 80))
            screen.blit(labelfont.render("Alpha_zero", 1, RED), (300, 360))
            screen.blit(labelfont.render("You", 1, RED), (535, 360))

            screen.blit(label_alpha_score, (350, 400))
            screen.blit(label_player_score, (550, 400))
            screen.blit(labelfont.render(
                "Press to play again", 1, GREEN), (200, 700))
            screen.blit(labelfont.render("QUIT", 1, RED), (550, 700))
            p.draw.rect(screen, GREEN, (250, 750, 100, 50))
            p.draw.rect(screen, RED, (525, 750, 100, 50))
            p.display.update()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_play':
            self.main_play()
        if self.state == 'level':
            self.level()
        if self.state == 'exit_screen':
            self.exit_screen()


def piecedisplay(screen, board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            p.draw.rect(screen, BLUE, (c*Square_size, r *
                        Square_size+Square_size, Square_size, Square_size))
            p.draw.circle(screen, BLACK, (int(c*Square_size+Square_size/2),
                          int(r*Square_size+Square_size+Square_size/2)), RADIUS)

    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == -1:
                p.draw.circle(screen, RED, (int(
                    (c)*Square_size+Square_size/2), int((r+1)*Square_size+Square_size/2)), RADIUS)
            elif board[r][c] == 1:
                p.draw.circle(screen, GREEN, (int(
                    (c)*Square_size+Square_size/2), int((r+1)*Square_size+Square_size/2)), RADIUS)


def main():
    game_play = GamePlay()
    while(True):
        game_play.state_manager()


if __name__ == '__main__':
    main()
