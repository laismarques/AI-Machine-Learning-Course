import numpy as np
from Graph import *

class SortedList:
    def __init__(self, size):
        self.size = size
        self.last_position = -1
        self.values = np.empty(self.size, dtype=object)
    # O(n)
    def show(self):
        if self.last_position == -1:
            print("The list is empty")
        else:
            for i in range( self.last_position + 1):
                print("[",i,"]", "-", self.values[i].vertex.label, "-", 
                self.values[i].distance, "-",
                self.values[i].vertex.goal_distance, "-",
                self.values[i].astar_distance)
    # O(n)
    def add(self, node):
        if self.last_position == self.size -1:
            print("The List is Full")
            return -1

        position = 0
        for i in range(self.last_position + 1):
            position = i
            if self.values[i].astar_distance > node.astar_distance:
                break
            if i == self.last_position:
                position = i + 1

        x = self.last_position
        while x >= position:
            self.values[x + 1] = self.values[x]
            x -=1
        self.values[position] = node
        self.last_position +=1