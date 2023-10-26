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

def has_cycle(G):
    for startNode in G.adj:
        Q = deque([startNode])
        marked = {}
        predecessor = {}
        
        for node in G.adj:
            marked[node] = False

        while len(Q) != 0:
            current_node = Q.popleft()
            marked[current_node] = True

            for node in G.adj[current_node]:
                #Cycle found if adj node is marked and not the parent node
                if marked[node] and node != predecessor[current_node]:
                    return True  
                # Keep traversing through nodes if false
                if not marked[node]:
                    Q.append(node)
                    predecessor[node] = current_node

    return False  # No cycle found in the entire graph

def plotGraph(numNodesList, numRandomGraphs):

    for numNode in numNodesList: 
        cycleProbTotal = []
        numEdge = []
        maxNumEdgesForTest = numNode + 20

        for edge in range(0, maxNumEdgesForTest, 5):
            if edge > maxNumEdgesForTest:  # Ensure termination
                break        
            numEdge.append(edge)
            
            # Stores the probability for the current test 
            # (i.e. probability for running 10 tests with 100 edges each)
            cycleProbForCurrentTest = 0

            # Generate a certain number of random graphs for each test
            for graph in range(numRandomGraphs):
                G = create_random_graph(numNode, edge)
                if has_cycle(G) == True:
                    cycleProbForCurrentTest += 1

            # Number of graphs that had a cycle / total number of random graphs with X edges
            cycleProbForCurrentTest = cycleProbForCurrentTest / numRandomGraphs
            cycleProbTotal.append(cycleProbForCurrentTest)

        plot.plot(numEdge, cycleProbTotal, label=f"Graph With {numNode} Nodes")

    plot.xlabel('Number of Edges')
    plot.ylabel('Cycle Probability')
    plot.title('Cycle Probability vs. Number of Edges')
    plot.legend()
    plot.show()

numNodesList = [25, 50, 75, 100]
numRandomGraphs = 20  # Number of random graphs to create for each test

plotGraph(numNodesList, numRandomGraphs)

    

