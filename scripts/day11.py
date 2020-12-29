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


def swap_seats():
    """
    Swap seats until pattern stablizes. Print number of seats occupied.
    """
    seats = data_parser()
    while True:
        for key in seats:
            if seats[key][0] == 'L':
                if not any([seats[n][0] == '#' for n in seats[key][2]]):
                    seats[key][1] = '#'
            elif seats[key][0] == '#':
                if sum([seats[n][0] == '#' for n in seats[key][2]]) >= 4:
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



