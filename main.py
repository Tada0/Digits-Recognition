import digits_recognition as DR
import ftplib
import pickle
from toddlernetwork import neural_network as NN

if __name__ == '__main__':

    n = NN.NeuralNetwork(784, 50, 10)
    n.set_learning_rate(0.003)
    DR.Train_Network(n, 1000)
    DR.Test_Network(n)
    n.save()

    session = ftplib.FTP('keikeikei.ugu.pl', 'keikeikei.ugu.pl', 'keikeikei123')
    file = open("nn.tnn", 'rb')
    session.storbinary('STOR nn.tnn', file)
    file.close()
    session.quit()