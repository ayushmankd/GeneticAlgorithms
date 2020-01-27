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
class TSP(PermutationProblem):
  def __init__(self):
    super(TSP, self).__init__()
    # Example
    distance_matrix = [
      [0, 10, 15, 20],
      [10, 0, 35, 25],
      [15, 35, 0, 30],
      [20, 25, 30, 0]
    ]
    number_of_cities = 4
    # # # #
    self.distance_matrix = distance_matrix
    self.number_of_variables = number_of_cities
    self.number_of_objectives = 1
    self.number_of_constraints = 0
    
  def evaluate(self, solution: PermutationSolution) -> PermutationSolution:
    fitness = 0

    for i in range(self.number_of_variables - 1):
      x = solution.variables[i]
      y = solution.variables[i + 1]
      fitness += self.distance_matrix[x][y]

    first, last = solution.variables[0], solution.variables[-1]
    fitness += self.distance_matrix[first][last]

    solution.objectives[0] = fitness

    return solution

  def create_solution(self) -> PermutationSolution:
    new_solution = PermutationSolution(
      number_of_variables=self.number_of_variables,
      number_of_objectives=self.number_of_objectives
    )
    new_solution.variables = random.sample(range(self.number_of_variables), k=self.number_of_variables)

    return new_solution
  def get_name(self):
        return 'Symmetric TSP'
algorithm = GeneticAlgorithm(
  problem=TSP(),
  population_size=4,
  offspring_population_size=4,
  # To Get a Different Combination by swapping any two positions
  mutation=PermutationSwapMutation(1.0 / 4),
  # Partially Mapped Crossover
  # Basically, parent 1 donates a swath of genetic material and the
  # corresponding swath from the other parent is sprinkled about in the child. 
  # Once that is done, the remaining alleles are copied direct from parent 2.
  crossover=PMXCrossover(0.8),
  # Compare any two Selection and then select the fittest
  selection=BinaryTournamentSelection(
    MultiComparator(
      [FastNonDominatedRanking.get_comparator(),
      CrowdingDistance.get_comparator()]
    )
  ),
  termination_criterion=StoppingByEvaluations(max=250)
)
algorithm.observable.register(observer=PrintObjectivesObserver(10))

algorithm.run()
result = algorithm.get_result()
# print('Algorithm: {}'.format(algorithm.get_name()))
print('Solution: {}'.format(result.variables))
print('Fitness: {}'.format(result.objectives[0]))
# print('Computing time: {}'.format(algorithm.total_computing_time))
