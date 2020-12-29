def num_counter(start, stop):
    """
    Given a starting list of nums, find the num spoken at the stop.
    Args:
         start (list): list of ints to start
         stop (int): step at which the game stops
    Returns:
        int: num at stop
    """
    step = 0
    record = {}
    for num in start[:-1]:
        record[num] = step
        step += 1
    last_num = start[-1]
    while step < stop:
        if last_num not in record:
            next_num = 0
        else:
            next_num = step - record[last_num]
        record[last_num] = step
        last_num = next_num
        step += 1
    return last_num


if __name__ == '__main__':
    print(num_counter([0, 8, 15, 2, 12, 1, 4], 29999999))