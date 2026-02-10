class MinStack(object):

    def __init__(self):
        self.s = []
        self.min = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.s.append(val)
        if not self.min:
            self.min.append(val)
        elif self.min[-1] >= val:
            self.min.append(val)

    def pop(self):
        """
        :rtype: None
        """
        x = self.s.pop()
        if self.min:
            if x == self.min[-1]:
                self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.min:
            return self.min[-1]
        