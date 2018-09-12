from node import *
import problem
import time

def idts(problem):
    import itertools
    nodesExplored = 0
    start_time = time.time()
    for max_depth in itertools.count():
        # dfs
        fringe = [Node(problem.initial)]
        while fringe:
            node = fringe.pop()
            if problem.goal_test(node.state):
                print("Nodes expanded:", nodesExplored)
                print("Time taken (ms):", (time.time() - start_time) * 1000)
                return node
            if nodesExplored >= 1000000:
                print("Nodes expanded:", nodesExplored)
                print("Time taken (ms):", (time.time() - start_time) * 1000)
                return None
            if node.depth < max_depth:
                nodesExplored += 1
                fringe.extend(node.expand(problem))
    
    return None
