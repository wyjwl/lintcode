def swap(nums, start, index):
    temp = nums[start]
    nums[start] = nums[index]
    nums[index] = temp


def per(nums, start, result):
    if start == len(nums) - 1:
        result.append([num for num in nums])

    else:
        index = start
        while index < len(nums):
            swap(nums, start, index)
            per(nums, start + 1, result)
            swap(nums, start, index)
            index += 1


def permute(nums):
    result = []

    if nums is None or len(nums) < 1:
        return result

    per(nums, 0, result)

    return result


print(permute([1, 2, 2]))
