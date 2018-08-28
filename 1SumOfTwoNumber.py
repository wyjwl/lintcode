def twoSum(nums, target):
    dataMap = dict()
    for index in range(len(nums)):
        complement = target - nums[index]
        if dataMap.__contains__(complement):
            return list([index, dataMap[complement]])
        dataMap[nums[index]] = index


result = twoSum([2, 7, 11, 15], 9)
print(result)
