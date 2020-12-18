from collections import Counter


def data_parser():
    """
    Parse out data in ../data/day2.txt.
    Returns:
        list of lists of [low(int), high(int), char (str), pw (str)]
    """
    file_path = '../data/day2.txt'
    with open(file_path) as stream:
        out = stream.readlines()

    out_cleaned = []
    for dat_line in out:
        count_range, char, pw = dat_line.strip().split(' ')
        low, high = [int(x) for x in count_range.split('-')]
        out_cleaned.append([low, high, char[:-1], pw])
    return out_cleaned


def pw_valid(dat_line):
    """
    Determine if a pw is valid.
    Args:
        dat_line (list): list of [low(int), high(int), char (str), pw (str)]
    Returns:
        bool: whether the pw is valid given the constraint
    """
    low, high, char, pw = dat_line
    pw_counts = Counter(pw)
    if char in pw_counts and low <= pw_counts[char] <= high:
        return True
    return False


def pw_vaid_v2(dat_line):
    """
    Determine if a pw is valid based on the 2nd version of the rule.
    Args:
        dat_line (list): list of [low(int), high(int), char (str), pw (str)]
    Returns:
        bool: whether the pw is valid given the constraint
    """
    low, high, char, pw = dat_line
    if len(pw) >= max(high, low):
        # XOR
        if int(pw[low - 1] == char) + int(pw[high - 1] == char) == 1:
            return True
    return False


def count_valid(ver = 1):
    """
    Count number of valid pw and print output.
    Args:
        ver (int, optional): which version of the pw rule is being used
    """
    dat_lines = data_parser()
    counter = 0
    for dat_line in dat_lines:
        if ver == 1:
            counter += int(pw_valid(dat_line))
        else:
            counter += int(pw_vaid_v2(dat_line))
    print(counter)
    return


if __name__ == '__main__':
    count_valid(ver=1)
    count_valid(ver=2)