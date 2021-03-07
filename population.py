import dots
import brain
import random
dot_count = 30
dirs = 100
dots_list = []
pop = []
fitnesses = []

for i in range(dot_count):
    dot = dots.Dot(brain.Brain(dirs))
    dots_list.append(dot)


def choose_parent():
    #returns index of random parent, more likely to return those with higher fitness
    indexes_list = []
    for index in range(dot_count):
        dot = dots_list[index]

        for i in range(dot.fitness):
            indexes_list.append(index)
    par_index = random.choice(indexes_list)

    return par_index





def new_gen():
    global dot_count
    new_list = []
    for i in range(dot_count):
        par_index = choose_parent()
        parent = dots_list[par_index]
        new_list.append(parent.birth())
        
    return new_list




def find_king():
    best_fitness= 0
    for i in range(dot_count):
        if dots_list[i].fitness > best_fitness:
            dots_list[i].is_best = True
        else:
            dots_list[i].is_best = False

