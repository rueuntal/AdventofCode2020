def data_parser():
    """
    Parse out data in ../data/day6.txt
    Returns:
        list: list of lists where each sublist consists of strings for people in that group.
    """
    file_path = '../data/day6.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    out, group = [], []
    for dat_line in raw:
        dat_line = dat_line.strip()
        if dat_line:
            group.append(dat_line)
        else:
            out.append(group)
            group = []
    out.append(group)
    return out


def count_qs():
    """
    Sum of all questions marked by all groups.
    """
    out = 0
    groups = data_parser()
    for group in groups:
        out += len(set(''.join(group)))
    print(out)
    return


def count_shared_qs():
    """
    Sum of all q's marked by everyone within each group.
    """
    out = 0
    groups = data_parser()
    for group in groups:
        out += len(set.intersection(*[set(x) for x in group]))
    print(out)
    return


if __name__ == '__main__':
    count_qs()
    count_shared_qs()