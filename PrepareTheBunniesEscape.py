import copy

moves_x = [1, -1, 0, 0]
moves_y = [0, 0, 1, -1]
maze_x = 0
maze_y = 0

def answer(map):
    global maze_x;
    global maze_y;
    maze_x = len(map)
    maze_y = len(map[0])
    new_path = path(copy.deepcopy(map))
    shortest = new_path if new_path > 0 else float('inf')
    for x in range(maze_x):
        for y in range(maze_y):
            new_maze = copy.deepcopy(map)
            if (new_maze[x][y] == 1):
                new_maze[x][y] = 0
                new_path = path(new_maze)
                if (new_path < shortest and new_path > 0):
                    shortest = new_path
            else:
                continue
    return int(shortest)


def path(_maze):
    moves = []
    _maze[0][0] = "X"
    moves.append(Node(0, 0, 1))
    while (moves):
        node = moves.pop(0)
        if (node.x == maze_x - 1 and node.y == maze_y - 1):
            return node.moves
        if (_maze[node.x][node.y] != 1):
            for i in range(len(moves_x)): 
                new_x = node.x + moves_x[i]
                new_y = node.y + moves_y[i]
                if (valid(new_x, new_y) and _maze[new_x][new_y] == 0):
                    _maze[new_x][new_y] = 'X'
                    new_node = Node(new_x, new_y, node.moves + 1)
                    moves.append(new_node)
                    
    return -1

def valid(_x, _y):
    return _x < maze_x and _x >= 0 and _y < maze_y and _y >= 0

class Node:
    def __init__(self, _x, _y, _moves):
        self.x = _x
        self.y = _y
        self.moves = _moves