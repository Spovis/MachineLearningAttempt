import random
seed = 1

class Brain:
    def __init__(self,dir_num):
        self.dir_num = dir_num #number of directions in the brain
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


    def mutate(self): #not working properly
        global seed
        mutation_rate = 3
        for i in range(self.dir_num):
            seed += 1
            random.seed(seed)
            rand = random.randint(1,100)
            seed += 1
            random.seed(seed)
            new_x = random.randint(-2,2)
            seed += 1
            random.seed(seed)
            new_y = random.randint(-2,2)
            new_dirs = [new_x,new_y]
            print(new_x, new_y)
            if mutation_rate > rand:
                self.directions[i] = new_dirs


    def clone(self): #returns exact copy of brain
        child = Brain(self.dir_num)
        child.directions = self.directions
        return child
