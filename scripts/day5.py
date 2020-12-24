def data_parser():
    """
    Parse out data in ../data/day5.txt
    Returns:
        list: list of str where each string shows boarding pass for one person.
    """
    file_path = '../data/day5.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    out = [x.strip() for x in raw]
    return out


def get_seat(bp):
    """
    Returns seat number given one boarding pass.
    Args:
        bp (str): boarding pass
    Returns:
        int: seat number
    """
    row_num = 0
    row_exp = 6
    for row_id in bp[:7]:
        if row_id == 'B':
            row_num += 2 ** row_exp
        row_exp -= 1

    seat_num = 0
    seat_exp = 2
    for seat_id in bp[7:]:
        if seat_id == 'R':
            seat_num += 2 ** seat_exp
        seat_exp -= 1

    return row_num * 8 + seat_num


def get_max_seat():
    """
    Print out max seat number.
    """
    dat = data_parser()
    max_seat = 0
    for bp in dat:
        seat_num = get_seat(bp)
        max_seat = max(max_seat, seat_num)
    print(max_seat)


def find_seat():
    """
    Find the missing seat where x-1 and x+1 both exist.
    """
    dat = data_parser()
    seat_set = set()
    for bp in dat:
        seat_set.add(get_seat(bp))
    missing_seats = set(range(128 * 8 - 1)) - seat_set
    for seat in missing_seats:
        if 0 < seat < 128 * 8 - 1 and seat - 1 in seat_set and seat + 1 in seat_set:
            print(seat)
            return


if __name__ == '__main__':
    get_max_seat()
    find_seat()