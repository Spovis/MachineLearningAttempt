import dots
import brain
import random
import time
dot_count = 500 #number dots in each gen
dirs = 1000 #number of directions in the brain
dots_list = [] #will contain all the dot objects


for i in range(dot_count): #first gen
    dot = dots.Dot(brain.Brain(dirs))
    dot.brain.randomize()
    dots_list.append(dot)


def choose_parents():
    #returns list of parents' indexes, more likely to choose ones with higher fitness
    indexes_list = []
    fitnesses_list = []
    parents_list = []
    for index in range(dot_count):
        dot = dots_list[index]
        fitnesses_list.append(dot.fitness)
        indexes_list.append(index)
    parents_list = random.choices(indexes_list,weights=fitnesses_list,k=(dot_count-2))
    return parents_list


def new_gen(): #creates new generation
    global dot_count
    new_list = []
    king = dots_list[find_king()].birth() #king lives on
    #king.color = [255,20,20]
    king.radius = 5
    prince = dots_list[find_king()].birth() #king always has a child which is mutated
    new_list.append(king)
    new_list.append(prince)

    parents_list = choose_parents()[:]
    for i in range(dot_count-2):
        par_index = parents_list[i]
        parent = dots_list[par_index]
        new_list.append(parent.birth())
    return new_list


def find_king():
    #returns index of dot with highest fitness
    best_fitness = 0
    for i in range(dot_count):
        if dots_list[i].fitness > best_fitness:
            best_fitness = dots_list[i].fitness
            best_index = i
    dots_list[best_index].is_best = True
    return best_index


def mutate_children(): #mutates entire generation, except the king
    for i in range(1,dot_count):
        if not dots_list[i].is_best:
            dots_list[i].brain.mutate()
