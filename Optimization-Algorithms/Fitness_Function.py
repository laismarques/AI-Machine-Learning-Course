import six
import sys
sys.modules['sklearn.externals.six'] = six
import mlrose
from Problem_Representation import *
cities = [('Lisboa', 'LIS'),
           ('Madrid', 'MAD'),
           ('Paris', 'CDG'), 
           ('Dublin', 'DUB'), 
           ('Bruxelas', 'BRU'), 
           ('London', 'LHR')]

destination = 'FCO'
flights = {}
for i in open('flights.txt'):
    origin, destination, departure, arrive, price = i.split(',')
    flights.setdefault((origin, destination), [])
    flights[(origin, destination)].append((departure, arrive, int(price)))


def fitness_function(schedule):
    id_flight = -1
    total_price = 0

    for i in range(len(schedule)//2):

        origin = cities[i][1]
        id_flight += 1
        outward_flight = flights[(origin, destination)][schedule[id_flight]]
        total_price += outward_flight[2]
        id_flight += 1
        flight_back = flights[(destination, origin)][schedule[id_flight]]
        total_price += flight_back[2]
    return total_price
#schedule represents the city and the flight that the person wants, 
# so the first person lives in Lisboa and wants the tird flight of the day. 
schedule = [1,2, 3,2, 7,3, 6,3, 2,4, 5,3]
print(fitness_function(schedule))

fitness = mlrose.CustomFitness(fitness_function)

problem = mlrose.DiscreteOpt(length=12, fitness_fn= fitness, maximize= False, max_val=10)

##Hill Climb
#better_solution, better_cost = mlrose.hill_climb(problem, random_state = 0)
#print(better_solution, better_cost)

#show_flights(better_solution)

##Simulated Annealing
#better_solution, better_cost = mlrose.simulated_annealing(problem)
#print(better_solution, better_cost)

#Genetic Algorithm
better_solution, better_cost = mlrose.genetic_alg(problem, pop_size = 500, mutation_prob=0.2)
print(better_solution, better_cost)