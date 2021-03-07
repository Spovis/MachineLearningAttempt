import brain


class Dot:
    def __init__(self, brain):
        self.x = 100
        self.y = 400
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

    def move(self):
        if self.x_vel < self.max_speed:
            self.x_vel += self.x_acc
        if self.y_vel < self.max_speed:
            self.y_vel += self.y_acc
        self.x += self.x_vel
        self.y += self.y_vel


    def change_dir(self, time):
        self.x_acc = self.brain.choose_x(time)
        self.y_acc = self.brain.choose_y(time)

    def get_fitness(self, goal_x, goal_y):
        x_dist = abs(goal_x-self.x)
        y_dist = abs(goal_y-self.y)
        total_dist = int(x_dist+y_dist)
        if not total_dist == 0:
            self.fitness = 1000-total_dist-self.time_to_goal
        else:
            self.fitness = 2500-self.time_to_goal
        return self.fitness

    def check_goal(self, goal_x, goal_y):
        if goal_x-5 <= self.x <= goal_x+5 and goal_y-5 <= self.y <= goal_y+5:
            return True
        else:
            return False

    def birth(self):
        child_brain = self.brain.clone()
        baby = Dot(child_brain)
        return baby