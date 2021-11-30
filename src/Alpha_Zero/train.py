from tensorflow.keras import layers, regularizers
from initialiser import *
from evaluation import *
from self_train import *
from Neural_network import *
from c4 import *
import tensorflow.keras.optimizers as optimizers
import tensorflow.keras.utils as utils
import tensorflow.keras.layers as layers
import tensorflow.keras.models as models
from tensorflow.python.keras.layers.pooling import MaxPooling2D
import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class store:
    def __init__(self, num, batch_size):
        self.boards = np.zeros((num, 6, 6))
        self.prob = np.zeros((num, 36))
        self.arr = np.zeros((num, 36))
        self.batch_size = batch_size
        self.num = num
        self.p = 0
        self.N = 0

    def add(self, boards, checks, arr, game_len):
        checks = checks.reshape(boards.shape)
        for i in range(3):
            for bool in [True, False]:
                board = change(np.rot90(boards, k=i, axes=(1, 2)), bool)
                check = change(np.rot90(checks, k=i, axes=(1, 2)),
                               bool).reshape(game_len, -1)
                for i in range(game_len):
                    self.boards[self.p] = board[i]
                    self.prob[self.p] = check[i]
                    self.arr[self.p] = arr[i]
                    self.p = (self.p+1) % self.num
                    self.N = min(self.N+1, self.num)

    def return_fun(self):
        return self.batch_size <= self.N

    def test_node(self):
        indexes = np.random.randint(self.N, size=self.batch_size)
        # print(self.boards)
        boards = tf.convert_to_tensor(self.boards[indexes])
        boards = tf.cast(tf.reshape(boards, shape=(
            self.batch_size, 1, 6, 6)), dtype=tf.float32)
        probs = tf.reshape(tf.convert_to_tensor(
            self.prob[indexes]), shape=(self.batch_size, 36))
        probs = tf.cast(probs, dtype=tf.float32)
        arr = tf.reshape(tf.convert_to_tensor(
            self.arr[indexes]), shape=(self.batch_size, 36))
        arr = tf.cast(arr, dtype=tf.float32)
        return boards, probs, arr


def change(array, do_the_flip):
    if do_the_flip:
        return np.flip(array, axis=2)
    else:
        return array


memory = store(buffer_size, batch_size)
Game_ = Connect
optimizer = optimizers.Adam(1e-4)
neural_network = (AlphaNet(6, 6))
neural_network.build(input_shape=(1, 1, 6, 6))

for idx in (range(num_games)):
    boards, probs, arr = play_self(
        Game_, num_mct_alpha, policy_val=neural_network.policy_val_fn, temp=3)
    memory.add(boards, probs, arr, boards.shape[0])
    if memory.return_fun():
        for i in range(num_grad_steps):
            new_state, new_prob, new_arr = memory.test_node()
            # Below is the important part of training, it takes all the trainable variables and pushes them along with loss to minimize it

            def compute_loss():
                predicted_prob, predicted_arr = neural_network(new_state)

                loss_1 = tf.reduce_mean((new_arr-predicted_arr)**2)
                loss_2 = -tf.reduce_mean(tf.reduce_sum(new_prob*predicted_prob, axis=None))
                loss = loss_1+loss_2
                return loss

            optimizer.minimize(
                compute_loss, neural_network.trainable_variables)
    # The below evaluation is costly and optional
    if (idx+1) % eval_freq == 0:
        alpha_player = []
        for i in range(eval_num_games):
            score = play_mct(Game=Game_, num_mct=num_mct, num_alphanet=num_mct_alpha,
                             policy_val=neural_network.policy_val_fn, inp="alpha")
        alpha_player.append(score)

        mct_player = []
        for i in range(eval_num_games):
            score = play_mct(Game=Game_, num_mct=num_mct, num_alphanet=num_mct_alpha,
                             policy_val=neural_network.policy_val_fn, inp="mct")
            mct_player.append(score)

        alpha_player = float(np.mean(alpha_player))
        mct_player = float(np.mean(mct_player))

        mean_net = (alpha_player+mct_player)/2
        print("Evaluation with Alpha playing is ", round(alpha_player, 2))

        print("Evaluation with MCT playing is ", round(mct_player, 2))
        print("Net score ", round(mean_net, 2))
        neural_network.save_weights("save_model.h5")
    print("Iter ", idx+1, " of ", num_games, " is over")
