class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.v1Index = 0
        self.v2Index = 0
        self.currentList = 1

    def next(self):
        if self.currentList == 1:
            if self.v1Index < len(self.v1):
                self.currentList = 2
                self.v1Index += 1
                return self.v1[self.v1Index - 1]
            else:
                self.currentList = 2
                self.v2Index += 1
                return self.v2[self.v2Index - 1]
        if self.currentList == 2:
            if self.v2Index < len(self.v2):
                self.currentList = 1
                self.v2Index += 1
                return self.v2[self.v2Index - 1]
            else:
                self.currentList = 1
                self.v1Index += 1
                return self.v1[self.v1Index - 1]



    def hasNext(self):
        return self.v1Index < len(self.v1) or self.v2Index < len(self.v2)
