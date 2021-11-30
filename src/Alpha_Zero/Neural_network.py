import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from tensorflow.keras import layers, regularizers
from tensorflow.python.ops.numpy_ops import np_config
from utils import *
import tensorflow.keras.optimizers as optimizers
import tensorflow.keras.utils as utils
import tensorflow.keras.models as models
from tensorflow.python.keras.layers.pooling import MaxPooling2D
from tensorflow import keras
import tensorflow as tf

import numpy as np

np_config.enable_numpy_behavior()


class AlphaNet(tf.keras.Model):
    def __init__(self, width, height):
        super(AlphaNet, self).__init__()
        self.width = width
        self.height = height

        self.conv1 = layers.Conv2D(
            32, kernel_size=3, padding='same', input_shape=(1, 6, 6, 1))
        self.conv2 = layers.Conv2D(64, kernel_size=3, padding='same')
        self.conv3 = layers.Conv2D(128, kernel_size=3, padding='same')
        self.action_conv = layers.Conv2D(4, kernel_size=1)
        self.action_fc = layers.Dense(36, activation=None)

        self.eval_conv = layers.Conv2D(2, kernel_size=3, padding='same')
        self.eval_fc1 = layers.Dense(64)
        self.eval_fc2 = layers.Dense(1)

    def call(self, inputs):

        inputs = tf.transpose(inputs, [0, 2, 3, 1])
        x = self.conv1(inputs)
        x = tf.nn.relu(x)
        x = self.conv2(x)
        x = tf.nn.relu(x)
        x = self.conv3(x)
        x = tf.nn.relu(x)
        x_act = self.action_conv(x)
        x_act = tf.nn.relu(x_act)
        x_act = tf.reshape(x_act, shape=[1, 144])
        x_act = self.action_fc(x_act)
        x_act = tf.nn.log_softmax(axis=1, logits=x_act)

        x_val = self.eval_conv(x)
        x_val = tf.nn.relu(x_val)
        x_val = tf.reshape(x_val, shape=[1, 72])
        x_val = self.eval_fc1(x_val)
        x_val = tf.nn.relu(x_val)
        x_val = self.eval_fc2(x_val)
        x_val = tf.nn.tanh(x_val)
        return x_act, x_val
# Below is the main policy value function to implement the code and guide the model to find probabiities

    def policy_val_fn(self, board, valid_moves, check: bool = False):

        total = board
        f_tensor = tf.cast(total, dtype='float32')
        f_tensor = tf.expand_dims(f_tensor, axis=0)
        f_tensor = tf.expand_dims(f_tensor, axis=0)

        assert f_tensor.get_shape().as_list() == [
            1, 1, self.height, self.width]
        f_tensor = tf.cast(f_tensor, dtype=tf.float32)
        with tf.GradientTape() as t:
            with t.stop_recording():
                x_new, x_fin = (self(f_tensor))

        p_new = np.exp(tf.squeeze(x_new).numpy())

        probs = []
        for move in valid_moves:
            index = (move[0]-1) * self.width + (move[1]-1)
            probs.append(p_new[index])

        if check is False:  # as guiding policy
            return {"moves": valid_moves, "prob": probs}, float(x_fin)
        else:  # for evaluation
            return p_new, float(x_fin)

    def get_config(self):
        config = super(AlphaNet, self).get_config()
        config.update({
            'conv1': self.conv1,
            'conv2': self.conv2,
            'conv3': self.conv3,
            'action_conv': self.action_conv,
            'action_fc': self.action_fc,
            'eval_conv': self.eval_conv,
            'eval_fc1': self.eval_fc1,
            'eval_fc2': self.eval_fc2
        })
        return config
