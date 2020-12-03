import numba as nb
import numpy as np


@nb.njit()
def neighbors(board, pos):
    """pos in (x, y)"""
    height, width = board.shape
    x, y = pos  # col, row = x, y
    top = y > 0
    right = x < width - 1
    bot = y < height - 1
    left = x > 0
    if top and left:
        yield (x - 1, y - 1)
    if top:
        yield (x, y - 1)
    if top and right:
        yield (x + 1, y - 1)
    if right:
        yield (x + 1, y)
    if right and bot:
        yield (x + 1, y + 1)
    if bot:
        yield (x, y + 1)
    if bot and left:
        yield (x - 1, y + 1)
    if left:
        yield (x - 1, y)


@nb.njit()
def shortestPathLen(board, player):

    # init
    height, width = board.shape
    openSet = set()
    closedSet = set([(1, 2)])  # so numba can infer set type
    closedSet.clear()
    gScore = dict()
    fScore = dict()
    goal = set()
    h_dim = 0
    h_acc = 0

    def cost(val):
        if val == player:
            return 0
        # return 1 # WORKING?!?!?
        return 2

    def h(node):
        return h_dim - 1 - node[h_acc]

    # init for different players
    # find path with multiple starting and end nodes
    # player 1 wants a path horizontally and player 2 wants a path vertically
    if player == 1:
        h_dim = width
        h_acc = 0
        for row in range(height):
            node = (0, row)
            val = board[node[::-1]]
            if val == 0 or val == player:
                openSet.add(node)
                gScore[node] = cost(val)
                fScore[node] = gScore.get(node, 255) + h(node)
            node = (width-1, row)
            val = board[node[::-1]]
            if val == 0 or val == player:
                goal.add(node)
    elif player == 2:
        h_dim = height
        h_acc = 1
        for col in range(width):
            node = (col, 0)
            val = board[node[::-1]]
            if val == 0 or val == player:
                openSet.add(node)
                gScore[node] = cost(val)
                fScore[node] = gScore.get(node, 255) + h(node)
            node = (col, height-1)
            val = board[node[::-1]]
            if val == 0 or val == player:
                goal.add(node)

    # run A* path finding
    while openSet:

        # find element from openSet with minimum fScore
        current = (-1, -1)
        for o in openSet:
            if current == (-1, -1) or fScore.get(o, 255) < fScore.get(current, 255):
                current = o

        if current in goal:
            return gScore.get(current, 255)

        openSet.remove(current)
        closedSet.add(current)
        for neighbor in neighbors(board, current):
            val = board[neighbor[::-1]]
            if neighbor in closedSet:
                continue
            if val == 0 or val == player:
                possible_g = gScore.get(current, 255) + cost(val)
                if possible_g < gScore.get(neighbor, 255):
                    gScore[neighbor] = gScore.get(current, 255) + cost(val)
                    fScore[neighbor] = gScore.get(neighbor, 255) + h(neighbor)
                    print(openSet)
                    print(neighbor)
                    if neighbor in openSet:  # it seems like this call does not return
                        print('continue')
                        continue
                    print('adding')
                    openSet.add(neighbor)

    assert False, 'No shortest path found??'
    return -1


if __name__ == "__main__":
    b = np.zeros((8, 9), dtype=np.uint8)
    b[1, 0] = 1
    b[1, 1] = 1
    b[2, 1] = 1
    b[2, 2] = 1
    b[2, 3] = 1
    b[1, 3] = 1
    b[1, 3] = 1
    b[2, 0] = 2
    b[3, 0] = 2
    b[0, 2] = 2
    b[1, 2] = 2
    print(b)
    print(shortestPathLen(b, 2))
