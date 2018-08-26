def rotate(nums, k):
    k = k % len(nums)
    reverse(nums, 0, len(nums) - k-1)
    reverse(nums, len(nums) - k, len(nums) - 1)
    reverse(nums, 0 , len(nums) - 1)
    return nums


def reverse(nums, s, e):
    if len(nums) == 0 or nums is None:
        return

    while s < e:
        temp = nums[s]
        nums[s] = nums[e]
        nums[e] = temp
        s += 1
        e -= 1


print(rotate([-1,-100,3,99], 2))
