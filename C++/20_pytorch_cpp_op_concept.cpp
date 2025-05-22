'''#include <iostream>
#include <vector>
#include <algorithm> // For std::max
#include <numeric>   // For std::inner_product
#include <cmath>     // For std::exp

// Concept: Custom C++ operations that could be part of a PyTorch workflow.
// These are simplified examples using std::vector.
// In a real PyTorch C++ extension, you would use torch::Tensor and PyTorch's C++ API.

// Custom Leaky ReLU activation function
// f(x) = x if x > 0
// f(x) = alpha * x if x <= 0
void custom_leaky_relu(std::vector<double>& data, double alpha = 0.01) {
    for (double& x : data) {
        if (x <= 0) {
            x = alpha * x;
        }
    }
}

// Sigmoid activation function (often used in neural networks)
double sigmoid(double x) {
    return 1.0 / (1.0 + std::exp(-x));
}

// Conceptual simple linear layer forward pass
// output = activation(input * weights^T + bias)
std::vector<double> conceptual_linear_layer_forward(
    const std::vector<double>& input,
    const std::vector<std::vector<double>>& weights, // weights[output_dim][input_dim]
    const std::vector<double>& bias, // bias[output_dim]
    bool apply_sigmoid = false
) {
    if (input.empty() || weights.empty() || bias.empty()) {
        std::cerr << "Error: Input, weights, or bias cannot be empty." << std::endl;
        return {};
    }
    if (weights[0].size() != input.size()) {
        std::cerr << "Error: Weight dimensions mismatch input dimensions. Input size: " << input.size() 
                  << ", Expected by weights: " << weights[0].size() << std::endl;
        return {};
    }
    if (weights.size() != bias.size()) {
        std::cerr << "Error: Bias dimensions mismatch output dimensions of weights. Bias size: " << bias.size()
                  << ", Expected by weights: " << weights.size() << std::endl;
        return {};
    }

    size_t output_dim = weights.size();
    std::vector<double> output(output_dim);

    for (size_t i = 0; i < output_dim; ++i) {
        // Weighted sum: std::inner_product computes sum(input[j] * weights[i][j])
        output[i] = std::inner_product(input.begin(), input.end(), weights[i].begin(), 0.0);
        output[i] += bias[i]; // Add bias
        if (apply_sigmoid) {
            output[i] = sigmoid(output[i]); // Apply activation if specified
        }
    }
    return output;
}


int main() {
    std::cout << "--- Custom C++ Operations for PyTorch (Conceptual Examples) ---" << std::endl;

    // Example 1: Custom Leaky ReLU
    std::vector<double> data1 = {1.0, -2.0, 0.0, 3.0, -0.5};
    std::cout << "\nOriginal data for Leaky ReLU: ";
    for (double x : data1) std::cout << x << " ";
    std::cout << std::endl;

    custom_leaky_relu(data1, 0.1); // Using alpha = 0.1

    std::cout << "Data after custom Leaky ReLU (alpha=0.1): ";
    for (double x : data1) std::cout << x << " ";
    std::cout << std::endl;

    // Example 2: Conceptual Linear Layer Forward Pass
    std::vector<double> input_features = {1.0, 2.0}; // input_dim = 2
    std::vector<std::vector<double>> layer_weights = { // output_dim = 3, input_dim = 2
        {0.1, 0.2},   // weights for output neuron 1
        {0.4, -0.5},  // weights for output neuron 2
        {-0.2, 0.7}   // weights for output neuron 3
    };
    std::vector<double> layer_bias = {0.5, -0.1, 0.2}; // bias for output_dim = 3

    std::cout << "\nInput features for linear layer: ";
    for (double x : input_features) std::cout << x << " ";
    std::cout << std::endl;

    std::vector<double> layer_output_no_activation = conceptual_linear_layer_forward(input_features, layer_weights, layer_bias, false);
    std::cout << "Output of conceptual linear layer (no activation): ";
    for (double x : layer_output_no_activation) std::cout << x << " ";
    std::cout << std::endl;

    std::vector<double> layer_output_with_sigmoid = conceptual_linear_layer_forward(input_features, layer_weights, layer_bias, true);
    std::cout << "Output of conceptual linear layer (with sigmoid): ";
    for (double x : layer_output_with_sigmoid) std::cout << x << " ";
    std::cout << std::endl;


    std::cout << "\nNote: These are simplified C++ examples." << std::endl;
    std::cout << "To integrate custom C++ code with PyTorch, you would typically:" << std::endl;
    std::cout << "1. Use PyTorch's C++ API (e.g., torch::Tensor for data, torch::autograd::Function for custom ops with backward pass)." << std::endl;
    std::cout << "2. Build your C++ code as an extension that Python can import (using Pybind11 or similar)." << std::endl;
    std::cout << "3. This often involves using build systems like CMake." << std::endl;
    std::cout << "Modifying PyTorch's *core* C++ source code directly is a much more complex undertaking, " << std::endl;
    std::cout << "requiring a deep understanding of its architecture (ATen, Caffe2, etc.) and build system." << std::endl;
    std::cout << "For developing custom extensions, refer to the official PyTorch documentation on C++ extensions and LibTorch." << std::endl;

    return 0;
}
'''
