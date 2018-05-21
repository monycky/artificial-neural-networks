import numpy as np
import math as math


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def activate(self, inputs):
        return 1 / (1 + math.exp(-dot_product(inputs, self.weights)) - self.bias)


def dot_product(inputs, weight):
    return sum((np.multiply(inputs, weight)))

