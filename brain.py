import random

class Brain:
    def __init__(self,dir_num):
        self.dir_num = dir_num
        self.randomize()


    def randomize(self):
        self.directions = []
        for i in range(self.dir_num):
            next_move = [random.randint(-2,2),random.randint(-2,2)]
            self.directions.append(next_move)


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


    def mutate(self):
        mutation_rate = 3
        for i in range(self.dir_num):
            rand = random.randint(1,100)
            new_dirs = [random.randint(-2,2), random.randint(-2,2)]
            if mutation_rate > rand:
                self.directions[i] = new_dirs


    def clone(self):
        child = Brain(self.dir_num)
        child.directions = self.directions
        return child
