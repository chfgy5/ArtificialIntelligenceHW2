from testcase import *
from problem import *
from iterative_deepening_tree_search import *
from depth_first_graph_search import *

problem1 = problem.Problem(test1, goal)
problem2 = problem.Problem(test2, goal)

node = idts(problem1)
if(node):
    print(*node.solution(), sep='\n')
else:
    print("No solution found")
print("\n")

node = idts(problem2)
if(node):
    print(*node.solution(), sep='\n')
else:
    print("No solution found")
print("\n")

node = dfgs(problem1)
if(node):
    print(*node.solution(), sep='\n')
else:
    print("No solution found")
print("\n")

node = dfgs(problem2)
if(node):
    print(*node.solution(), sep='\n')
else:
    print("No solution found")