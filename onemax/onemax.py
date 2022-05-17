import pygad
from random import randint

initial_pop = [[randint(0,1) for _ in range(10)]
        for _ in range(100)]
def fitness_func(solution,solution_idx):
    return sum(solution)

ga_instance = pygad.GA(num_generations=100,
        num_parents_mating=100,
        gene_type=int,
        initial_population=initial_pop,
        fitness_func=fitness_func)

ga_instance.run()
print(ga_instance.best_solution(ga_instance.last_generation_fitness))
