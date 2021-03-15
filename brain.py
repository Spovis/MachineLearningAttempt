import random
import itertools

#create a list of choices for the brain to choose from when randomizing
l = []
for i in range(-30,31):
    l.append(i/10)
choices = list(itertools.permutations(l, r=2))


r = []
for i in range(-15,16):
    r.append(i/10)
choices = list(itertools.permutations(l, r=2))


class Brain:
    def __init__(self,dir_num):
        self.dir_num = dir_num #number of directions in the brain
        self.directions = []


    def randomize(self):
        self.directions = random.choices(choices, k=self.dir_num)


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
                new_x = random.choice(l)
                new_y = random.choice(l)
                new_values = (new_x,new_y)
                self.directions[i] = new_values


    def clone(self): #returns exact copy of brain
        child = Brain(self.dir_num)
        child.directions = self.directions[:]
        return child
