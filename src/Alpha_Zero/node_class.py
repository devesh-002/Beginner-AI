import random
import numpy as np
import math
from copy import deepcopy

# These are nodes of each MCT defined


class node(object):
    def __init__(self, previous_node, p):
        self.previous_node = previous_node
        self.states = {}
        self.next_node = {}  # List of all childrens of a node
        self.N = 0
        self.P = p
        self.S = 0
        self.expanded = False

    def check_if_leaf(self):
        if len(self.next_node) == 0:
            return True
        else:
            return False

    def check_if_root(self):
        if self.previous_node == None:
            return True
        else:
            return False

    def expand(self, moves):
        if self.expanded == False:
            for m, p in zip(moves['moves'], moves['prob']):
                self.next_node[m] = node(previous_node=self, p=p)
            self.expanded = True

    def backup(self, value):
        if self.check_if_root() == False:
            self.previous_node.backup(-value)
        self.N += 1
        self.S += value

    def evaluate(self, constant):
        Q = 0 if self.N == 0 else self.S/self.N
        U = (constant*self.P*math.sqrt(self.previous_node.N)/(1+self.N))
        return Q+U

    def tree_search(self):
        return max(self.next_node.items(), key=lambda N: N[1].evaluate(5))

    def get_next_move(self, p):
        if self.check_if_root() == True:
            if p >= 0 and p <= 1:
                if p > 0:
                    moves = []
                    num = []
                    for move, next_node in self.next_node.items():
                        moves.append(move)
                        num.append(next_node.N)
                    probs = softmax(1.0/p*np.log(np.array(num)+1e-10))
                    assert np.allclose(np.sum(probs), 1)
                    return random.choices(moves, weights=probs, k=1)[0]
                else:
                    best_visit = -np.inf
                    best_move = None
                    for i, (move, next_node) in enumerate(self.next_node.items()):
                        if next_node.N > best_visit:
                            best_visit = next_node.N
                            best_move = move
                    return best_move

    def get_next_move_and_prob_matrix(self, w, h, p, alpha_net):
        assert self.check_if_root()
        assert 0 <= p <= 1
        assert(p > 0 and alpha_net is None) or (
            p == 0 and alpha_net is not None)

        if p > 0:
            moves = []
            num = []
            for move, next_node in self.next_node.items():
                moves.append(move)
                num.append(next_node.N)

            probs = softmax(1.0/p*np.log(np.array(num)+1e-10))
        else:

            best_visit = -np.inf
            best_move_idx = None
            num_of_moves = 0
            moves = []
            for i, (move, next_node) in enumerate(self.next_node.items()):
                if next_node.N > best_visit:
                    best_visit = next_node.N
                    best_move_idx = i
                num_of_moves += 1
                moves.append(move)
            probs = np.zeros((num_of_moves,))
            probs[best_move_idx] = 1
            probs = probs*0.75 + \
                np.random.dirichlet([alpha_net]*num_of_moves)*0.25
            # print(probs)
            if np.sum(probs) == 0:
                print(probs)
                print(self.next_node.items())
            assert np.allclose(np.sum(probs), 1)
        pi_vec = np.zeros((w * h,))
        for move, prob in zip(moves, probs):
            index = (move[0]-1) * w + (move[1]-1)
            pi_vec[index] = prob
        return random.choices(moves, weights=probs, k=1)[0], pi_vec

# The node evaluation function


def softmax(x):
    probs = np.exp(x - np.max(x))
    probs /= np.sum(probs)
    return probs
