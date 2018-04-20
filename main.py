import digits_recognition as DR
from toddlernetwork import neural_network as NN

if __name__ == '__main__':

    # network = NN.NeuralNetwork(784, 50, 10)
    # DR.Train_Network(network, 100)
    # DR.Test_Network(network)
    # network.save()

    network = NN.NeuralNetwork('2018_04_18___13_44_23___784_200_10')
    DR.Test_Network_With_Image(network, 'Test_Images/test_image.png')
