# ArtificialIntelligenceHW2

### Team
* Caleb Fagan
* Paul Thongmotai
* Song Vu

### Description
Iterative deepening tree search and depth first graph search are implemented using the Node and Problem class. The node class handles keeping track of parent, child and expanding itself, basically it handles the tree/graph structure so our search doesn't have to worry about that. The problem class handles goal testing and managing the 4x4 square, again so that our search algorithm doesn't have these details to worry about. Iterative deepening tree search uses a counter and depth first limited search. This is so that depth first search acts more like breadth first search without the memory issues. Depth first graph search is just depth first search, that doesn't expand the same node twice. These were both developed on a windows laptop using VS Code, python extension, to run and debug.

### Iterative Deepening Tree Search:
##### A)

* First 5 states:
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 15, 8], [13, 14, 12, 0]]
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 15, 0], [13, 14, 12, 8]]
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 15, 8], [13, 14, 0, 12]]
    * [[1, 2, 7, 3], [5, 6, 11, 0], [9, 10, 15, 4], [13, 14, 12, 8]]
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 0, 15], [13, 14, 12, 8]]
* Solution Sequence
    * ['LEFT', 'UP', 'UP', 'UP', 'RIGHT', 'DOWN', 'DOWN', 'DOWN']
* Nodes Expanded
    * 2705 Nodes
* Time Taken
    * 37.142 ms

##### B)

* First 5 states:
    * [[5, 1, 7, 3], [9, 2, 11, 4], [13, 6, 15, 8], [0, 10, 14, 12]]
    * [[5, 1, 7, 3], [9, 2, 11, 4], [0, 6, 15, 8], [13, 10, 14, 12]]
    * [[5, 1, 7, 3], [9, 2, 11, 4], [13, 6, 15, 8], [10, 0, 14, 12]]
    * [[5, 1, 7, 3], [0, 2, 11, 4], [9, 6, 15, 8], [13, 10, 14, 12]]
    * [[5, 1, 7, 3], [9, 2, 11, 4], [6, 0, 15, 8], [13, 10, 14, 12]]
* Solution Sequence
    * No solution found
* Nodes Expanded
    * 1,000,000 Nodes
* Time Taken
    * 12948.824 ms

### Depth First Graph Search:
##### A)

* First 5 states:
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 15, 8], [13, 14, 12, 0]]
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 15, 0], [13, 14, 12, 8]]
    * [[1, 2, 7, 3], [5, 6, 11, 0], [9, 10, 15, 4], [13, 14, 12, 8]]
    * [[1, 2, 7, 0], [5, 6, 11, 3], [9, 10, 15, 4], [13, 14, 12, 8]]
    * [[1, 2, 0, 7], [5, 6, 11, 3], [9, 10, 15, 4], [13, 14, 12, 8]]
* Solution Sequence
    * No solution found
* Nodes Expanded
    * 1,000,000 Nodes
* Time Taken
    * 18571.336 ms

##### B)

* First 5 states:
    * [[5, 1, 7, 3], [9, 2, 11, 4], [13, 6, 15, 8], [0, 10, 14, 12]]
    * [[5, 1, 7, 3], [9, 2, 11, 4], [0, 6, 15, 8], [13, 10, 14, 12]]
    * [[5, 1, 7, 3], [0, 2, 11, 4], [9, 6, 15, 8], [13, 10, 14, 12]]
    * [[0, 1, 7, 3], [5, 2, 11, 4], [9, 6, 15, 8], [13, 10, 14, 12]]
    * [[1, 0, 7, 3], [5, 2, 11, 4], [9, 6, 15, 8], [13, 10, 14, 12]]
<<<<<<< HEAD
* Solution Sequence
    * No solution found
* Nodes Expanded
    * 1,000,000 Nodes
* Time Taken
    * 18714.244 ms

--

Code referenced: https://github.com/aimacode/aima-python/blob/master/search.py
=======
    
 
### A* Search:
##### A)

* First 5 states:
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 15, 8], [13, 14, 12, 0]]
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 15, 8], [13, 14, 0, 12]]
    * [[1, 2, 7, 3], [5, 6, 11, 4], [9, 10, 0, 8], [13, 14, 15, 12]]
    * [[1, 2, 7, 3], [5, 6, 0, 4], [9, 10, 11, 8], [13, 14, 15, 12]]
    * [[1, 2, 0, 3], [5, 6, 7, 4], [9, 10, 11, 8], [13, 14, 15, 12]]
    
##### B)

* First 5 states:
    * [[5, 1, 7, 3], [9, 2, 11, 4], [13, 6, 15, 8], [0, 10, 14, 12]]
    * [[5, 1, 7, 3], [9, 2, 11, 4], [0, 6, 15, 8], [13, 10, 14, 12]]
    * [[5, 1, 7, 3], [0, 2, 11, 4], [9, 6, 15, 8], [13, 10, 14, 12]]
    * [[0, 1, 7, 3], [5, 2, 11, 4], [9, 6, 15, 8], [13, 10, 14, 12]]
    * [[1, 0, 7, 3], [5, 2, 11, 4], [9, 6, 15, 8], [13, 10, 14, 12]]
>>>>>>> cb483786ea561618069d2d01ac42687b906a3e00
