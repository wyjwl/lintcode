class MovingAverage:
    """
    @param: size: An integer
    """

    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.currentTotal = 0
        self.mystack = []

    """
    @param: val: An integer
    @return:
    """

    def next(self, val):
        # write your code here
        if len(self.mystack) < self.size:
            self.mystack.append(val)
            self.currentTotal += val
            return self.currentTotal/len(self.mystack)
        else:
            self.currentTotal = self.currentTotal - self.mystack[0]
            self.mystack.remove(self.mystack[0])
            self.mystack.append(val)
            self.currentTotal = self.currentTotal + val
            return self.currentTotal / len(self.mystack)
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)

a = MovingAverage(3)
a.next(1)
a.next(10)
a.next(3)
a.next(5)
