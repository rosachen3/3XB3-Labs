import copy
import matplotlib.pyplot as plot
import min_heap
import random

class DirectedWeightedGraph:

    def __init__(self):
        self.adj = {}
        self.weights = {}

    def are_connected(self, node1, node2):
        for neighbour in self.adj[node1]:
            if neighbour == node2:
                return True
        return False

    def adjacent_nodes(self, node):
        return self.adj[node]

    def add_node(self, node):
        self.adj[node] = []

    def add_edge(self, node1, node2, weight):
        if node2 not in self.adj[node1]:
            self.adj[node1].append(node2)
        self.weights[(node1, node2)] = weight

    def w(self, node1, node2):
        if self.are_connected(node1, node2):
            return self.weights[(node1, node2)]

    def number_of_nodes(self):
        return len(self.adj)
    
    #### Added this myself (may need to erase after because I'm not sure if we should be adding methods) ###
    def copy(self):
        # Create a deep copy of the current object
        new_graph = copy.deepcopy(self)
        return new_graph

def dijkstra(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return dist

def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relaxation_count = {} #Relaxation count for each node dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        if current_node not in relaxation_count:
            #Initiazlize relaxation_count to be 0 for each node
            relaxation_count[current_node] = 0 

        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                # Check that the relaxation count is <= k
                if relaxation_count[current_node] < k: 
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
                    relaxation_count[current_node] += 1 #Increase relaxation count by 1 for the current node
                
    return dist

def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relaxation_count = {} #Relaxation count for each node dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        if current_node not in relaxation_count:
            #Initiazlize relaxation_count to be 0 for each node
            relaxation_count[current_node] = 0 

        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                # Check that the relaxation count is <= k
                if relaxation_count[current_node] < k: 
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
                    relaxation_count[current_node] += 1 #Increase relaxation count by 1 for the current node
                
    return dist

def bellman_ford(G, source):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(G.number_of_nodes()):
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist

def total_dist(dist):
    total = 0
    for key in dist.keys():
        total += dist[key]
    return total

def create_random_complete_graph(n,upper):
    G = DirectedWeightedGraph()
    for i in range(n):
        G.add_node(i)
    for i in range(n):
        for j in range(n):
            if i != j:
                G.add_edge(i,j,random.randint(1,upper))
    return G


#Assumes G represents its nodes as integers 0,1,...,(n-1)
def mystery(G):
    n = G.number_of_nodes()
    d = init_d(G)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][j] > d[i][k] + d[k][j]: 
                    d[i][j] = d[i][k] + d[k][j]
    return d

def init_d(G):
    n = G.number_of_nodes()
    d = [[float("inf") for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if G.are_connected(i, j):
                d[i][j] = G.w(i, j)
        d[i][i] = 0
    return d

# ************* Part 1 - Shortest Path Approximations *************

def dijkstra_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    relaxation_count = {} #Relaxation count for each node dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())

    #Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    #Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key

        if current_node not in relaxation_count:
            #Initiazlize relaxation_count to be 0 for each node
            relaxation_count[current_node] = 0 

        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                # Check that the relaxation count is < k
                if relaxation_count[current_node] < k: 
                    Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                    pred[neighbour] = current_node
                    relaxation_count[current_node] += 1 #Increase relaxation count by 1 for the current node
                
    return dist

def bellman_ford_approx(G, source, k):
    pred = {} #Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {} #Distance dictionary
    nodes = list(G.adj.keys())

    #Initialize distances
    for node in nodes:
        dist[node] = float("inf")
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(k+1): # Running k iterations instead of V - 1
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour):
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
    return dist

# Graph: Total Shortest Distance vs Number of Relaxations
def graph1():
    numNodes = 25
    maxRelaxations = numNodes - 1
    relaxationsList = []
    dijkstraDistancesList = []
    bellmanFordDistancesList = []

    G = create_random_complete_graph(numNodes, 20)
    for k in range(maxRelaxations): 
        relaxationsList.append(k)
        G1_copy = G.copy()
        G2_copy = G.copy()

        dijkstra_graph = dijkstra_approx(G1_copy, 0, k)
        dijkstra_shortest_distances = total_dist(dijkstra_graph)
        dijkstraDistancesList.append(dijkstra_shortest_distances)
        
        # bellman_ford_graph = bellman_ford_approx(G2_copy, 0, k)
        # bellman_ford_shortest_distances = total_dist(bellman_ford_graph)
        # bellmanFordDistancesList.append(bellman_ford_shortest_distances)
    plot.plot(relaxationsList, dijkstraDistancesList, label='Dijkstra Approximation')
    # plot.plot(relaxationsList, bellmanFordDistancesList, label='Bellman Ford Approximation')
    plot.legend()
    plot.title('Total Shortest Distance vs Number of Relaxations')
    plot.xlabel('Number of relaxations')
    plot.ylabel('Total Shortest Distance')
    plot.show()

# Graph 2: Number of Relaxations for Shortest Distance vs Number of nodes
def graph2():
    numNodes = 25
    nodesList = []
    relaxationsList1 = []
    relaxationsList2 = []

    for node in range(numNodes): 
        nodesList.append(node)
        G = create_random_complete_graph(node, node*(node-1)/2)
        G1_copy = G.copy()
        G2_copy = G.copy()
        kValue1 = 0
        dijkstra_shortest_distance = float('inf')
        bellman_ford_shortest_distance = float('inf')
        for k in range(node):
            dijkstra_graph = dijkstra_approx(G1_copy, 0, k)
            dijkstra_current_distance = total_dist(dijkstra_graph)

            if dijkstra_current_distance < dijkstra_shortest_distance: 
                dijkstra_shortest_distance = dijkstra_current_distance
                kValue1 = k
            
        relaxationsList1.append(kValue1)

    plot.plot(nodesList, relaxationsList1, label='Dijkstra Approximation')
    plot.legend()
    plot.title('Number of Relaxations for Shortest Distance vs Number of Nodes')
    plot.xlabel('Number of nodes')
    plot.ylabel('Number of Relaxations for Shortest Distance')
    plot.show()

# graph1()
# graph2()


    


