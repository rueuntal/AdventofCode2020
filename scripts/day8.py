def data_parser():
    """
    Parse out data in ../data/day8.txt
    Returns:
        list: list of lists where each sublist contains [command (str), num (int)]
    """
    file_path = '../data/day8.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    out = [x.strip().split(' ') for x in raw]
    out = [[x[0], int(x[1])] for x in out]
    return out



def run_commands(execs):
    """
    Identify loop in commands.
    Args:
        execs: list of lists defining the commands
    Returns:
        int, int: id of command that starts looping (-1 if executed to the end), accumulator
    """
    accumulator = 0
    visited = set()
    i = 0
    while True:
        if i in visited:
            return i, accumulator
        visited.add(i)
        if i == len(execs):
            return -1, accumulator
        if i > len(execs):
            return -2, accumulator
        command, val = execs[i]
        if command == 'nop':
            i += 1
        elif command == 'acc':
            i += 1
            accumulator += val
        else:
            i += val


def find_loop():
    """
    Find val before loop starts.
    If a loop is found
    """
    execs = data_parser()
    _, acc = run_commands(execs)
    print(acc)
    return


def fix_loop():
    """
    Find command that can fix the infinite loop.
    """
    execs = data_parser()
    for i in range(len(execs)):
        command, val = execs[i]
        if command != 'acc':
            execs_cp = [x[:] for x in execs]
            if command == 'nop':
                execs_cp[i][0] = 'jmp'
            else:
                execs_cp[i][0] = 'nop'
            idx, acc = run_commands(execs_cp)
            if idx == -1:
                return acc



if __name__ == '__main__':
    find_loop()
    print(fix_loop())