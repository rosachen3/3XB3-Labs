from queue import PriorityQueue, Queue
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
    

def a_star(G,s,d,h):
    distance = {}
    pred = {}
    queue = PriorityQueue()
    queue.put((0, s))
    distance[s] = 0
    shortestPath = []
    nodes = list(G.adj.keys())
    
    while not queue.empty():
        priority, current = queue.get() 
        shortestPath.append(current)

        if (current == d): # If node reaches destination, shortest path is found
            break

        for neighbour in G.adj[current]:
            g_cost = distance[current] + G.w(current, 
            neighbour)
            h_value = h[neighbour]
            f_value = g_cost + h_value 
            # print('g cost: ', g_cost)
            # print('h value: ', h_value)
            # print('f value: ', f_value)
            
            if (neighbour not in distance) or (g_cost < distance[neighbour]): 
                distance[neighbour] = g_cost
                pred[neighbour] = current 
                queue.put((f_value, neighbour)) # Choose next current_value based on f_value

    return pred, shortestPath
   
###### Testing Code ######
# G = DirectedWeightedGraph()

# for i in range(6):
#     G.add_node(i)

# G.add_edge(0,1,1)
# G.add_edge(0,5,10)
# G.add_edge(1,3,1)
# G.add_edge(1,2,2)
# G.add_edge(2,4,5)
# G.add_edge(3,4,3)
# G.add_edge(3,5,4)
# G.add_edge(4,5,2)

# heuristic = {0: 5, 1: 3, 2: 4, 3: 2, 4: 6, 5: 0}
# print(a_star(G,0,5,heuristic))
