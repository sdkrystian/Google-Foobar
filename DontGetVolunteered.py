board = [[0 for x in range(8)] for y in range(8)] 
move_x = [2, 2, -2, -2, 1, 1, -1, -1]
move_y = [-1, 1, 1, -1, 2, -2, 2, -2]

def answer(src, dst):
    num = 0
    for x in range(8):
        for y in range(8):
            board[x][y] = num
            num += 1
    coords_to = coords(src, dst)
    used = {}
    moves = []
    src_node = Node(coords_to[0], coords_to[1])
    dst_node = Node(coords_to[2], coords_to[3])
    moves.append(src_node)
    while len(moves) > 0:
        node = moves.pop(0)
        if (dst_node.equal(node)):
            return node.moves
        if (node not in used):
            used[node] = True
            for i in range(8):
                newx = node.x + move_x[i]
                newy = node.y + move_y[i]
                if (valid(newx, newy)):
                    new_node = Node(newx, newy)
                    new_node.moves = node.moves + 1
                    moves.append(new_node);
    return -1

def valid(x, y):
    return x < 8 and x >= 0 and y < 8 and y >= 0

def coords(src, dst):
    output = [0 for i in range(4)]
    for x in range(8):
        for y in range(8):
            if (src == board[x][y]):
                output[0] = x
                output[1] = y
            if (dst == board[x][y]):
                output[2] = x
                output[3] = y
    return output

class Node:

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y
        self.moves = 0

    def equal(self, other):
        return other.x == self.x and other.y == self.y