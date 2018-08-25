class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """

    def closestTargetValue(self, target, array):
        # Write your code here
        array.sort()
        start = 0
        end = len(array) - 1
        lastSum = None

        while start < end:
            sum = array[start] + array[end]
            if sum == target:
                return sum

            elif sum < target:
                start += 1
                lastSum = myMax(lastSum, sum)

            else:
                end -= 1

        return lastSum if lastSum else -1

def myMax(lastSum, sum):
    return max(lastSum, sum) if lastSum is not None else sum











# 先排序 然后双指针前后搜索