def data_parser():
    """
    Parse out data in ../data/day3.txt
    Returns:
        list: list of str where each string shows open space and trees in one row.
    """
    file_path = '../data/day3.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    out = [x.strip() for x in raw]
    return out


def count_trees(right, down):
    """
    Count the number of trees that will be bumped into by right and down.
    Args:
        right (int): position to move to the right in each round
        down (int): position to move to the bottom in each round
    """
    dat = data_parser()
    row, pos = 0, 0
    row_len = len(dat[0])
    tree_count = 0
    while row < len(dat) - down:
        row += down
        pos = (pos + right) % row_len
        if dat[row][pos] == '#':
            tree_count += 1
    return tree_count


def count_trees_multiple():
    """
    Apply the previous function with different options and obtain the product of the counts.
    """
    ans = 1
    for right, down in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        ans *= count_trees(right, down)
    print(ans)
    return


if __name__ == '__main__':
    print(count_trees(3, 1))
    count_trees_multiple()