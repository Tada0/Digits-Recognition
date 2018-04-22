Digits-Recognition
==================

## Project status 

[![Travis](https://travis-ci.org/Tada0/Digits-Recognition.svg?branch=master)]()

## About

Digits Recognition is a project created using my other project <a href="https://github.com/Tada0/Toddler-Neural-Network">Toddler Neural Network</a>

- **Source:** https://github.com/Tada0/Digits-Recognition
- **Bug reports:** https://github.com/Tada0/Digits-Recognition/issues
- **Author:** https://github.com/Tada0
- **Contact:** <a href="mailto:tomekholda@gmail.com">@</a>

It provides:

- Training method, based on <a href="http://yann.lecun.com/exdb/mnist/">THE MNIST DATABASE</a>
- Test method, based on the same database
- Digit recognition based on user provided image
- Picture should be 28x28px, png format, black background, as example in Test_Images/*



<a href="https://github.com/Tada0/Toddler-Neural-Network">Toddler Neural Network</a> required


Example code in ``python``

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

## License
    
Digits-Recognition is licensed under the [MIT License](http://opensource.org/licenses/MIT).