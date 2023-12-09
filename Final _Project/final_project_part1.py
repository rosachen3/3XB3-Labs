import copy
import timeit
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
    relaxation_count = {} #Relaxation count for each node dictionary

    #Initialize distances and relaxation counts
    for node in nodes:
        dist[node] = float("inf")
        relaxation_count[node] = 0
    dist[source] = 0

    #Meat of the algorithm
    for _ in range(k+1): # Running k iterations instead of V - 1
        for node in nodes:
            for neighbour in G.adj[node]:
                if dist[neighbour] > dist[node] + G.w(node, neighbour) and relaxation_count[neighbour] < k:
                    dist[neighbour] = dist[node] + G.w(node, neighbour)
                    pred[neighbour] = node
                    relaxation_count[neighbour] += 1
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
        
        bellman_ford_graph = bellman_ford_approx(G2_copy, 0, k)
        bellman_ford_shortest_distances = total_dist(bellman_ford_graph)
        bellmanFordDistancesList.append(bellman_ford_shortest_distances)
    plot.plot(relaxationsList, dijkstraDistancesList, label='Dijkstra Approximation')
    plot.plot(relaxationsList, bellmanFordDistancesList, label='Bellman Ford Approximation')
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
        kValue2 = 0
        dijkstra_shortest_distance = float('inf')
        bellman_ford_shortest_distance = float('inf')
        for k in range(node):
            dijkstra_graph = dijkstra_approx(G1_copy, 0, k)
            dijkstra_current_distance = total_dist(dijkstra_graph)

            bellman_ford_graph = bellman_ford_approx(G2_copy, 0, k)
            bellman_ford_current_distance = total_dist(bellman_ford_graph)

            if dijkstra_current_distance < dijkstra_shortest_distance: 
                dijkstra_shortest_distance = dijkstra_current_distance
                kValue1 = k
            
            if bellman_ford_current_distance < bellman_ford_shortest_distance: 
                bellman_ford_shortest_distance = bellman_ford_current_distance 
                kValue2 = k
        relaxationsList1.append(kValue1)
        relaxationsList2.append(kValue2)

    plot.plot(nodesList, relaxationsList1, label='Dijkstra Approximation')
    plot.plot(nodesList, relaxationsList2, label='Bellman Ford Approximation')
    plot.legend()
    plot.title('Number of Relaxations for Shortest Distance vs Number of Nodes')
    plot.xlabel('Number of nodes')
    plot.ylabel('Number of Relaxations for Shortest Distance')
    plot.show()

# Graph 3: Number of Relaxations for Shortest Distance vs Upper Edge Weight
def graph3():
    numNodes = 25
    numEdgeWeight = 50
    edgeWeightList = []
    relaxationsList1 = []
    relaxationsList2 = []

    for edgeWeight in range(1, numEdgeWeight): 
        edgeWeightList.append(edgeWeight)
        G = create_random_complete_graph(numNodes, edgeWeight)
        G1_copy = G.copy()
        G2_copy = G.copy()
        kValue1 = 0
        kValue2 = 0
        dijkstra_shortest_distance = float('inf')
        bellman_ford_shortest_distance = float('inf')
        for k in range(numNodes):
            dijkstra_graph = dijkstra_approx(G1_copy, 0, k)
            dijkstra_current_distance = total_dist(dijkstra_graph)

            bellman_ford_graph = bellman_ford_approx(G2_copy, 0, k)
            bellman_ford_current_distance = total_dist(bellman_ford_graph)

            if dijkstra_current_distance < dijkstra_shortest_distance: 
                dijkstra_shortest_distance = dijkstra_current_distance
                kValue1 = k
            
            if bellman_ford_current_distance < bellman_ford_shortest_distance: 
                bellman_ford_shortest_distance = bellman_ford_current_distance 
                kValue2 = k
        relaxationsList1.append(kValue1)
        relaxationsList2.append(kValue2)

    plot.plot(edgeWeightList, relaxationsList1, label='Dijkstra Approximation')
    plot.plot(edgeWeightList, relaxationsList2, label='Bellman Ford Approximation')
    plot.legend()
    plot.title('Number of Relaxations for Shortest Distance vs Edge Weight')
    plot.xlabel('Edge Density')
    plot.ylabel('Number of Relaxations for Shortest Distance')
    plot.show()
# graph1()
# graph2()
# graph3()

# G = DirectedWeightedGraph()
# G.add_node(0)
# G.add_node(1)
# G.add_node(2)
# G.add_node(3)
# G.add_node(4)

# G.add_edge(0, 1, -12)
# G.add_edge(4, 1, 4)
# G.add_edge(2, 4, 16)
# G.add_edge(1, 2, 1)
# G.add_edge(2, 3, 10)
# G.add_edge(3, 4, 20)
# G.add_edge(1, 3, 5)


# def exp_mystery(n):
#     times = [] #list of execution time for each list length
#     #list_lengths = [10, 50, 100, 300, 500]
#     # nodes = [1, 10, 100, 1000]
#     nodes = []
#     for i in range(1, 100):
#         total = 0
#         nodes.append(i)
#         for j in range(n):
#             G = create_random_complete_graph(i, 10)

#             start = timeit.default_timer()
#             mystery(G)
#             end = timeit.default_timer()
#             total += end - start

#         times.append(total/n)
#     return times, nodes

# outputs = exp_mystery(20)

# plot.loglog(outputs[1], outputs[0], base=10, linestyle='-', label='MysteryAlgorithm')
# plot.legend()
# plot.title('Mystery Algorithm Performance')
# plot.xlabel('Number of Nodes')
# plot.ylabel('Execution Time (seconds)')
# plot.show()


