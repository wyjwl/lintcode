def productExceptSelf(nums):
    mul = 1
    for num in nums:
        mul *= num

    k = []

    if mul == 0:
        for num in nums:
            k.append(0)
        return k

    for num in nums:
        k.append(int(mul/num))

    return k
