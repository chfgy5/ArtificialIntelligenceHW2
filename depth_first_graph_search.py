from node import *
import problem

def dfgs(problem):
    frontier = [(Node(problem.initial))]  # Stack
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        if explored.__len__() > 1000000:
            break
        if(node.state not in explored):
            explored.add(node.state)
            frontier.extend(node.expand(problem))
    
    return None