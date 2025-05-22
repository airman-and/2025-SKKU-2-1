'''#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm> // For std::sort, std::min_element
#include <map>

// Simple structure to represent a data point with features and a label
struct DataPoint {
    std::vector<double> features;
    int label; // Class label (e.g., 0, 1, 2, ...)
    int id; // Optional: for tracking
};

// Function to calculate Euclidean distance between two points
double euclideanDistance(const std::vector<double>& p1, const std::vector<double>& p2) {
    if (p1.size() != p2.size()) {
        std::cerr << "Error: Feature vectors must have the same dimension." << std::endl;
        return -1.0; // Or throw an exception
    }
    double sum = 0.0;
    for (size_t i = 0; i < p1.size(); ++i) {
        sum += (p1[i] - p2[i]) * (p1[i] - p2[i]);
    }
    return std::sqrt(sum);
}

// Simple KNN classifier
class KNNClassifier {
public:
    std::vector<DataPoint> trainingData;
    int k; // Number of neighbors to consider

    KNNClassifier(int num_neighbors) : k(num_neighbors) {}

    void train(const std::vector<DataPoint>& data) {
        trainingData = data;
    }

    int predict(const std::vector<double>& newPointFeatures) {
        if (trainingData.empty()) {
            std::cerr << "Error: Training data is empty. Please train the model first." << std::endl;
            return -1; // Or throw
        }
        if (k > trainingData.size()) {
             std::cerr << "Warning: k is larger than the number of training samples. Setting k to training set size." << std::endl;
             k = trainingData.size();
        }


        // Calculate distances to all training points
        std::vector<std::pair<double, int>> distances; // pair: <distance, label>
        for (const auto& point : trainingData) {
            double dist = euclideanDistance(newPointFeatures, point.features);
            if (dist >= 0) { // Check for valid distance
                distances.push_back({dist, point.label});
            }
        }

        // Sort distances in ascending order
        std::sort(distances.begin(), distances.end());

        // Get the labels of the k nearest neighbors
        std::map<int, int> labelCounts; // <label, count>
        for (int i = 0; i < k && i < distances.size(); ++i) {
            labelCounts[distances[i].second]++;
        }

        // Find the most frequent label among the k neighbors (majority vote)
        int predictedLabel = -1;
        int maxCount = 0;
        for (const auto& pair : labelCounts) {
            if (pair.second > maxCount) {
                maxCount = pair.second;
                predictedLabel = pair.first;
            }
        }
        return predictedLabel;
    }
};

int main() {
    // Sample training data
    std::vector<DataPoint> trainPoints = {
        {{1.0, 1.0}, 0, 1},
        {{1.5, 2.0}, 0, 2},
        {{2.0, 1.5}, 0, 3},
        {{5.0, 5.0}, 1, 4},
        {{5.5, 6.0}, 1, 5},
        {{6.0, 5.5}, 1, 6},
        {{2.5, 3.0}, 0, 7},
        {{7.0, 7.0}, 1, 8}
    };

    KNNClassifier knn(3); // Use K=3
    knn.train(trainPoints);

    // New points to classify
    std::vector<double> testPoint1 = {2.0, 2.0}; // Expected: 0
    std::vector<double> testPoint2 = {6.0, 6.0}; // Expected: 1
    std::vector<double> testPoint3 = {3.0, 3.0}; // Borderline, depends on K

    std::cout << "Classifying point (2.0, 2.0): Label = " << knn.predict(testPoint1) << std::endl;
    std::cout << "Classifying point (6.0, 6.0): Label = " << knn.predict(testPoint2) << std::endl;
    std::cout << "Classifying point (3.0, 3.0): Label = " << knn.predict(testPoint3) << std::endl;

    KNNClassifier knn_k1(1);
    knn_k1.train(trainPoints);
    std::cout << "
Using K=1:" << std::endl;
    std::cout << "Classifying point (3.0, 3.0): Label = " << knn_k1.predict(testPoint3) << std::endl;


    // Test with k > trainingData.size()
    KNNClassifier knn_large_k(100);
    knn_large_k.train(trainPoints);
    std::cout << "
Using K=100 (larger than dataset):" << std::endl;
    std::cout << "Classifying point (3.0, 3.0): Label = " << knn_large_k.predict(testPoint3) << std::endl;


    return 0;
}
''
