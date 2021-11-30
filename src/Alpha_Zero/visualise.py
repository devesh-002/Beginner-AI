import numpy as np
from c4 import *
from Neural_network import *
from node_class import *
from mct import *
from utils import *
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
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
neural_network = AlphaNet(6, 6)
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


def initialise_neural_network(path="model/Level4.h5"):
    neural_network.build(input_shape=(1, 1, 6, 6))
    neural_network.load_weights(path)


class GamePlay():
    def __init__(self) -> None:
        self.state = 'intro'
        self.player = 'A'

    def intro(self):
        global game
        game = Connect()
        global board
        board = game.board

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
                        self.player = 'H'
                        game.current_player = 'H'
                        self.state = 'level'
                        running = False
                        return
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        self.player = 'A'
                        self.state = 'level'
                        running = False
                        return
            screen.blit(mediumfont.render(
                "Choose to go first or second", 1, RED), (125, 300))
            screen.blit(labelfont.render("First", 1, RED), (170, 400)
                        ); p.draw.rect(screen, RED, (150, 450, 100, 50))
            screen.blit(labelfont.render("Second", 1, BLUE), (560, 400)); p.draw.rect(
                screen, BLUE, (550, 450, 100, 50))
            p.display.update()

    def main_play(self):
        running = True
        global player_score
        global alpha_score
        screen.fill((0, 0, 0))
        while running:
            val_moves = game.get_valid_moves()

            for e in p.event.get():
                pos = p.mouse.get_pos()
                move = ((pos[1]//Square_size),
                                   (pos[0]//Square_size)+1)
                if e.type == p.QUIT:
                    running = False
                elif e.type == p.MOUSEBUTTONDOWN and game.get_current() == 'H' and move in val_moves:
                            gameover, winner = game.makeMove(move)
                            if gameover:
                                if winner == None:
                                    alpha_score += 0.5
                                    player_score += 0.5
                                    label = myfont.render(
                                        "Draw", 1, RED)
                                elif winner == 'A':
                                    label = myfont.render(
                                        "Alpha wins", 1, RED)
                                else:
                                    player_score += 1

                                    label = myfont.render(
                                        "You win", 1, RED)
                                running = False
                            
                elif game.get_current() == 'A':
                    prob, _ = neural_network.policy_val_fn(make_board_array(
                        game.board)*return_player_val(game.get_current()), game.get_valid_moves(), True)
                    prob[prob < 0.01] = 0

                    # print(prob)
                    root = node(previous_node=None, p=1.0)

                    for i in range(np.random.randint(50, 1000)):
                        mct_main(
                            game, root, policy_value_fn=neural_network.policy_val_fn)
                    move = root.get_next_move(p=0)
                    # print(move)
                    gameover, winner = game.makeMove(move)

                    if gameover:
                        if winner == None:
                            label = mediumfont.render(
                                "Draw", 1, RED)
                            alpha_score += 0.5
                            player_score += 0.5

                        elif winner == 'A':
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
        while(running):

            for e in p.event.get():
                if e.type == p.QUIT:
                    p.quit()
                mouse = p.mouse.get_pos()
                if e.type == p.MOUSEBUTTONDOWN:
                    if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
                        initialise_neural_network("model/Level1.h5")
                        self.state = 'main_play'
                        return
                    elif 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
                        initialise_neural_network("model/Level2.h5")
                        self.state = 'main_play'
                        return
                    elif 150+100 > mouse[0] > 150 and 650+50 > mouse[1] > 650:
                        initialise_neural_network("model/Level3.h5")
                        self.state = 'main_play'
                        return
                    elif 550+100 > mouse[0] > 550 and 650+50 > mouse[1] > 650:
                        initialise_neural_network("model/Level4.h5")
                        self.state = 'main_play'
                        return
            screen.blit(myfont.render("Choose Level",1,RED),(130,130))
            screen.blit(labelfont.render("Level 1",1,RED),(155,400)); p.draw.rect(screen, RED, (150, 450, 100, 50))
            screen.blit(labelfont.render("Level 2",1,BLUE),(555,400));p.draw.rect(screen, BLUE, (550, 450, 100, 50))
            screen.blit(labelfont.render("Level 3",1,GREEN),(155,600));p.draw.rect(screen, GREEN, (150, 650, 100, 50))
            screen.blit(labelfont.render("Level 4",1,WHITE),(555,600));p.draw.rect(screen, WHITE, (550, 650, 100, 50))
    
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
            screen.blit(myfont.render("Game Score",1,RED),(240,80))
            screen.blit(labelfont.render("Alpha_zero",1,RED),(300,360))
            screen.blit(labelfont.render("You",1,RED),(535,360))

            screen.blit(label_alpha_score, (350, 400))
            screen.blit(label_player_score, (550, 400))
            screen.blit(labelfont.render("Press to play again",1,GREEN), (200, 700))
            screen.blit(labelfont.render("QUIT",1,RED),(550,700))
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
            if board[r][c] == 'A':
                p.draw.circle(screen, RED, (int(
                    (c)*Square_size+Square_size/2), int((r+1)*Square_size+Square_size/2)), RADIUS)
            elif board[r][c] == 'H':
                p.draw.circle(screen, GREEN, (int(
                    (c)*Square_size+Square_size/2), int((r+1)*Square_size+Square_size/2)), RADIUS)


def main():
    game_play = GamePlay()
    while(True):
        game_play.state_manager()


if __name__ == '__main__':
    main()
