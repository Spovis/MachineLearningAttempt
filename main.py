import pygame
import population

dots_are_alive = True #determines if any of the dots are still alive, used to stop the main loop
pygame.init()
win_width = 600
win_height = 600
black = [0,0,0]
white = [100,100,100]
red = [100, 0, 0]

window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('ML')
pygame.display.update()

#make goal
class Goal:
    def __init__(self):
        self.x = win_width/2
        self.y = 20
        self.radius = 5
goal = Goal()

#main loop
def main():
    time = 0
    global dots_are_alive
    while dots_are_alive:
        time += 1
        dots_are_alive = False #will be made true if any are alive
        pygame.time.wait(3)
        window.fill(black)
        pygame.draw.circle(window, red, [goal.x, goal.y], goal.radius)

        #draw dots
        for i in range(len(population.dots_list)):
            pygame.display.update()
            dot = population.dots_list[i-1]
            pygame.draw.circle(window, dot.color, [dot.x, dot.y], dot.radius)
            if not dot.dead:

                if not dot.check_goal(goal.x, goal.y):
                    dots_are_alive = True
                    dot.change_dir(time)
                    dot.move()
                else:
                    dot.dead = True
                    dot.time_to_goal = time
            elif dot.dead:
                dot.time_to_goal = time
            if not 1 <= dot.x <= win_width-1 or not 1 <= dot.y <= win_height-1:
                dot.dead = True



running = True
while running: #runs once per generation
    dots_are_alive = True
    main()
    for i in range(population.dot_count):
        dot = population.dots_list[i]
        dot.fitness = dot.get_fitness(goal.x,goal.y)



    population.dots_list = population.new_gen()
    if not dot.is_best:
        dot.brain.mutate()



pygame.quit()
quit()