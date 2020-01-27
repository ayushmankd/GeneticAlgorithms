# Objective Functions
# Minimize f(x) = 1 - exp(summation(i=1 to 3)[xi - 1/root(3)]^2)
# Minimize g(x) = 1 - exp(summation(i=1 to 3)[xi + 1/root(3)]^2)
# No Constraints
# This Problem is Called FON Problem
import math
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution
class FON_Problem(FloatProblem):
  def __init__(self):
    super(FON_Problem, self).__init__()
    self.number_of_variables = 3
    self.number_of_objectives = 2
    self.number_of_constraints = 0

    self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
    self.obj_labels = ['f(x)', 'g(x)']
    self.lower_bound = [-4.0 for i in range(self.number_of_variables)]
    self.upper_bound = [4.0 for i in range(self.number_of_variables)]

  def evaluate(self, solution: FloatSolution) -> FloatSolution:
    solution.objectives[0] = 1 - math.exp(-1 * sum([math.pow((solution.variables[i] - (1/math.sqrt(3))), 2.0) for i in range(self.number_of_variables)]))
    solution.objectives[1] = 1 - math.exp(-1 * sum([math.pow((solution.variables[i] + (1/math.sqrt(3))), 2.0) for i in range(self.number_of_variables)]))
    return solution
  def get_name(self):
    return "FON Problem"