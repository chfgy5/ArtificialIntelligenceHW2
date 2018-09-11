from node import *
import problem

def dfgs(problem):
    nodesExplored = 0
    frontier = [(Node(problem.initial))]  # Stack
    explored = set()
    while frontier:
        node = frontier.pop()
        nodesExplored += 1
        if problem.goal_test(node.state):
            return node
        if nodesExplored > 1000000:
            break
        if(node.state not in explored):
            explored.add(node.state)
            frontier.extend(node.expand(problem))
    
    return None