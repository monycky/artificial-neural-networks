# import Neuron


class Layers:
    def __init__(self, neurons):
        self.neurons = neurons

    def activate(self, inputs):
        outputs = list()
        for neuron in self.neurons:
            outputs.append(neuron.activate(inputs))
        return outputs
