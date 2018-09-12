from testcase import *
from problem import *
from iterative_deepening_tree_search import *
from depth_first_graph_search import *

problem1 = problem.Problem(test1, goal)
problem2 = problem.Problem(test2, goal)

node = idts(problem1)
if(node):
    print(node.solution())
else:
    print("No solution found")

node = idts(problem2)
if(node):
    print(node.solution())
else:
    print("No solution found")

node = dfgs(problem1)
if(node):
    print(node.solution())
else:
    print("No solution found")

node = dfgs(problem2)
if(node):
    print(node.solution())
else:
    print("No solution found")