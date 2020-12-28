def data_parser():
    """
    Parse out data in ../data/day9.txt
    Returns:
        list: list of ints.
    """
    file_path = '../data/day9.txt'
    with open(file_path, 'r') as stream:
        raw = stream.readlines()
    out = [int(x.strip()) for x in raw]
    return out


def find_sum(nums, target):
    """
    Find if target can be represented as the sum of two numbers from nums.
    Args:
        nums (list): list of ints to search
        target (int): target sum
    Returns:
        bool: whether target can be found
    """
    nums = sorted(nums)
    i, j = 0, len(nums) - 1
    while i < j:
        curr_sum = nums[i] + nums[j]
        if curr_sum == target:
            return True
        if curr_sum < target:
            i += 1
        else:
            j -= 1
    return False


def find_first():
    """
    Find first number for day 9 data that cannot be represented as a two-sum in the previous 25 nums.
    """
    all_nums = data_parser()
    i = 25
    while i < len(all_nums):
        if not find_sum(all_nums[(i-25):i], all_nums[i]):
            return all_nums[i]
        i += 1


def find_consecutive():
    """
    Find consecutive numbers that add to the number found in part 1.
    Brutal force search O(n**2)
    """
    target = find_first()
    all_nums = data_parser()
    for i in range(len(all_nums)):
        curr_sum = all_nums[i]
        curr_min, curr_max = all_nums[i], all_nums[i]
        for j in range(i + 1, len(all_nums)):
            curr_sum += all_nums[j]
            curr_min = min(curr_min, all_nums[j])
            curr_max = max(curr_max, all_nums[j])
            if curr_sum == target:
                return curr_min + curr_max


if __name__ == '__main__':
    print(find_first())
    print(find_consecutive())