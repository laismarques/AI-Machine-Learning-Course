#Importing the necessary libarys
import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose

#Products that have in the first position the name, than the size in m³ and in the last position the price
catalog = [('A', 0.751, 999.90),
            ('B', 0.0000899, 2199.12),
            ('C', 0.400, 4346.99),
            ('D', 0.200, 2999.90),
            ('E', 0.00350, 2499.90),
            ('F', 0.496,  199.90),
            ('G', 0.0424, 308.66),
            ('H', 0.0544, 429.90),
            ('I', 0.0319, 299.29),
            ('J', 0.635, 849.00),
            ('K', 0.870, 1199.89),
            ('L', 0.572, 3999.00),
            ('M', 0.290, 3999.90),
            ('N', 0.498, 1999.90)]

available_space = 3
#List of products that will go the mall
products = [0,1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1]

def fitness_function(products):
    sum_sizes = 0
    total_price = 0
    for i in range(len(products)):
        if products[i] != 0:
            sum_sizes += catalog[i][1]
            total_price += catalog[i][2]
    
    if sum_sizes > available_space:
        return 1
    
    return total_price
 

fitness = mlrose.CustomFitness(fitness_function)

problem = mlrose.DiscreteOpt(length=14, fitness_fn= fitness, maximize= True, max_val=2)

##Hill Climb
#better_solution, better_cost = mlrose.hill_climb(problem, random_state = 0)
#print(better_solution, better_cost)

#show_flights(better_solution)

##Simulated Annealing
#better_solution, better_cost = mlrose.simulated_annealing(problem)
#print(better_solution, better_cost)

#Genetic Algorithm
#better_solution, better_cost = mlrose.genetic_alg(problem, pop_size = 500, mutation_prob=0.2)
#print(better_solution, better_cost)