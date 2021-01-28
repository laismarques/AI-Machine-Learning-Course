import numpy as np
from Graph import *
from AStar_Sorted import *

class AStar:
    def __init__(self, goal):
        self.goal = goal
        self.find = False

    def search(self, actual):
        print('-----------------')
        print('Actual: {}'.format(actual.label))
        actual.visitaded = True

        if actual == self.goal:
            self.find = True
        else:
            sorted_list = SortedList(len(actual.adjacent))
            for adjacent in actual.adjacent:
                if adjacent.vertex.visitaded == False:
                    adjacent.vertex.visitaded = True
                    sorted_list.add(adjacent)
            sorted_list.show()
        
            if sorted_list.values[0] != None:
                self.search(sorted_list.values[0].vertex)

graph = Graph()
list = SortedList(3)
list.add(graph.arad.adjacent[0])
list.add(graph.arad.adjacent[1])
list.add(graph.arad.adjacent[2])
list.show()
aStar = AStar(graph.bucharest)
aStar.search(graph.arad)