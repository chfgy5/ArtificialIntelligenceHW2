from node import *
import problem

def idts(problem):
    import itertools

    def dfs(problem, max_depth):
        frontier = [Node(problem.initial)]  # Stack

        while frontier:
            node = frontier.pop()
            if problem.goal_test(node.state):
                return node
            if node.depth < max_depth:
                frontier.extend(node.expand(problem))
        return None

    for depth in itertools.count():
        node = dfs(problem, depth)
        if node:
            return node
