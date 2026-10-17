import numpy as np

#A single neuron, with inputs weights and bias, calculating the vector product of inputs and weigths

def neuron(inputs, weights, bias):
    result = np.dot(inputs, weights)+bias
    return result

print(neuron(inputs=np.array([0.9,0.8,.01]), weights= np.array([0.1, 0.7, 0.3]), bias= 0.1))


# 3 Neurons, with inputs weights and biases, matrix multiplication
def layers(inputs, weights, biases):
    results = np.dot(weights, inputs)+ biases
    return results

inputs = np.array([0.9, 0.8, 0.01])

weights = np.array([
    [0.1, 0.7, 0.3],  # Neuron 1
    [0.4, 0.2, 0.8],  # Neuron 2
    [0.6, 0.5, 0.1]   # Neuron 3
])

biases = np.array([0.1, 0.2, 0.3])

print(layers(inputs=inputs, weights=weights, biases=biases))


#Adding Activation function to the weigthed sum
biases = np.array([-1.0, 0.2, -2.0])

def layers_activate(inputs, weights, biases):
    weighted_sum = np.dot(weights, inputs) + biases

    activated = np.maximum(0, weighted_sum)
    return activated

print(layers_activate(inputs=inputs, weights=weights, biases=biases))

##One forward pushing neural network with random weights and biases

#create a forward pushing function, calculating the activated results of each layer, and pushing it as an input to the next
inputs = np.array([0.5, 0.8, 0.2, 0.0])

weights1 = np.random.randn(4, 4)
biases1 = np.random.randn(4)

weights2 = np.random.randn(3, 4)
biases2 = np.random.randn(3)

def forward(inputs, weights_1, biases_1, weights_2, biases_2):
    layer_one_result = layers_activate(inputs,weights_1,biases_1)
    layer_two_result = layers(layer_one_result, weights_2, biases_2)
    return layer_two_result

print(forward(inputs,weights1,biases1,weights2,biases2))

#choose highest value of the output neurons to decide on an action

def predict(inputs, weights_1, biases_1, weights_2, biases_2):
    index = np.argmax(forward(inputs,weights_1,biases_1,weights_2,biases_2))
    return index

print(predict(inputs,weights1,biases1,weights2,biases2))


## Generate a population of neural networks with random weights and biases

def generate_population(population_size):
    population = []

    for i in range(0,population_size):
        neural_network = {
            "weights1": np.random.randn(4, 4),
            "biases1": np.random.randn(4),
            "weights2": np.random.randn(3, 4),
            "biases2": np.random.randn(3),
        }
        population.append(neural_network)

    return population

population = generate_population(50)

#create a fitness function to evaluate which neural network performed the best

def fitness(survival_frames, score):
    fitness_score = survival_frames/60 + 10*score
    return fitness_score

print(fitness(20,7))