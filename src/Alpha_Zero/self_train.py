import numpy as np

from node_class import *
from mct import *
from utils import *
from typing import Callable

# This produces the games it plays


def play_self(Game, num_mct, temp, policy_val: Callable = None):

    game = Game()
    boards = []
    probs = []
    num_act = 0
    while True:
        board = make_board_array(game.board) * \
            return_player_val(game.get_current())

        root = node(previous_node=None, p=1.0)
        for i in range(num_mct):
            mct_main(game, root, policy_value_fn=policy_val)
        if num_act < temp:
            move, vec = root.get_next_move_and_prob_matrix(
                6, 6, p=1, alpha_net=None)
        else:
            move, vec = root.get_next_move_and_prob_matrix(
                6, 6, p=0, alpha_net=0.3)
        boards.append(board)
        probs.append(vec)
        check, winner = game.makeMove(move)

        num_act += 1
        if check:
            break
    game_len = len(boards)
    if winner == None:
        arr = [0] * game_len
    else:
        arr = []
        final_player = game.get_previous_player()
        favour = 1 if final_player == winner else -1
        for i in range(game_len):
            arr.append(favour)
            favour *= -1
        arr = list(reversed(arr))

    boards, probs, arr = map(np.array, [boards, probs, arr])
    return boards, probs, arr
