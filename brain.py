import random
seed = 1

class Brain:
    def __init__(self,dir_num):
        self.dir_num = dir_num #number of directions in the brain
        self.randomize()


    def randomize(self):
        self.directions = []
        for i in range(self.dir_num):
            next_move = [random.randint(-1,1),random.randint(-1,1)]
            self.directions.append(next_move)


    def choose_x(self, time): #returns x acceleration
        if len(self.directions) > time:
            x_acc = self.directions[time][0]
            return x_acc
        else:
            print('out of directions')
            return 0


    def choose_y(self, time): #returns y acceleration
        if len(self.directions) > time:
            y_acc = self.directions[time][1]
            return y_acc
        else:
            return 0


    def mutate(self): #changes brain slightly
        global seed
        mutation_rate = 2
        for i in range(self.dir_num):
            rand = random.randint(1,100)
            new_x = random.randint(-1,1)
            new_y = random.randint(-1,1)
            new_dirs = [new_x, new_y]
            if mutation_rate >= rand:
                self.directions[i] = [new_x, new_y][:]


    def clone(self): #returns exact copy of brain
        child = Brain(self.dir_num)
        child.directions = self.directions[:]
        return child
