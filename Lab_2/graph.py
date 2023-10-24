from collections import deque

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

#BFS2 - Returning the path from node1 to node2 in a list
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

def BSF3(G, node1):
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

'''
# ***** Example Graph Generation for BFS2 ***** #
g1 = Graph(6)
g1.add_edge(0,1)
g1.add_edge(1,3)
g1.add_edge(3,5)
g1.add_edge(0,2)
g1.add_edge(2,4)
g1.add_edge(2,3)
g1.add_edge(3,4)

print(BSF3(g1, 1))
'''


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
    nodes = [i for i in range(G.get_size())]
    subsets = power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(min_cover):
                min_cover = subset
    return min_cover


