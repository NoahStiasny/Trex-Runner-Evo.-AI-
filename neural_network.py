import numpy as np

class NeuralNetwork:
    def __init__(self, weights_1=None, weights_2=None, biases_1=None,biases_2=None):

        self.weights1 = np.random.randn(4, 4)
        self.biases1 = np.random.randn(4)

        self.weights2 = np.random.randn(3, 4)
        self.biases2 = np.random.randn(3)

        if weights_1 is not None:
            self.weights1 = weights_1.copy()
        if weights_2 is not None:
            self.weights2 = weights_2.copy()
        if biases_1 is not None:
            self.biases1 = biases_1.copy()
        if biases_2 is not None:
            self.biases2 = biases_2.copy()

    def layers(self, inputs, weights, biases):
        results = np.dot(weights, inputs) + biases
        return results

    def layers_activate(self, inputs, weights, biases):
        weighted_sum = np.dot(weights, inputs) + biases
        activated = np.maximum(0, weighted_sum)
        return activated

    def forward(self, input):
        layer_one_result = self.layers_activate(input, self.weights1, self.biases1)
        layer_two_result = self.layers(layer_one_result, self.weights2, self.biases2)
        return layer_two_result

    def predict(self, input):
        index = np.argmax(self.forward(input))
        return index


