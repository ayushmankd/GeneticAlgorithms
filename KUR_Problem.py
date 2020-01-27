# Objective Functions
# Minimize f(x) = Summation(from i=1 to n-1)[-10exp(-0.2sqrt(xi^2 + xi+1 ^ 2))]
# Minimize g(x) = Summation(from i=1 to n)[mod[xi]^0.8 + 5sin(xi ^ 3)]
# n = 3
# No Constraints
# This Problem is Called KUR Problem
import math
from jmetal.core.problem import FloatProblem
from jmetal.core.solution import FloatSolution
class KUR_Problem(FloatProblem):
  def __init__(self):
    super(KUR_Problem, self).__init__()
    self.number_of_variables = 3
    self.number_of_objectives = 2
    self.number_of_constraints = 0

    self.obj_directions = [self.MINIMIZE, self.MINIMIZE]
    self.obj_labels = ['f(x)', 'g(x)']
    self.lower_bound = [-5.0 for i in range(self.number_of_variables)]
    self.upper_bound = [5.0 for i in range(self.number_of_variables)]

  def evaluate(self, solution: FloatSolution) -> FloatSolution:
    solution.objectives[0] = sum([(-10 * math.exp(-0.2 * math.sqrt((solution.variables[i]*solution.variables[i]) + (solution.variables[i+1]*solution.variables[i+1])))) for i in range(solution.number_of_variables - 1)])
    solution.objectives[1] = sum([(math.pow(abs(solution.variables[i]), 0.8) + (5 * math.sin(solution.variables[i]*solution.variables[i]*solution.variables[i]))) for i in range(solution.number_of_variables)])
    return solution
  def get_name(self):
    return "KUR Problem"