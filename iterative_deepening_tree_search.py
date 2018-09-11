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
            nodesExplored += 1
            if problem.goal_test(node.state):
                return node
            if nodesExplored > 1000000:
                return None
            if node.depth < max_depth:
                frontier.extend(node.expand(problem))
    return None
