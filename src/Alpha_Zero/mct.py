from utils import make_board_array, return_player_val
from c4 import *
from node_class import node
from copy import deepcopy
import random
# Here we have the main MCT structure defined


def random_selection(valid_moves):
    num = len(valid_moves)
    probs = [1/num] * num
    return {"moves": valid_moves, "prob": probs}


def test_move(pol):
    return random.choices(pol["moves"], weights=pol["prob"])[0]


def iter_till_end(game):
    current_player = game.get_current()
    while True:
        l = game.get_valid_moves()
        if(len(l) == 0):
            return 0
        move = test_move(random_selection(l))
        check, winner = game.makeMove(move)
        if check == True:
            break

    if winner == None:
        return 0
    if winner == current_player:
        return 1
    return -1


def mct_main(game, root: node, policy_value_fn=None):
    game, node = deepcopy(game), root
    while True:
        if node.check_if_leaf() == True:
            break
        else:
            move, node = node.tree_search()
            check, winner = game.makeMove(move)
    opp_val = 1
    if node.check_if_root() == True or check == False:
        if policy_value_fn == None:
            l = game.get_valid_moves()
            if len(l) == 0:
                opp_val = 0
            else:
                node.expand(moves=random_selection(l))
                opp_val = iter_till_end(game)
        else:
            total = make_board_array(game.board)
            player_val = return_player_val(game.get_current())
            moves_set, opp_val = policy_value_fn(
                board=(total*player_val), valid_moves=game.get_valid_moves(), check=False)
            node.expand(moves=moves_set)
    else:
        if winner == None:
            opp_val = 0
        else:
            if winner == game.get_current():
                opp_val = 1
            else:
                opp_val = -1

    node.backup(-(opp_val))
