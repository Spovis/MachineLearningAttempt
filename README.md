# MachineLearningAttempt
My first attempt at a very simple form of machine learning. Following the tutorial by codebullet, but I coded in python instead of what he used

The dots are each controlled by their own brain, which has a list of 2000 instructions for accelerations in the x y axis. Each generation, the dots that got closest to the goal
are more likely to be chosen to have children in the next generation. The children in the next generation are then slightly mutated. The best dot from each gen is put directly 
into the next generation, and is highlighted in green for comparason. this makes it easier to see progress in the generations. There are 4 maps included, which have obstacles and 
checkpoints. The dots immedialtly die if they touch the walls, obstacles, or goal. They are given a bonus to their fitness if they reach a checkpoint. 

Each of the maps is progressivly more complex, and it will take more generations to reach the goal on each one. 
