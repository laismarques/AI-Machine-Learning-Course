
import numpy as np
class Node:
    def __init__(self, label, goal_distance):
        self.label = label
        self.visitaded = False
        self.adjacent = []
        self.goal_distance = goal_distance
    
    def add_adjacent(self, adjacent):
        self.adjacent.append(adjacent)

    def show_adjacent(self):
        for i in self.adjacent:
            print(i.vertex.label, i.distance)
    
class Adjacent:
    def __init__(self, vertex, distance):
        self.vertex = vertex
        self.distance = distance

        #New atribute 
        self.astar_distance = vertex.goal_distance + self.distance

class Graph:
    #straight line distance
    arad = Node('Arad', 366)
    zerind = Node('Zerind', 374)
    oradea = Node('Oradea', 380)
    sibiu = Node('Sibiu', 253)
    timisoara = Node('Timisoara', 329)
    lugoj = Node('Lugoj', 244)
    mehadia = Node('Mehadia', 241)
    dobreta = Node('Dobreta', 242)
    craiova = Node('Craiova', 160)
    rimnicu = Node('Rimnicu', 193)
    fagaras = Node('Fagaras', 178)
    pitesti = Node('Pitesti', 98)
    bucharest = Node('Bucharest', 0)
    giurgiu = Node('Giurgiu', 77)
    
    #real distance
    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad, 75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(pitesti, 138))
    craiova.add_adjacent(Adjacent(rimnicu, 146))

    rimnicu.add_adjacent(Adjacent(craiova, 146))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucharest, 101))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))