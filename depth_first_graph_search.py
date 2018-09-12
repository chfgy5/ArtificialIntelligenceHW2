from node import *
import problem
import time

def dfgs(problem):
    fringe = [(Node(problem.initial))]  # Stack
    closed = set()
    start_time = time.time()
    while fringe:
        node = fringe.pop()
        if problem.goal_test(node.state):
            print("Nodes expanded:", closed.__len__())
            print("Time taken (ms):", (time.time() - start_time) * 1000)
            return node
        if closed.__len__() >= 1000000:
            print("Nodes expanded:", closed.__len__())
            print("Time taken (ms):", (time.time() - start_time) * 1000)
            break
        if(node.state not in closed):
            closed.add(node.state)
            fringe.extend(node.expand(problem))
    
    return None