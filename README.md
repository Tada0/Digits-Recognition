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

####<a href="https://github.com/Tada0/Toddler-Neural-Network">Toddler Neural Network</a> required


Example code in ``python``

    # Import the library
    from toddlernetwork import neural_network as NN
    import digits_recognition as DR
    
    # Create Neural Network object with 784 inputs, n hidden nodes and 10 outputs
    network = NN.NeuralNetwork(784, n, 10)
    
    # Create Neural Network from existing file
    network = NN.NeuralNetwork('filename')
    
    # Use of Training Method 
    DR.Train_Network(network, iterations)
    
    # Use of Test Methond
    DR.Test_Network(network)
   
    # Use of Digit Recognition with user provided image
    DR.Test_Network_With_Image(network, image_path):
    
## License
    
Digits-Recognition is licensed under the [MIT License](http://opensource.org/licenses/MIT).