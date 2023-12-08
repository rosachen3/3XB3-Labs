import copy
from queue import PriorityQueue
import matplotlib.pyplot as plot
import min_heap 
import random
import csv
import math

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


def createLondonCityGraph(): 
    # Create a graph to store the london city network
    G = DirectedWeightedGraph()
    path1 = 'Final _Project\Part3\london_connections.csv'
    path2 = 'Final _Project\Part3\london_stations.csv'

    # Open london_connections file to access data 
    with open(path1, mode='r') as file: 
        london_connections = csv.reader(file)
         
        for row in london_connections:
            station1 = row[0]
            station2 = row[1]

            # Add nodes in the graph
            if station1 not in G.adj:
                G.add_node(station1)
            if station2 not in G.adj:
                G.add_node(station2)
        
            # Open london_stations file
            with open(path2, mode='r') as file2:
                london_stations = csv.reader(file2)
                lat1 = 0
                lat2 = 0
                long1 = 0
                long2 = 0

                for entry in london_stations: 
                    if entry[0] == station1:    # Find latitude/ longitude of each station by node number
                        lat1 = float(entry[1])
                        long1 = float(entry[2])
                    if entry[0] == station2:
                        lat2 = float(entry[1])
                        long2 = float(entry[2])
                
                weight = distanceBetweenStations(lat1, long1, lat2, long2)    # The weight between nodes will be the distance between stations 
                G.add_edge(station1, station2, weight)
    return G

def distanceBetweenStations(lat1, long1, lat2, long2):
    # Use Pythagorean to calculate distance
    distance = ((lat2-lat1)**2 + (long2-long1)**2) **(1/2)
    return distance


def buildHeuristic(G, destination):
    heuristic = {}
    path1 = 'Final _Project\Part3\london_connections.csv'
    path2 = 'Final _Project\Part3\london_stations.csv'
    # Open london_connections file to access data 
    heuristic[destination] = 0

    with open(path1, mode='r') as file: 
        with open(path2, mode='r') as file2:
            london_connections = csv.reader(file)
            london_stations = csv.reader(file2)
            next(london_stations)
            lat1 = 0
            long1 = 0

            # Compute latitude and longitude of destination node
            print("Destination: ", destination) 
            for entry in london_stations:
                if int(entry[0]) == destination:    # Find latitude/ longitude of destination node
                    lat1 = float(entry[1])
                    long1 = float(entry[2])
                
                # Determine the distance from each node to the destination node
                else:
                    lat2 = float(entry[1])
                    long2 = float(entry[2])
                    h_value = distanceBetweenStations(lat1,long1,lat2,long2)
                    heuristic[entry[0]] = h_value 
    return heuristic

G = createLondonCityGraph()
h = buildHeuristic(G,1)


