import dots
import brain
import random
import time
dot_count = 50
dirs = 2000
dots_list = []
pop = []

for i in range(dot_count): #first gen
    dot = dots.Dot(brain.Brain(dirs))
    dots_list.append(dot)


def choose_parents():
    #returns index of random parent, more likely to return those with higher fitness
    indexes_list = []
    parents_list = []
    for index in range(dot_count):
        dot = dots_list[index]
        for i in range(dot.fitness):
            indexes_list.append(index)
    for i in range(2,dot_count):
        par_index = random.choice(indexes_list)
        parents_list.append(par_index)
    return parents_list


def new_gen(): #creates new generation
    global dot_count
    new_list = []
    king = dots_list[find_king()].birth() #king lives on
    king.radius = 4
    king.color = [0, 255, 0]
    prince = dots_list[find_king()].birth() #king always has a child which is mutated
    new_list.append(king)
    new_list.append(prince)

    parents_list = choose_parents()
    print(len(parents_list))
    for i in range(dot_count-2):
        par_index = parents_list[i]
        parent = dots_list[par_index]
        new_list.append(parent.birth())
    return new_list


def find_king():
    best_fitness = 0
    for i in range(dot_count):
        if dots_list[i].fitness > best_fitness:
            best_fitness = dots_list[i].fitness
            best_index = i
    dots_list[best_index].is_best = True
    return best_index


def mutate_children():
    for i in range(1,dot_count):
        if not dots_list[i].is_best:
            dots_list[i].brain.mutate()