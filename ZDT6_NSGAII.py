# Solving SCH Problem using NSGAII
from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.operator import SBXCrossover, PolynomialMutation
from jmetal.util.termination_criterion import StoppingByEvaluations
from jmetal.util.observer import ProgressBarObserver, VisualizerObserver
from jmetal.lab.visualization import Plot, InteractivePlot
from jmetal.problem.multiobjective.zdt import ZDT6
if __name__ == '__main__':
  problem = ZDT6()
  max_evaluations = 20000
  algorithm = NSGAII(
    problem = problem,
    population_size = 100,
    offspring_population_size = 100,
    mutation=PolynomialMutation(probability=0.05, distribution_index=20),
    crossover=SBXCrossover(probability=1.0, distribution_index=20),
    termination_criterion=StoppingByEvaluations(max=max_evaluations)
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

  print('Algorithm (continuous problem): ' + algorithm.get_name())
  print('Problem: ' + problem.get_name())
  print('Computing time: ' + str(algorithm.total_computing_time))
