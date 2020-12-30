def data_parser():
    """
    Parse out data in ../data/day11.txt
    Returns:
        dict: a dictionary mapping the connections. Each point on the 2-d grid is mapped to an int=num_row * row_len + num_col.
            The value is a list in the form of [curr_val, next_val, [list of connected vertices]].
    """
    file_path = '../data/day11.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    grid = [x.strip() for x in raw]
    nrow, ncol = len(grid), len(grid[0])
    out = {}
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] != '.':
                # neighbors
                index = i * ncol + j
                out[index] = [grid[i][j], grid[i][j], []]
                for x in range(max(0, i - 1), min(i + 2, nrow)):
                    for y in range(max(0, j - 1), min(j + 2, ncol)):
                        if not (x == i and y == j):
                            if grid[x][y] != '.':
                                out[index][2].append(x * ncol + y)
    return out


def data_parser_v2():
    """
    Part 2 of question where neighbors are defined as closest seat in each direction.
    Returns:
        dict: a dictionary mapping the connections. Each point on the 2-d grid is mapped to an int=num_row * row_len + num_col.
            The value is a list in the form of [curr_val, next_val, [list of connected vertices]].
    """
    file_path = '../data/day11.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    grid = [x.strip() for x in raw]
    nrow, ncol = len(grid), len(grid[0])
    out = {}
    for i in range(nrow):
        for j in range(ncol):
            if grid[i][j] != '.':
                # neighbors
                index = i * ncol + j
                out[index] = [grid[i][j], grid[i][j], []]
                neighbors = find_neighbors(grid, i, j)
                for x, y in neighbors:
                    out[index][2].append(x * ncol + y)
    return out


def find_neighbors(mat, i, j):
    """
    Given the seat map and seat loc (i, j), find its neighbors in all directions.
    Args:
        mat (list): list of str representing the seating map
        i, j (int): loc of the target seat.
    Returns:
        list: list of (x, y) for all neighbors for the target seat.
    """
    neighbors = []
    # top
    x = i - 1
    while x >= 0:
        if mat[x][j] != '.':
            neighbors.append((x, j))
            break
        x -= 1
    # bottom
    x = i + 1
    while x < len(mat):
        if mat[x][j] != '.':
            neighbors.append((x, j))
            break
        x += 1
    # left
    y = j - 1
    while y >= 0:
        if mat[i][y] != '.':
            neighbors.append((i, y))
            break
        y -= 1
    # right
    y = j + 1
    while y < len(mat[0]):
        if mat[i][y] != '.':
            neighbors.append((i, y))
            break
        y += 1
    # top left
    x, y = i - 1, j - 1
    while x >= 0 and y >= 0:
        if mat[x][y] != '.':
            neighbors.append((x, y))
            break
        x -= 1
        y -= 1
    # top right
    x, y = i - 1, j + 1
    while x >= 0 and y < len(mat[0]):
        if mat[x][y] != '.':
            neighbors.append((x, y))
            break
        x -= 1
        y += 1
    # bottom left
    x, y = i + 1, j - 1
    while x < len(mat) and y >= 0:
        if mat[x][y] != '.':
            neighbors.append((x, y))
            break
        x += 1
        y -= 1
    # bottom right
    x, y = i + 1, j + 1
    while x < len(mat) and y < len(mat[0]):
        if mat[x][y] != '.':
            neighbors.append((x, y))
            break
        x += 1
        y += 1
    return neighbors



def swap_seats(ver=1):
    """
    Swap seats until pattern stablizes. Print number of seats occupied.
    Args:
        ver (int, optional): whether seating for q1 or for q2 is to be used.
    """
    if ver == 1:
        seats = data_parser()
        threshold = 4
    else:
        seats = data_parser_v2()
        threshold = 5
    while True:
        for key in seats:
            if seats[key][0] == 'L':
                if not any([seats[n][0] == '#' for n in seats[key][2]]):
                    seats[key][1] = '#'
            elif seats[key][0] == '#':
                if sum([seats[n][0] == '#' for n in seats[key][2]]) >= threshold:
                    seats[key][1] = 'L'
        unchanged = True
        n_occupied = 0
        for key in seats:
            unchanged = unchanged and (seats[key][0] == seats[key][1])
            seats[key][0] = seats[key][1]
            if seats[key][0] == '#':
                n_occupied += 1
        if unchanged:
            print(n_occupied)
            return


if __name__ == '__main__':
    swap_seats()
    swap_seats(ver=2)



