# Objective Functions
# Minimize f(x) = 1 + (A1-B1) ^ 2 + (A2-B2) ^ 2
# Minimize g(x) = (x1+3) ^ 2 + (x2+1) ^ 2
# A1 = 0.5sin1 - 2cos1 + sin2 - 1.5cos2
# A2 = 1.5sin1 - cos1 + 2sin2 - 0.5cos2
# B1 = 0.5sinx1 - 2cosx1 + sinx2 - 1.5cosx2
# B2 = 1.5sinx1 - cosx1 + 2sinx2 - 0.5cosx2
# No Constraints
# This Problem is Called POL Problem
import math
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution
class POL_Problem(FloatProblem):
  def __init__(self):
    super(POL_Problem, self).__init__()
    self.number_of_variables = 2
    self.number_of_objectives = 2
    self.number_of_constraints = 0

    self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
    self.obj_labels = ['f(x)', 'g(x)']
    self.lower_bound = [-1 * math.pi for i in range(self.number_of_variables)]
    self.upper_bound = [math.pi for i in range(self.number_of_variables)]

  def evaluate(self, solution: FloatSolution) -> FloatSolution:
    x1 = solution.variables[0]
    x2 = solution.variables[1]
    A1 = 0.5 * math.sin(1) - 2 * math.cos(1) + math.sin(2) - 1.5 * math.cos(2)
    B1 = 0.5 * math.sin(x1) - 2 * math.cos(x1) + math.sin(x2) - 1.5 * math.cos(x2)
    A2 = 1.5 * math.sin(1) - 2 * math.cos(1) + math.sin(2) - 0.5 * math.cos(2)
    B2 = 1.5 * math.sin(x1) - 2 * math.cos(x1) + math.sin(x2) - 0.5 * math.cos(x2)
    solution.objectives[0] = 1 + math.pow((A1-B1), 2.0) + math.pow((A2-B2), 2.0)
    solution.objectives[1] = math.pow((x1 + 3), 2.0) + math.pow((x2+1), 2.0)
    return solution
  def get_name(self):
    return "POL Problem"