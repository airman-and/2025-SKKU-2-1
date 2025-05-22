'''#include <iostream>
#include <vector>
#include <queue>
#include <map>
#include <set>

// Simple graph representation using an adjacency list
class Graph {
public:
    std::map<int, std::vector<int>> adj;

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u); // For undirected graph
    }

    void printGraph() {
        for (auto const& [node, neighbors] : adj) {
            std::cout << "Node " << node << ": ";
            for (int neighbor : neighbors) {
                std::cout << neighbor << " ";
            }
            std::cout << std::endl;
        }
    }

    // Breadth-First Search
    void bfs(int startNode) {
        if (adj.find(startNode) == adj.end()) {
            std::cout << "Start node " << startNode << " not in graph." << std::endl;
            return;
        }

        std::queue<int> q;
        std::set<int> visited; // Using set for efficient lookup

        q.push(startNode);
        visited.insert(startNode);

        std::cout << "BFS starting from node " << startNode << ": ";
        while (!q.empty()) {
            int currentNode = q.front();
            q.pop();
            std::cout << currentNode << " ";

            for (int neighbor : adj[currentNode]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    q.push(neighbor);
                }
            }
        }
        std::cout << std::endl;
    }
};

int main() {
    Graph g;
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);

    std::cout << "Graph structure:" << std::endl;
    g.printGraph();
    std::cout << std::endl;

    g.bfs(2);
    g.bfs(0);
    g.bfs(4); // Node not in graph

    return 0;
}
''
