import digits_recognition as DR
from toddlernetwork import neural_network as NN

if __name__ == '__main__':
    # Create Neural Network object with 784 inputs, 50 hidden nodes and 10 outputs
    network = NN.NeuralNetwork(784, 50, 10)

    # Create Neural Network from existing file
    network = NN.NeuralNetwork.load('2018_04_22___21_15_40___784_50_10.tnn')

    # Use of Training Method (50 iterations)
    DR.Train_Network(network, 50)

    # Use of Test Method
    DR.Test_Network(network)

    # Use of Digit Recognition with user provided image
    DR.Test_Network_With_Image(network, 'Test_Images/test_image.png')

