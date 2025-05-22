'''#include <iostream>
#include <vector>
#include <string>
#include <algorithm> // For std::shuffle, std::generate
#include <random>    // For std::mt19937, std::uniform_int_distribution

// Simple representation of a chromosome (e.g., a binary string)
class Chromosome {
public:
    std::string genes; // Binary string for simplicity
    double fitness;

    Chromosome(int length) : fitness(0.0) {
        genes.resize(length);
        // Initialize with random binary genes (0 or 1)
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> distrib(0, 1);
        for (int i = 0; i < length; ++i) {
            genes[i] = distrib(gen) == 0 ? '0' : '1';
        }
    }

    Chromosome(std::string initial_genes) : genes(initial_genes), fitness(0.0) {}

    void print() const {
        std::cout << "Genes: " << genes << ", Fitness: " << fitness;
    }

    // Simple mutation: flip a random bit
    void mutate(double mutationRate) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_real_distribution<> distrib_rate(0.0, 1.0);
        std::uniform_int_distribution<> distrib_gene_idx(0, genes.length() - 1);

        for (size_t i = 0; i < genes.length(); ++i) {
            if (distrib_rate(gen) < mutationRate) {
                genes[i] = (genes[i] == '0' ? '1' : '0');
                std::cout << " (Mutated gene at index " << i << ")";
            }
        }
    }

    // Example fitness function: count number of '1's (simple "OneMax" problem)
    void calculateFitness() {
        fitness = 0;
        for (char gene : genes) {
            if (gene == '1') {
                fitness++;
            }
        }
    }
};

// Simple Crossover: Single-point crossover
std::pair<Chromosome, Chromosome> crossover(const Chromosome& parent1, const Chromosome& parent2) {
    if (parent1.genes.length() != parent2.genes.length() || parent1.genes.empty()) {
        std::cerr << "Error: Parents must have same non-zero length for crossover." << std::endl;
        return {Chromosome(0), Chromosome(0)}; // Return empty chromosomes
    }

    std::random_device rd;
    std::mt19937 gen(rd());
    // Crossover point between 1 and length-1
    std::uniform_int_distribution<> distrib(1, parent1.genes.length() - 1);
    int crossoverPoint = distrib(gen);

    std::string child1_genes = parent1.genes.substr(0, crossoverPoint) + parent2.genes.substr(crossoverPoint);
    std::string child2_genes = parent2.genes.substr(0, crossoverPoint) + parent1.genes.substr(crossoverPoint);

    return {Chromosome(child1_genes), Chromosome(child2_genes)};
}


int main() {
    int chromosomeLength = 10;
    double mutationRate = 0.1; // 10% chance per gene

    Chromosome individual1(chromosomeLength);
    individual1.calculateFitness();
    std::cout << "Individual 1: ";
    individual1.print();
    std::cout << std::endl;

    Chromosome individual2("0000011111");
    individual2.calculateFitness();
    std::cout << "Individual 2: ";
    individual2.print();
    std::cout << std::endl;

    std::cout << "
Mutating Individual 1:" << std::endl;
    individual1.mutate(mutationRate);
    individual1.calculateFitness(); // Recalculate fitness after mutation
    std::cout << "
Individual 1 (after mutation): ";
    individual1.print();
    std::cout << std::endl;

    std::cout << "
Performing Crossover between Individual 1 and Individual 2:" << std::endl;
    auto children = crossover(individual1, individual2);
    children.first.calculateFitness();
    children.second.calculateFitness();

    std::cout << "Child 1: ";
    children.first.print();
    std::cout << std::endl;
    std::cout << "Child 2: ";
    children.second.print();
    std::cout << std::endl;
    
    // Example of crossover with different length (should ideally be handled or prevented)
    // Chromosome short_parent("101");
    // auto bad_children = crossover(individual1, short_parent);


    return 0;
}
''
