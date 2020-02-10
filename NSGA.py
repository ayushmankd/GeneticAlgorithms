from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.util.observer import ProgressBarObserver, VisualizerObserver
from jmetal.util.solutions import print_function_values_to_file, print_variables_to_file, read_solutions
from jmetal.util.solutions.comparator import DominanceComparator
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.lab.visualization import Plot, InteractivePlot
import random
# To Define The Problem and Solution
from jmetal.core.problem import PermutationProblem
from jmetal.core.solution import PermutationSolution
# To Use Genetic Algorithm
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import BinaryTournamentSelection
from jmetal.operator.crossover import PMXCrossover, Order1Crossover
from jmetal.operator.mutation import PermutationSwapMutation
from jmetal.util.density_estimator import CrowdingDistance
from jmetal.util.observer import PrintObjectivesObserver
from jmetal.util.ranking import FastNonDominatedRanking
from jmetal.util.solutions.comparator import MultiComparator
from jmetal.util.termination_criterion import StoppingByEvaluations
from CreateMatrix import CreateMatrix
class NSGA(PermutationProblem):
  def __init__(self):
    super(NSGA, self).__init__()
    # Example
    distance_matrix = [
      [0, 81, 72, 55, 81, 3],
      [81, 0, 3, 44, 9, 40],
      [72, 3, 0, 87, 72, 21],
      [55, 44, 87, 0, 67, 25],
      [81, 9, 77, 67, 0, 93],
      [3, 40, 21, 25, 93, 0]
    ]
    cost_matrix = [
      [0, 82, 14, 14, 43, 47],
      [82, 0, 61, 76, 29, 47],
      [14, 61, 0, 29, 31, 51],
      [14, 76, 29, 0, 78, 67],
      [43, 29, 31, 78, 0, 28],
      [47, 47, 51, 67, 28, 0]
    ]
    # distance_matrix = CreateMatrix('kroA100.tsp')
    # cost_matrix = CreateMatrix('kroB100.tsp')
    number_of_cities = len(distance_matrix[0])
    # # # #
    self.distance_matrix = distance_matrix
    self.cost_matrix = cost_matrix
    self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
    self.obj_labels = ['Distance', 'Cost']
    self.number_of_objectives = 2
    self.number_of_variables = number_of_cities
    self.number_of_constraints = 0
    
  def evaluate(self, solution: PermutationSolution) -> PermutationSolution:
    distance_fitness = 0
    cost_fitness = 0

    for i in range(self.number_of_variables - 1):
      x = solution.variables[i]
      X = solution.variables[i]
      y = solution.variables[i + 1]
      Y = solution.variables[i + 1]
      distance_fitness += self.distance_matrix[x][y]
      cost_fitness += self.cost_matrix[X][Y]

    first, last = solution.variables[0], solution.variables[-1]
    First, Last = solution.variables[0], solution.variables[-1]
    distance_fitness += self.distance_matrix[first][last]
    cost_fitness += self.cost_matrix[First][Last]

    solution.objectives[0] = distance_fitness
    solution.objectives[1] = cost_fitness

    return solution

  def create_solution(self) -> PermutationSolution:
    new_solution = PermutationSolution(
      number_of_variables=self.number_of_variables,
      number_of_objectives=self.number_of_objectives
    )
    new_solution.variables = random.sample(range(self.number_of_variables), k=self.number_of_variables)

    return new_solution
  def get_name(self):
        return 'MultiObjective TSP'
if __name__ == '__main__':
  problem = NSGA()
  max_evaluations = 20000
  algorithm = NSGAII(
    problem=problem,
    population_size=20,
    offspring_population_size=20,
    mutation=PermutationSwapMutation(probability=0.2),
    # crossover=PMXCrossover(probability=0.9),
    crossover=Order1Crossover(probability=0.9),
    termination_criterion=StoppingByEvaluations(max=max_evaluations),
  )
  algorithm.observable.register(observer=ProgressBarObserver(max=max_evaluations))
  algorithm.observable.register(observer=VisualizerObserver(reference_front=problem.reference_front))

  algorithm.run()
  front = algorithm.get_result()

  # Plot front
  plot_front = Plot(plot_title='Pareto front approximation', reference_front=problem.reference_front, axis_labels=problem.obj_labels)
  plot_front.plot(front, label=algorithm.label, filename=algorithm.get_name())

  # Plot interactive front
  plot_front = InteractivePlot(plot_title='Pareto front approximation', reference_front=problem.reference_front, axis_labels=problem.obj_labels)
  plot_front.plot(front, label=algorithm.label, filename=algorithm.get_name())

  # Save results to file
  print_function_values_to_file(front, 'FUN.' + algorithm.label)
  print_variables_to_file(front, 'VAR.'+ algorithm.label)

  print('Algorithm (continuous problem): ' + algorithm.get_name())
  print('Problem: ' + problem.get_name())
  print('Computing time: ' + str(algorithm.total_computing_time))
