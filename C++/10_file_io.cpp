#include <iostream>
#include <fstream> // For file I/O
#include <string>

int main() {
    std::string filename = "example.txt";

    // Writing to a file
    std::ofstream outFile(filename); // Opens the file for writing (creates if it doesn't exist, truncates if it does)

    if (outFile.is_open()) {
        outFile << "Hello from C++ File I/O!\n";
        outFile << "This is the second line.\n";
        outFile << "Writing numbers: " << 123 << " and " << 45.67 << std::endl;
        outFile.close(); // Close the file
        std::cout << "Successfully wrote to " << filename << std::endl;
    } else {
        std::cerr << "Unable to open file for writing: " << filename << std::endl;
        return 1; // Indicate an error
    }

    std::cout << "\nReading from " << filename << ":" << std::endl;
    // Reading from a file
    std::ifstream inFile(filename); // Opens the file for reading
    std::string line;

    if (inFile.is_open()) {
        while (std::getline(inFile, line)) { // Read line by line
            std::cout << line << std::endl;
        }
        inFile.close(); // Close the file
    } else {
        std::cerr << "Unable to open file for reading: " << filename << std::endl;
        return 1; // Indicate an error
    }

    return 0;
}
