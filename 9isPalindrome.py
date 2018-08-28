def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    revertNumber = 0
    while (x > revertNumber):
        revertNumber = 10 * revertNumber + x % 10
        x = int(x/10)

    return x == revertNumber or x == int(revertNumber / 10)

print(isPalindrome(121))