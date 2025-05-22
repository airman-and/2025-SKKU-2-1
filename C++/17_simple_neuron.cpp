#include <iostream>
#include <vector>
#include <cmath> // For exp (sigmoid function)
#include <numeric> // For inner_product
#include <stdexcept> // For std::invalid_argument

// Sigmoid activation function
double sigmoid(double x) {
    return 1.0 / (1.0 + std::exp(-x));
}

// A very simple representation of a single neuron
class Neuron {
public:
    std::vector<double> weights;
    double bias;

    Neuron(int numInputs) : bias(0.0) {
        // Initialize weights randomly (or with zeros for simplicity here)
        weights.resize(numInputs, 0.5); // Example: all weights 0.5
        bias = 0.1; // Example bias
    }

    Neuron(std::vector<double> w, double b) : weights(w), bias(b) {}

    double feedforward(const std::vector<double>& inputs) {
        if (inputs.size() != weights.size()) {
            throw std::invalid_argument("Error: Number of inputs must match number of weights.");
        }

        // Calculate weighted sum: (inputs[0]*weights[0] + inputs[1]*weights[1] + ...) + bias
        double total = std::inner_product(inputs.begin(), inputs.end(), weights.begin(), 0.0);
        total += bias;

        // Apply activation function
        return sigmoid(total);
    }
};

int main() {
    // Neuron with 2 inputs
    Neuron neuron1(2);
    neuron1.weights = {0.7, -0.3};
    neuron1.bias = 0.1;

    std::vector<double> inputs1 = {10.0, 5.0};
    double output1 = neuron1.feedforward(inputs1);
    std::cout << "Neuron 1 with inputs (" << inputs1[0] << ", " << inputs1[1] << ") output: " << output1 << std::endl;

    // Neuron with 3 inputs
    Neuron neuron2({0.2, 0.8, -0.5}); // Using constructor with initializer list for weights
    neuron2.bias = -0.2;

    std::vector<double> inputs2 = {1.0, 0.5, 2.0};
    double output2 = neuron2.feedforward(inputs2);
    std::cout << "Neuron 2 with inputs (" << inputs2[0] << ", " << inputs2[1] << ", " << inputs2[2] << ") output: " << output2 << std::endl;
    
    // Example of input size mismatch
    std::vector<double> wrong_inputs = {1.0};
    try {
        neuron1.feedforward(wrong_inputs);
    } catch (const std::invalid_argument& e) {
        std::cerr << "Caught exception: " << e.what() << std::endl;
    }


    return 0;
}

