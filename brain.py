import random
import numpy as np

class Brain:
    def __init__(self,dir_num):
        self.dir_num = dir_num #number of directions in the brain
        self.directions = []
        self.choices = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,0],[0,1],[1,-1],[1,0],[1,1]]


    def randomize(self):
        for i in range(self.dir_num):
            self.directions.append(random.choice(self.choices))


    def choose_x(self, time): #returns x acceleration
        if len(self.directions) > time:
            x_acc = self.directions[time][0]
            return x_acc
        else:
            return 0


    def choose_y(self, time): #returns y acceleration
        if len(self.directions) > time:
            y_acc = self.directions[time][1]
            return y_acc
        else:
            return 0


    def mutate(self): #changes brain slightly
        mutation_rate = .01
        for i in range(self.dir_num):
            rand = random.random()
            if mutation_rate >= rand:
                self.directions[i] = [random.randint(-1,1),random.randint(-1,1)][:]


    def clone(self): #returns exact copy of brain
        child = Brain(self.dir_num)
        child.directions = self.directions[:]
        return child
