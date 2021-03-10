import pygame
import population

dots_are_alive = True #determines if any of the dots are still alive, used to stop the main loop
pygame.init()
win_width = 600
win_height = 600
black = [0,0,0]
white = [100,100,100]
red = [100, 0, 0]
blue = [0,0,150]
grey = [20,20,20]
gen = 1
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(('Gen ' + str(gen)), True, blue, black)
textRect = text.get_rect()
textRect.center = (500,580)



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



def map1():
    pass
def map2():
    ob = Obstacle(250,300,15,200)
def map3():
    ob = Obstacle(425, 250, 15, 350)
    ob_ = Obstacle(175, 350, 15, 350)
    check = Checkpoint(300, 300, 85, 15)
def map4():

    ob = Obstacle(200,500,15,400)
    ob_ = Obstacle(400,300,15,400)
    ob__ = Obstacle(200,150,15,400)

    check = Checkpoint(280,400,185,15)
    check_ = Checkpoint(200,225,135,15)
    check__ = Checkpoint(360,225,135,15)
    check___ = Checkpoint(400,555,95,15)
    check____ = Checkpoint(500,150,15,200)

def map_choice():
    font = pygame.font.Font('freesansbold.ttf', 28)
    text = font.render('Which map would you like? 1, 2, 3, or 4', True, white, black)
    textRect = text.get_rect()
    textRect.center = (300, 300)

    choosing = True
    while choosing:
        window.blit(text, textRect)
        pygame.display.update()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_1:
                    map1()
                    choosing = False
                elif e.key == pygame.K_2:
                    map2()
                    choosing = False
                elif e.key == pygame.K_3:
                    map3()
                    choosing = False
                elif e.key == pygame.K_4:
                    map4()
                    choosing = False
map_choice()


#main loop
def main():
    time = 0
    global dots_are_alive
    while dots_are_alive:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()
        time += 1 #number of frames that have happened in that generation
        dots_are_alive = False #will be made true if any are alive
        window.fill(black)
        pygame.draw.circle(window, [0,0,200], [goal.x, goal.y], goal.radius)
        window.blit(text, textRect)


        for i in range(len(obstacles)):
            obstacles[i].draw()

        for i in range(len(checkpoints)):
            checkpoints[i].draw()


        #draw dots
        for i in range(len(population.dots_list)-1,0,-1): #iterates through each dot, finishes with king so you can see it
            dot = population.dots_list[i-1]
            pygame.draw.circle(window, dot.color, [dot.x, dot.y], dot.radius)

            if not 3 <= dot.x <= win_width-3 or not 3 <= dot.y <= win_height-3:
                dot.dead = True #kill dots that hit edge

            for check in range(len(checkpoints)): #check if they got a checkpoint
                if checkpoints[check].check_got(dot.x,dot.y) and not dot in checkpoints[check].dots_have_got:
                    dot.checks_reached += 1
                    checkpoints[check].dots_have_got.append(dot) #dont let them get credit for the same chackpoint multiple times

            for i in range(len(obstacles)): #check if they hit an obstacle
                if obstacles[i].check_killed(dot.x,dot.y):
                    dot.dead = True

            if not dot.dead:
                if not dot.check_goal(goal.x, goal.y):
                    dots_are_alive = True #means at least one dot is alive
                    dot.change_dir(time)
                    dot.move()
                else: #it has reached the goal
                    dot.dead = True
                    dot.reached_goal = True
                    dot.time_to_goal = time

        pygame.display.update()
        pygame.time.wait(10)




running = True
while running: #runs once per generation
    dots_are_alive = True
    main()
    gen += 1
    for i in range(population.dot_count):
        dot = population.dots_list[i]
        dot.get_fitness(goal.x,goal.y)

    population.find_king()
    population.dots_list = population.new_gen()
    population.mutate_children()

    text = font.render(('Gen ' +str(gen)), True, blue, black)

pygame.quit()
quit()