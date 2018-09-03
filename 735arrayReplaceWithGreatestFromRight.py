def arrayReplaceWithGreatestFromRight(nums):
    a = nums[len(nums) - 2]
    b = nums[len(nums) - 1]
    nums[len(nums) - 2] = nums[len(nums) - 1]
    nums[len(nums) - 1] = -1

    index = len(nums) - 3

    while index > -1:
        save = nums[index]
        nums[index] = max(a, b)
        b = max(a, b)
        a = max(nums[index], save)
        index -= 1

    return nums

print(arrayReplaceWithGreatestFromRight([1]))