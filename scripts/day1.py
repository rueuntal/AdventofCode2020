def read_file():
    """
    Read ../data/day1a.txt into a list of ints.
    """
    file_path = '../data/day1a.txt'
    with open(file_path, 'r') as stream:
        out = stream.readlines()
    out = [int(x.strip()) for x in out]
    return out


def get_product():
    """
    Get the product of the two ints from the given list that add up to 2020.
    """
    nums = set(read_file())
    for num in nums:
        if num != 2020 // 2 and 2020 - num in nums:
            print(num * (2020 - num))
            return


def get_three_product():
    """
    Return the product of the three numbers from the given list that add up to 2020.
    """
    # sorting is O(nlog(n))
    nums = sorted(read_file())
    # find sum is O(n**2)
    for i in range(len(nums) - 2):
        num_i = nums[i]
        target = 2020 - num_i
        j, k = i + 1, len(nums) - 1
        while j < k:
            if nums[j] + nums[k] < target:
                j += 1
            elif nums[j] + nums[k] > target:
                k -= 1
            else:
                print(num_i * nums[j] * nums[k])
                return



if __name__ == '__main__':
    get_product()
    get_three_product()