import sys
import datetime

def moves(current_state): 
    output = []  
    puzzle = eval(current_state)
    i = 0
    while 0 not in puzzle[i]:
        i += 1
    j = puzzle[i].index(0); #looking for 0

    if i > 0:                                   
        puzzle[i][j], puzzle[i-1][j] = puzzle[i-1][j], puzzle[i][j];  #move up
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i-1][j] = puzzle[i-1][j], puzzle[i][j]; 
      
    if i < 3:                                   
        puzzle[i][j], puzzle[i+1][j] = puzzle[i+1][j], puzzle[i][j]   #move down
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i+1][j] = puzzle[i+1][j], puzzle[i][j]

    if j > 0:                                                      
        puzzle[i][j], puzzle[i][j-1] = puzzle[i][j-1], puzzle[i][j]   #move left
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i][j-1] = puzzle[i][j-1], puzzle[i][j]

    if j < 3:                                   
        puzzle[i][j], puzzle[i][j+1] = puzzle[i][j+1], puzzle[i][j]   #move right
        output.append(str(puzzle))
        puzzle[i][j], puzzle[i][j+1] = puzzle[i][j+1], puzzle[i][j]

    return output

def heuristic_manhattan(current_state):
    distance = 0
    puzzle = eval(current_state)
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == 0: continue
            distance += abs(i - ((puzzle[i][j]-1)/4)) + abs(j -  ((puzzle[i][j]-1)%4));
    return distance

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

def report(path):
    for index, node in enumerate(path[1:]):
        if(index > 0):
            print(print_move(path[index],node), node)
        else:
            print("INITAIL\t", node)

def astar(start,end):
    queue = [[heuristic_manhattan(start), start]]
    expanded = []
    expanded_nodes=0
    while queue:
        i = 0
        for j in range(1, len(queue)):
            if queue[i][0] > queue[j][0]:
                i = j
        path = queue[i]
        queue = queue[:i] + queue[i+1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded: continue
        for k in moves(endnode):
            if k in expanded: continue
            newpath = [path[0] + heuristic_manhattan(k) - heuristic_manhattan(endnode)] + path[1:] + [k]
            queue.append(newpath)
            if endnode not in expanded: expanded.append(endnode)
        expanded_nodes += 1
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
    
    print("\n--------------------------\n")

    print("A*")
    astar(puzzle2,goal)

    stop = datetime.datetime.now()
    total = stop-start
    print('\nExecution time:',total.total_seconds() * 1000, 'ms')
    
if __name__ == '__main__':
    main()