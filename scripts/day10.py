def data_parser():
    """
    Parse out data in ../data/day10.txt
    Returns:
        list: list of ints.
    """
    file_path = '../data/day10.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    out = [int(x.strip()) for x in raw]
    return out


def find_jumps():
    """
    Find jumps of 1's and 3's, assuming every adapter is used once.
    Returns:
        product of 1-jo;t steps and 3-jolt steps
    """
    adapters = sorted(data_parser())
    cur_level = 0
    diff_1, diff_3 = 0, 0
    for adapter in adapters:
        if adapter - cur_level == 1:
            diff_1 += 1
        elif adapter - cur_level == 3:
            diff_3 += 1
        cur_level = adapter
    diff_3 += 1
    return diff_1 * diff_3


def count_paths():
    """
    Count number of paths.
    """
    adapters = sorted(data_parser(), reverse=True)
    path_count = {}

    def count_recur(adapters):
        """
        Count number of ways from the lowest adapter to the highest adapter, assuming each step is 1-3.
        Args:
            adapters (list): sorted list of ints from high to low
        Returns:
            int: number of paths
        """
        max_adapter = adapters[0]
        if max_adapter in path_count:
            return path_count[max_adapter]
        if len(adapters) == 1:
            return 1
        # count to max is the sum of all paths to other adapters within jolt diff of 3
        next_steps = [i for i in range(1, 4) if i < len(adapters) and max_adapter - adapters[i] <= 3]
        counts = 0
        for next_step in next_steps:
            counts += count_recur(adapters[next_step:])
        # if max adapter is below 3 then it can be directly reached
        if max_adapter <= 3:
            counts += 1
        path_count[max_adapter] = counts
        return counts

    return count_recur(adapters)


if __name__ == '__main__':
    print(find_jumps())
    print(count_paths())