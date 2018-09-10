import pprint
pp = pprint.PrettyPrinter(indent=4)

def puzz_breadth_first(start,end):
    front = [[puzzle]]
    expanded = []
    expanded_nodes=0
    while front:
        i = 0
        for j in range(1, len(front)):    #minimum
            if len(front[i]) > len(front[j]):
                i = j
        path = front[i]         
        front = front[:i] + front[i+1:]
        endnode = path[-1]
        if endnode in expanded: continue
        for k in moves(endnode):
            if k in expanded: continue
            front.append(path + [k])
        expanded.append(endnode)
        expanded_nodes += 1
        if endnode == end: break
            
    print("Expanded nodes:",expanded_nodes)
    print ("Solution:")
    pp.pprint(path)

def puzz_astar(start,end):
    front = [[heuristic_2(start), start]] #optional: heuristic_1
    expanded = []
    expanded_nodes=0
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i+1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded: continue
        for k in moves(endnode):
            if k in expanded: continue
            newpath = [path[0] + heuristic_2(k) - heuristic_2(endnode)] + path[1:] + [k] 
            front.append(newpath)
            expanded.append(endnode)
        expanded_nodes += 1 
    print ("Expanded nodes:", expanded_nodes)
    print ("Solution:")
    pp.pprint(path)


def moves(mat): 
    output = []  
    m = eval(mat)
    i = 0
    while 0 not in m[i]:
        i += 1
    j = m[i].index(0); #looking for 0

    if i > 0:                                   
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
      output.append(str(m))
      m[i][j], m[i-1][j] = m[i-1][j], m[i][j]; 
      
    if i < 3:                                   
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
      output.append(str(m))
      m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:                                                      
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
      output.append(str(m))
      m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 3:                                   
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
      output.append(str(m))
      m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    return output

def heuristic_1(puzz):
    misplaced = 0
    compare = 1
    m = eval(puzz)
    for i in range(4):
        for j in range(4):
            if m[i][j] != compare:
                misplaced += 1
            compare += 1
            if(compare == 16): compare = 0
    return misplaced

def heuristic_2(puzz):
    distance = 0
    m = eval(puzz)          
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0: continue
            distance += abs(i - ((m[i][j]-1)/4)) + abs(j -  ((m[i][j]-1)%4));
    return distance

puzzle1 = str([[1,2,7,3],[5,6,11,4], [9,10,15,8],[13,14,12,0]])
puzzle2 = str([[5,1,7,3],[9,2,11,4], [13,6,15,8],[0,10,14,12]])
end = str([[1,2,3,4],[5,6,7,8], [9,10,11,12],[13,14,15,0]])
print("A*")
puzz_astar(puzzle1,end)
print("\n\nBFS")
puzz_breadth_first(puzzle1,end)
print("--------------------------")
print("A*")
puzz_astar(puzzle2,end)
print("\n\nBFS")
puzz_breadth_first(puzzle2,end)

