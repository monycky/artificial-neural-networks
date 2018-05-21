from Layers import Layers
from Neuron import Neuron
import numpy as np
import random


class NeuralNetwork:
    def __init__(self, n, m, k):
        self.layers = [start_layer(n, 1), start_layer(m, n), start_layer(k, m)]

    def activate(self, inputs):
        outputs = list()

        for layer in self.layers:
            outputs = layer.activate(inputs)
        return outputs


def start_layer(neurons_count, weights_count):
    neurons = list()
    for i in range(neurons_count):
        neuron = Neuron(np.random.rand(weights_count), random.random())
        neurons.append(neuron)
    return Layers(neurons)


NeuralNetwork(1, 2, 1)