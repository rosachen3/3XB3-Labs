from collections import deque
import random
import copy
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

#Breadth First Search
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

#**************** BREADTH FIRST SEARCH IMPLEMENTATIONS ****************************#
def BFS2(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    parent = {}
    path = []

    # If the initial 2 nodes you want to find the path for are the same, return an empty list
    if node1 == node2:
        return []
    
    # Initialize every node in the dictionary besides the start node to be False (Not marked)
    for node in G.adj:
        if node != node1:
            marked[node] = False

    # Run while there are numbers in the queue
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            #If in our search, we have reached the second node, trace the path backwards
            if node == node2:
                path = [node2]
                # Update the parent of the end node
                parent[node] = current_node
                while node2 != node1:
                    node2 = parent[node2]
                    path.insert(0, node2)
                return path
            # If the node has not been marked, mark it and change it's value in the dict to True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                parent[node] = current_node
    return []

def BFS3(G, node1):
    Q = deque([node1])
    marked = {node1 : True}
    predecessor = {}
    
    for node in G.adj:
        if node != node1:
            marked[node] = False

    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:        
            if not marked[node]:
                Q.append(node)
                marked[node] = True
                predecessor[node] = current_node
    return predecessor

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

def is_connected(G):
    # Use BFS to check if a path exists between all comb. of two nodes in a graph
    for node1 in G.adj: 
        for node2 in G.adj: 
            if node1 != node2 and BFS(G, node1, node2) == False:
                return False
    return True

#Depth First Search
def DFS(G, node1, node2):
    S = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

#**************** DEPTH FIRST SEARCH IMPLEMENTATIONS ****************************#
#Depth First Search 2
def DFS2(G, node1, node2):
    S = [node1]
    marked = {}
    path = []
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            marked[current_node] = True
            path.append(current_node) #adding node into path list
            for node in G.adj[current_node]:
                if node == node2:
                    path.append(node) #adding last node into path list
                    return path
                S.append(node)
    return []

#Depth First Search 3
def DFS3(G, node):
    S = [node]
    marked = {}
    predecessor = {}
    for i in G.adj:
        marked[i] = False
    while len(S) != 0:
        current_node = S.pop()
        for i in G.adj[current_node]:
            if not marked[i] and (i != node):
                S.append(i)
                marked[i] = True
                predecessor[i] = current_node
    return predecessor

#Use the methods below to determine minimum Vertex Covers
def add_to_each(sets, element):
    copy = sets.copy()
    for set in copy:
        set.append(element)
    return copy

def power_set(set):
    if set == []:
        return [[]]
    return power_set(set[1:]) + add_to_each(power_set(set[1:]), set[0])

def is_vertex_cover(G, C):
    for start in G.adj:
        for end in G.adj[start]:
            if not(start in C or end in C):
                return False
    return True

def MVC(G):
    nodes = [i for i in range(len(G.adj))]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover

##### the following is testing code #####
# G1 = Graph(6)
# G1.add_edge(0,1)
# G1.add_edge(1,3)
# G1.add_edge(3,5)
# G1.add_edge(0,2)
# G1.add_edge(2,3)
# G1.add_edge(2,4)
# G1.add_edge(4,3)
# you can even delete edges to test if our algos work

# print(G1.adj)
# print(DFS2(G1,1,2))
# print(DFS3(G1, 3))

#**************** PART TWO ****************************#

def approx1(G):
    C = set()
    while True:
        if is_vertex_cover(G, C):
            return C
        v = -1
        highest_deg = -1
        for i in G.adj:
            deg = len(G.adj[i])
            if deg > highest_deg:
                highest_deg = deg
                v = i
        C.add(v)
        G1 = copy.deepcopy(G)
        G1.adj[v] = []
        G = G1
    return C
    
def approx2(G):
    C = set()
    while not is_vertex_cover(G, C):
        while True:
            v = random.randint(0, len(G.adj)-1)
            if v not in C:
                break
        C.add(v)
    return C

def approx3(G):
    C = set()
    while not is_vertex_cover(G, C):
        u = random.randint(0, len(G.adj)-1)
        while (G.adj[u] == []):
            u = random.randint(0, len(G.adj)-1)
        v = random.choice(G.adj[u])
        
        C.add(u);C.add(v)
        G1 = copy.deepcopy(G)
        G1.adj[u] = []
        G1.adj[v] = []
    return C

##### the following is for testig purposes

# G1 = Graph(4)
# G1.add_edge(0,2)
# G1.add_edge(1,3)
# G1.add_edge(2,3)
# G1.add_edge(1,0)
# G1.add_edge(0,3)
# G1.add_edge(1,2)
# print(approx1(G1))
# print(approx2(G1))
# print(approx3(G1))
def approx_Exp():
    # edge_values = [1, 5, 10, 15, 20, 25]
    edge_values = []
    #declaring a list of expected performance for each edge value
    exp_performance1 = []
    exp_performance2 = []
    exp_performance3 = []
    #generating 1000 graphs for each value of edges
    for edges in range(1, 36, 2):
    # for edges in edge_values:
        mvc_sum = 0
        a1_sum = 0
        a2_sum = 0
        a3_sum = 0
        edge_values.append(edges)
        for i in range(1000):
            G = create_random_graph(9, edges)
            mvc_sum += len(MVC(G))

            # running each approximation on each of the same 1000 graphs
            vc1 = approx1(G)
            # updating sum variables
            a1_sum += len(vc1) 
            vc2 = approx2(G)
            a2_sum += len(vc2) 
            vc3 = approx3(G)
            a3_sum += len(vc3) 
            
        exp_performance1.append(a1_sum/mvc_sum)
        exp_performance2.append(a2_sum/mvc_sum)
        exp_performance3.append(a3_sum/mvc_sum)
    return exp_performance1, exp_performance2, exp_performance3, edge_values

outputs = approx_Exp()
print()
plot.plot(outputs[3], outputs[0], label='approx1')
plot.plot(outputs[3], outputs[1], label='approx2')
plot.plot(outputs[3], outputs[2], label='approx3')
plot.plot()
plot.legend()
plot.title('Expected Performance vs. Edges')
plot.xlabel('Edges')
plot.ylabel('Expected Performance')
plot.show()
