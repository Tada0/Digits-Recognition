import digits_recognition as DR
from toddlernetwork import neural_network as NN

if __name__ == '__main__':

    n = NN.NeuralNetwork.load('2018_04_22___21_15_40___784_50_10.tnn')
    DR.Test_Network(n)

