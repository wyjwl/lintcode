def getSingleNumber(nums):
    index = 0
    while index < len(nums):
        if nums[index] == nums[index+1]:
            index += 2

        else:
            return nums[index] if nums[index+1] == nums[index+2] else nums[index+1]