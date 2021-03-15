import brain
import random

class Dot:
    def __init__(self, brain):
        self.x = 100
        self.y = 550
        self.x_vel = 0
        self.y_vel = 0
        self.x_acc = 0
        self.y_acc = 0
        self.radius = 3
        self.max_speed = 10
        self.time_to_goal = 0
        self.dead = False
        self.brain = brain
        self.fitness = 0
        self.is_best = False
        self.color = [255,255,255]
        self.reached_goal = False
        self.checks_reached = []


    def move(self):
        if self.x_acc < 0:
            if not self.x_vel <= -self.max_speed:
                self.x_vel += self.x_acc
        if self.x_acc > 0:
            if not self.x_vel >= self.max_speed:
                self.x_vel += self.x_acc
        if self.y_acc < 0:
            if not self.y_vel <= -self.max_speed:
                self.y_vel += self.y_acc
        if self.y_acc > 0:
            if not self.y_vel >= self.max_speed:
                self.y_vel += self.y_acc
        self.x += self.x_vel
        self.y += self.y_vel


    def change_dir(self, time):
        self.x_acc = self.brain.choose_x(time)
        self.y_acc = self.brain.choose_y(time)


    def get_fitness(self, goal_x, goal_y):
        x_dist = abs(goal_x-self.x)
        y_dist = abs(goal_y-self.y)
        total_dist = (int((x_dist**2)+(y_dist**2)))**.5
        if self.reached_goal:
            self.fitness = 250000-(self.time_to_goal ** 2)
        else:
            self.fitness = 1500000/(total_dist ** 2)
        self.fitness = int(self.fitness)
        self.fitness += (500 * len(self.checks_reached))
        return self.fitness


    def check_goal(self, goal_x, goal_y, goal_radius): #has the dot reached the goal
        x_dist = abs(goal_x - self.x)
        y_dist = abs(goal_y - self.y)
        total_dist = (int((x_dist ** 2) + (y_dist ** 2))) ** .5
        if total_dist <= goal_radius:
            return True
        else:
            return False


    def birth(self): #creates new dot with same brain
        child_brain = self.brain.clone()
        baby = Dot(child_brain)
        #baby.color = self.color #color is genetic, allows you to see the genetic algorithim at work
        return baby