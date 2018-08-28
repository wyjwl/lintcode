def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    i = 0
    while i < len(nums) - 1:
        if nums[i] == val:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)
