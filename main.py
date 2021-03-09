import pygame
import population

dots_are_alive = True #determines if any of the dots are still alive, used to stop the main loop
pygame.init()
win_width = 600
win_height = 600
black = [0,0,0]
white = [100,100,100]
red = [100, 0, 0]
blue = [0,0,50]
grey = [20,20,20]
gen = 1
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(gen), True, blue, black)
textRect = text.get_rect()
textRect.center = (550,580)



window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('ML')
pygame.display.update()

#make goal
class Goal:
    def __init__(self):
        self.x = 300
        self.y = 20
        self.radius = 10
goal = Goal()


obstacles = []
class Obstacle:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        obstacles.append(self)

    def draw(self):
        shape = pygame.Rect(self.x-self.width/2,self.y-self.height/2,self.width,self.height)
        pygame.draw.rect(window,red,shape)

    def check_killed(self, dot_x, dot_y):
        if (self.x-(self.width/2))-3 <= dot_x <= (self.x+(self.width/2))+3 and (self.y-(self.height/2))-3 <= dot_y <= (self.y+(self.height/2))+3:
            return True
        else:
            return False
obstacles = []
ob = Obstacle(425,250,15,350)
obstacles.append(ob)
shape = pygame.Rect(ob.x-ob.width/2,ob.y-ob.height/2,ob.width,ob.height)

ob_ = Obstacle(175,350,15,350)
obstacles.append(ob_)
shape_ = pygame.Rect(ob_.x-ob_.width/2,ob_.y-ob_.height/2,ob_.width,ob_.height)


checkpoints = []
class Checkpoint:
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.dots_have_got = []
        checkpoints.append(self)
    def check_got(self, dot_x, dot_y):
        if (self.x - self.width/2 - 3) <= dot_x <= (self.x + self.width/2 + 3) and (self.y - self.height/2 - 3) <= dot_y <= (self.y + self.height/2 + 3):
            return True
        else:
            return False
    def draw(self):
        shape = pygame.Rect(self.x-self.width/2,self.y-self.height/2,self.width,self.height)
        pygame.draw.rect(window,grey,shape)
check = Checkpoint(300,300,90,15)



def map1():
    ob.x = 2000
    ob_.x = 2000
    check.x = 2000
def map2():
    ob.x = 200
    ob.y = 500
    ob.width = 400
    ob.height = 15

    ob_.x = 400
    ob_.y = 300
    ob_.width = 400
    ob_.height = 15

    ob__ = Obstacle(200,150,15,400)

    check.x = 300
    check.y = 400
    check.height = 185
    check.width = 15

    check_ = Checkpoint(200,225,135,15)
    check__ = Checkpoint(400,225,135,15)
    check___ = Checkpoint(400,555,95,15)
    check____ = Checkpoint(500,150,15,200)


map2()



#main loop
def main():
    time = 0
    global dots_are_alive
    while dots_are_alive:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        time += 1
        dots_are_alive = False #will be made true if any are alive
        window.fill(black)
        pygame.draw.circle(window, [0,0,200], [goal.x, goal.y], goal.radius)
        window.blit(text, textRect)


        for i in range(len(obstacles)):
            obstacles[i].draw()

        for i in range(len(checkpoints)):
            checkpoints[i].draw()


        #draw dots
        for i in range(len(population.dots_list)):
            pygame.display.update()
            dot = population.dots_list[i-1]
            pygame.draw.circle(window, dot.color, [dot.x, dot.y], dot.radius)
            if not 2 <= dot.x <= win_width-2 or not 2 <= dot.y <= win_height-2:
                dot.dead = True

            for check in range(len(checkpoints)):
                if checkpoints[check].check_got(dot.x,dot.y) and not dot in checkpoints[check].dots_have_got:
                    dot.checks_reached += 1
                    checkpoints[check].dots_have_got.append(dot)

            for i in range(len(obstacles)):
                if obstacles[i].check_killed(dot.x,dot.y):
                    dot.dead = True

            if not dot.dead:
                if not dot.check_goal(goal.x, goal.y):
                    dots_are_alive = True
                    dot.change_dir(time)
                    dot.move()
                else:
                    dot.dead = True
                    dot.reached_goal = True
                    dot.time_to_goal = time





running = True
while running: #runs once per generation
    dots_are_alive = True
    main()
    gen += 1
    for i in range(population.dot_count):
        dot = population.dots_list[i]
        dot.fitness = dot.get_fitness(goal.x,goal.y)


    population.find_king()
    population.dots_list = population.new_gen()
    population.mutate_children()


    text = font.render(str(gen), True, blue, black)

pygame.quit()
quit()