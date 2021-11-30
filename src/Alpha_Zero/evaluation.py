from node_class import *
from mct import *

# This is a suplementary file just for evaluation


def play_mct(Game, num_mct, num_alphanet, policy_val, inp):
    game = Game()
    if inp == "mct":
        mcts = game.get_current()
        alpha = game.get_opponent()
    elif inp == "alpha":
        alpha = game.get_current()
        mcts = game.get_opponent()
    else:
        print("enter valid input(Check eval.py)")

    while True:
        root = node(previous_node=None, p=1.0)
        if game.get_current() == alpha:
            for i in range(num_alphanet):
                mct_main(game, root, policy_value_fn=policy_val)
            move = root.get_next_move(p=0)
        else:
            for i in range(num_mct):
                mct_main(game, root, policy_value_fn=None)
            move = root.get_next_move(p=0)
        check, winner = game.makeMove(move)
        if check == True:
            break
    if winner == mcts:
        return -1
    elif winner == alpha:
        return 1
    elif winner == None:
        return 0
