def removeDuplicnumstes(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.remove(nums[i])
        else:
            i += 1
    return len(nums)

print(removeDuplicnumstes([1,1,2]))