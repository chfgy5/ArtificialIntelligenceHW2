# Reference: https://github.com/aimacode/aima-python/blob/master/search.py

from node import *
import problem

def idts(problem):
    import itertools
    nodesExplored = 0

    for max_depth in itertools.count():
        # dfs
        frontier = [Node(problem.initial)]
        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            if nodesExplored > 1000000:
                return None
            if node.depth < max_depth:
                nodesExplored += 1
                frontier.extend(node.expand(problem))
    return None
