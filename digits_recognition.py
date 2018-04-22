import mnist
import warnings
from time import gmtime, strftime
from timeit import default_timer as timer

warnings.filterwarnings("ignore")


def Train_Network(n_network, n):
    iterations = n

    print("Preparing Training Data Set.")
    training_images = [x.reshape(1, x.shape[0] * x.shape[1]).tolist()[0] for x in mnist.train_images()]
    print("Preparing Training Data Set Completed.\n")

    print("Training Start.")
    training_labels = mnist.train_labels()

    answers = [[0 for _ in range(10)] for _ in range(len(training_labels))]

    for x in range(len(answers)):
        answers[x][training_labels[x]] = 1

    training_start = timer()

    for y in range(iterations):

        iteration_start = timer()

        for x in range(len(training_images)):
            n_network.train(training_images[x], answers[x])

        iteration_end = timer()

        print("{0:.1f}".format((y + 1) / iterations * 100) + "% Completed. Elapsed Time:",
              "{0:.1f}".format(iteration_end - iteration_start) + "s. Remaining Time ~",
              "{0:.1f}".format((iterations - y - 1) * (iteration_end - iteration_start)) + "s.")

    training_end = timer()
    print("Training End. Elapsed time: " + strftime("%Hh, %Mm, %Ss.", gmtime(training_end - training_start)) + "\n")


def Test_Network(n_network):
    print("Preparing Test Data Set.")
    test_images = [x.reshape(1, x.shape[0] * x.shape[1]).tolist()[0] for x in mnist.test_images()]
    print("Preparing Test Data Set Completed.\n")
    print("Testing Start.")

    test_labels = mnist.test_labels()

    successes = 0

    for x in range(len(test_images)):
        output = n_network.feedforward(test_images[x])

        pos = 0
        max_probability = 0
        for z in range(10):
            if output[z] > max_probability:
                max_probability = output[z]
                pos = z

        if pos == test_labels[x]:
            successes += 1

    print("Testing End.\n")
    print("Successes : {0:.2f}%".format(successes / len(test_labels) * 100))


def Test_Network_With_Image(n_network, image):
    import png

    print("Gathering Image Metadata.\n")
    reader = png.Reader(filename=image)
    w, h, pixels, metadata = reader.read_flat()
    pixels = [pixels[x] for x in [x * 4 for x in range(w * h)]]
    output = n_network.feedforward(pixels)

    position = 0
    max_probability = 0

    for x in range(len(output)):
        if output[x] > max_probability:
            max_probability = output[x]
            position = x

    print("Prediction: {0}".format(position) + " Certainty: {0:.2f}".format(output[position] * 100) + "%")

