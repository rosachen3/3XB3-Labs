from collections import deque
import random
import matplotlib.pyplot as plot

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
    
def MIS(G):
    # If graph has 1 node, return the singular node as the IS
    if len(G.adj) == 1:
        return list(G.adj.keys())
    
    # If graph has 0 edges, return an empty IS
    if len(G.adj) == 0:
        return []

    # Get first node in the dictionary
    # Convert it to a list to access the nodes as indexes 
    getNodeKey = list(G.adj.keys())
    currentNode = first_node = getNodeKey[0] 
    
    # Copy the current graph into another variable graph2
    graph2 = Graph(len(G.adj))
    graph2.adj = {}
    for k, v in G.adj.items():
        graph2.adj[k] = list(v)

    # Delete the current vertex from the max set
    del graph2.adj[currentNode]
    
    result1 = MIS(graph2)

    # Loop through the neighbours for the node
    for neighbour in G.adj[currentNode]:
        # If an adj node is detected, delete it from the graph
        if neighbour in graph2.adj:
            del graph2.adj[neighbour]

    result2 = [currentNode] + MIS(graph2)

    # Out of two results, the larger one is the max IS
    if len(result1) > len(result2):
        return result1
    return result2

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


# Sample graph for testing 
'''
g1 = Graph(4)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
'''
