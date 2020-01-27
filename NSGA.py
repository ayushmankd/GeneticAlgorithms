from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution
from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.util.observer import ProgressBarObserver, VisualizerObserver
from jmetal.util.solutions import print_function_values_to_file, print_variables_to_file, read_solutions
from jmetal.util.solutions.comparator import DominanceComparator
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.lab.visualization import Plot, InteractivePlot
from jmetal.operator import SBXCrossover, PolynomialMutation
import random
# To Define The Problem and Solution
from jmetal.core.problem import PermutationProblem
from jmetal.core.solution import PermutationSolution
# To Use Genetic Algorithm
from jmetal.algorithm.singleobjective.genetic_algorithm import GeneticAlgorithm
from jmetal.operator import BinaryTournamentSelection
from jmetal.operator.crossover import PMXCrossover
from jmetal.operator.mutation import PermutationSwapMutation
from jmetal.problem.singleobjective.tsp import TSP
from jmetal.util.density_estimator import CrowdingDistance
from jmetal.util.observer import PrintObjectivesObserver
from jmetal.util.ranking import FastNonDominatedRanking
from jmetal.util.solutions.comparator import MultiComparator
from jmetal.util.termination_criterion import StoppingByEvaluations
class NSGA(PermutationProblem):
  def __init__(self):
    super(NSGA, self).__init__()
    # Example
    distance_matrix = [
      [0, 23, 25, 15, 17],
      [23, 0, 36, 9, 18],
      [25, 36, 0, 23, 4],
      [15, 9, 23, 0, 16],
      [17, 18, 4, 16, 0]
    ]
    cost_matrix = [
      [0, 30, 13, 6, 24],
      [30, 0, 18, 8, 19],
      [13, 18, 0, 22, 42],
      [6, 8, 22, 0, 21],
      [24, 19, 42, 21, 0]
    ]
    number_of_cities = 5
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
  max_evaluations = 10000
  algorithm = NSGAII(
    problem=problem,
    population_size=2,
    offspring_population_size=2,
    mutation=PermutationSwapMutation(probability=1.0 / 6),
    crossover=PMXCrossover(probability=0.5),
    # crossover=PMXCrossover(0.8),
    termination_criterion=StoppingByEvaluations(max=max_evaluations),
    # dominance_comparator=DominanceComparator()
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
