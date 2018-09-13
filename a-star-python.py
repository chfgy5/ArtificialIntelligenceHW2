# Reference: https://en.wikipedia.org/wiki/A*_search_algorithm

import sys
import datetime

# Generate All posible moves for the input state
def moves(current_state): 
    output = []
    puzzle = eval(current_state)
    i = 0
    
    # Looking for zero in row
    while 0 not in puzzle[i]:
        i += 1
    j = puzzle[i].index(0); # Looking for zero in column

    if i > 0:                                   
        puzzle[i][j], puzzle[i-1][j] = puzzle[i-1][j], puzzle[i][j];  # move up
        # Add the result to output list
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i-1][j] = puzzle[i-1][j], puzzle[i][j]; 
      
    if i < 3:                                   
        puzzle[i][j], puzzle[i+1][j] = puzzle[i+1][j], puzzle[i][j]   # move down
        # Add the result to output list
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i+1][j] = puzzle[i+1][j], puzzle[i][j]

    if j > 0:                                                      
        puzzle[i][j], puzzle[i][j-1] = puzzle[i][j-1], puzzle[i][j]   # move left
        # Add the result to output list
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i][j-1] = puzzle[i][j-1], puzzle[i][j]

    if j < 3:                                   
        puzzle[i][j], puzzle[i][j+1] = puzzle[i][j+1], puzzle[i][j]   # move right
        # Add the result to output list
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i][j+1] = puzzle[i][j+1], puzzle[i][j]

    return output

# Heuristic function for A*
def heuristic_manhattan(current_state):
    distance = 0
    puzzle = eval(current_state)
    # Sum the total distance of each tile to its goal
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0: continue
            distance += abs(i - ((puzzle[i][j]-1)/4)) + abs(j -  ((puzzle[i][j]-1)%4));
    return distance

# Function to print the report of moving step
def print_move(previous, current):
    
    previous_puzzle = eval(previous)
    current_puzzle = eval(current)
    
    i = 0
    while 0 not in previous_puzzle[i]:
        i += 1
    j = previous_puzzle[i].index(0);
    
    if(i > 0 and current_puzzle[i-1][j] == 0):
        return "UP\t"
    elif(i < 3 and current_puzzle[i+1][j] == 0):
        return "DOWN\t"
    elif(j > 0 and current_puzzle[i][j-1] == 0):
        return "LEFT\t"
    elif(j < 3 and current_puzzle[i][j+1] == 0):
        return "RIGHT\t"

# Function to print the report
def report(path):
    for index, node in enumerate(path[1:]):
        if(index > 0):
            print(print_move(path[index],node), node)
        else:
            print("INITAIL\t", node)

# A* algorithm
def astar(start,end):
    # Add the input test case to the list
    queue = [[heuristic_manhattan(start), start]]
    expanded = []
    expanded_nodes=0
    
    # Loop to expand the node until the list is became empty
    while queue:
        i = 0
        # Looking for the best valule that calcuate from heuristic_manhattan and get its location
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j
        # Let the path equal to new value
        path = queue[i]
        # Remove that from the queue
        queue = queue[:i] + queue[i+1:]
        
        # Check the node with the goal
        endnode = path[-1]
        if endnode == end:
            break
        
        # To save memory, if the node is expanded then skip
        if endnode in expanded: continue
        
        # Generate all posible moving step for the current sttate
        for k in moves(endnode):
            # To save memory, if the node is expanded then skip
            if k in expanded: continue
                
            # Generate the new path for the tree for the next loop, and add it to the queue
            newpath = [path[0] + heuristic_manhattan(k) - heuristic_manhattan(endnode)] + path[1:] + [k]
            queue.append(newpath)
            # Also add it to expanded list to protect for doing it again
            if endnode not in expanded: expanded.append(endnode)
                
        expanded_nodes += 1 # count expanded nodes
        
        # Terminate the program when it has visited more than 1 million nodes
        if(expanded_nodes > 1000000):
            print("Solution not found!")
            sys.exit("The A* algorithm expands more than 1 million nodes.")
    
    print("First 5 nodes:")
    print(*expanded[:5], sep='\n')
    print("\nSolution found:")
    report(path)
    print ("\nTotal expanded nodes:", expanded_nodes)

def main():
    puzzle1 = str([[1,2,7,3],[5,6,11,4], [9,10,15,8],[13,14,12,0]])
    puzzle2 = str([[5,1,7,3],[9,2,11,4], [13,6,15,8],[0,10,14,12]])
    goal = str([[1,2,3,4],[5,6,7,8], [9,10,11,12],[13,14,15,0]])
    
    start = datetime.datetime.now()
    print("A*")
    astar(puzzle1,goal)
    stop = datetime.datetime.now()
    total = stop-start
    print('\nExecution time:',total.total_seconds() * 1000, 'ms')
    
    print("\n--------------------------\n")

    start = datetime.datetime.now()
    print("A*")
    astar(puzzle2,goal)
    stop = datetime.datetime.now()
    total = stop-start
    print('\nExecution time:',total.total_seconds() * 1000, 'ms')
    
if __name__ == '__main__':
    main()