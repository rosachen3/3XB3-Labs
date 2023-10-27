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
    print(node)
    marked = {}
    predecessor = {}
    for i in G.adj:
        marked[i] = False
    for current_node in G.adj:
        if current_node != node: # to not include target node in the dictionary
            if not marked[current_node]:
                marked[current_node] = True
                path = DFS2(G, current_node, node)
                print("path from ", current_node, " to ", node, ": ", path) # to see the path from each node to the target node
                if path != []: # if a path exists
                    predecessor[current_node] = path[1]
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
    nodes = [i for i in range(G.get_size())]
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
# # you can even delete edges to test if our algos work

# print(G1.adj)
# print(DFS2(G1,1,2))
# print(DFS3(G1, 3))