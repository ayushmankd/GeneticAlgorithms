# Objective Functions
# Minimize f(x) = x ^ 2 
# Minimize g(x) = (x - 2) ^ 2
# No Constraints
# This Problem is Called SCH Problem
import math
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution
class SCH_Problem(FloatProblem):
  def __init__(self):
    super(SCH_Problem, self).__init__()
    self.number_of_variables = 1
    self.number_of_objectives = 2
    self.number_of_constraints = 0

    self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
    self.obj_labels = ['f(x)', 'g(x)']
    self.lower_bound = [-2.0]
    self.upper_bound = [3.0]

  def evaluate(self, solution: FloatSolution) -> FloatSolution:
    solution.objectives[0] = math.pow(solution.variables[0], 2.0)
    solution.objectives[1] = math.pow(solution.variables[0] - 2, 2.0)
    return solution
  def get_name(self):
    return "SCH Problem"