def findDisappearedNumbers(nums):

    i = 0
    while i < len(nums):
        if i+1 != nums[i] and nums[i] != nums[nums[i]-1]:
            temp = nums[i]
            nums[i] = nums[nums[i]-1]
            nums[temp - 1] = temp
            i -= 1
        i += 1
    miss = []

    for i in range(0, len(nums)):
        if i+1 != nums[i]:
            miss.append(i+1)

    return miss
