from collections import deque
import random

#Undirected graph using an adjacency list
class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def are_connected(self, node1, node2):
        return node2 in self.adj[node1]

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self):
        self.adj[len(self.adj)] = []

    def add_edge(self, node1, node2):
        if node1 not in self.adj[node2]:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)

    def number_of_nodes():
        return len()
    

def create_random_graph(i,j): 
    numNodes = i 
    numEdges = j
    count = 0
    # Assuming we have a simple graph where we cannot have multiple edges or self-loops
    # Max number of edges is found through the equation: nodes * (nodes - 1) / 2
    maxEdges = (i * (i-1)) // 2 

    if j > maxEdges: 
        print("Number of edges is too large for the number of vertices. Cannot generate graph")
        return Graph(i)
    
    # Generate graph with i nodes
    graph = Graph(i)

    while count < j:
        # Randomly select two nodes
        node1 = random.randint(0, i-1)
        node2 = random.randint(0, i-1)

        # Only add the edge between two nodes if the nodes are not equal
        # and if there does not exist an edge between the two nodes yet
        if node1 != node2 and node2 not in graph.adj[node1]:
            graph.add_edge(node1, node2)
            count += 1

    return graph

'''
G = create_random_graph(4,3)
print(G.adj)
'''






