def searchInsert(nums, target):
    if len(nums) == 0:
        return 0

    for i in range(0, len(nums)):
        if nums[i] >= target:
            return i

    return len(nums)