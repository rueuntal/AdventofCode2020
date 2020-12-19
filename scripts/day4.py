def data_parser():
    """
    Parse out ../data/day4.txt.
    Returns:
        list: list of dict where each dict contains info for one person with key:val
    """
    file_path = '../data/day4.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    out, pp = [], {}
    for dat_line in raw:
        dat_line = dat_line.strip()
        if dat_line:
            key_val_list = dat_line.split(' ')
            for key_val in key_val_list:
                key, val = key_val.split(':')
                pp[key] = val
        else:
            out.append(pp)
            pp = {}
    out.append(pp)
    return out


def count_valid_pp():
    """
    Count valid passports with the designated fields except for cid.
    """
    pp_count = 0
    pps = data_parser()
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for pp in pps:
        if all([key in pp for key in keys]):
            pp_count += 1
    print(pp_count)
    return


def count_valid_pp_strict():
    """
    Count valid passports with stricter rules.
    """
    pp_count = 0
    pps = data_parser()
    keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for pp in pps:
        if all([key in pp for key in keys]):
            if 1920 <= int(pp['byr']) <= 2002:
                if 2010 <= int(pp['iyr']) <= 2020:
                    if 2020 <= int(pp['eyr']) <= 2030:
                        if (pp['hgt'][-2:] == 'in' and 59 <= int(pp['hgt'][:-2]) <= 76) or (pp['hgt'][-2:] == 'cm' and 150 <= int(pp['hgt'][:-2]) <= 193):
                            if pp['hcl'][0] == '#' and pp['hcl'][1:].isalnum():
                                if pp['ecl'] in ['amb', 'blu','brn', 'gry', 'grn', 'hzl', 'oth']:
                                    if len(pp['pid']) == 9 and pp['pid'].isdigit():
                                        pp_count += 1
    print(pp_count)
    return


if __name__ == '__main__':
    count_valid_pp()
    count_valid_pp_strict()