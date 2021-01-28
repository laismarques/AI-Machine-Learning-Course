import numpy as np
from Graph import *
from SortedList import *

class GreedySearch():
    def __init__(self, goal):
        self.goal = goal 
        self.find = False

    def search(self, current):
        print("----------")
        print("Current: {}".format(current.label))
        current.visitaded = True

        if current == self.goal:
            self.find = True
        else:
            sorted_list = SortedList(len(current.adjacent))

            for i in current.adjacent:
                if i.vertex.visitaded == False:
                    i.vertex.visitaded == True
                    sorted_list.add(i.vertex)
            sorted_list.show()

            if sorted_list.values[0] != None:
                self.search(sorted_list.values[0])


graph = Graph()
graph.arad.show_adjacent()
list = SortedList(5)
list.add(graph.arad)
list.add(graph.craiova)  
list.add(graph.bucharest) 
list.add(graph.dobreta)

list.show()
greedy_search = GreedySearch(graph.bucharest)
greedy_search.search(graph.arad)