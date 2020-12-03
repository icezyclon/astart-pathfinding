import numba as nb

@ nb.njit()
def problem():

    # init
    openSet = set()

    openSet.add((0, 0))
    openSet.add((1, 0))
    openSet.add((2, 0))
    openSet.add((3, 0))
    openSet.add((4, 0))
    openSet.add((5, 0))
    openSet.add((6, 0))
    openSet.add((7, 0))
    openSet.add((8, 0))

    openSet.remove((2, 0))
    openSet.add((2, 1))
    openSet.remove((2, 1))
    openSet.remove((4, 0))
    openSet.add((5, 1))
    openSet.add((4, 1))
    openSet.remove((7, 0))
    openSet.add((8, 1))
    openSet.add((7, 1))
    openSet.add((6, 1))
    openSet.remove((8, 0))
    openSet.remove((1, 0))
    openSet.remove((0, 0))
    openSet.remove((5, 0))
    openSet.remove((6, 0))
    openSet.remove((3, 0))
    openSet.remove((7, 1))
    openSet.add((8, 2))
    openSet.add((7, 2))
    openSet.add((6, 2))
    openSet.remove((8, 1))
    openSet.remove((6, 1))
    openSet.add((5, 2))
    openSet.remove((4, 1))
    openSet.add((4, 2))
    openSet.remove((5, 1))
    openSet.remove((6, 2))
    openSet.add((7, 3))
    openSet.add((6, 3))
    openSet.add((5, 3))
    openSet.remove((7, 2))
    openSet.add((8, 3))
    openSet.remove((8, 2))
    openSet.remove((4, 2))
    openSet.add((4, 3))
    openSet.add((3, 3))
    openSet.remove((5, 2))
    openSet.remove((7, 3))
    openSet.add((8, 4))
    openSet.add((7, 4))
    print('About to check (6,4) in openSet')
    return (6, 4) in openSet


if __name__ == "__main__":
    print(problem())
    print('DONE')
