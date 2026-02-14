class StockSpanner(object):

    def __init__(self):
        self.stack = []
        
    def next(self, v):
        # count = 1
        # if not self.stack:
        #     self.stack.append((v,1))
        #     return 1
        # else:
        #     if v < self.stack[-1][0]:
        #         self.stack.append((v,1))
        #         return 1
        #     else:
        #         while self.stack and self.stack[-1][0] <= v:
        #             _,freq = self.stack.pop()
        #             count += freq
        #         self.stack.append((v,count))
        #         return count
        count =1
        while self.stack and self.stack[-1][0] <= v:
            _,freq = self.stack.pop()
            count += freq
        self.stack.append((v,count))
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)