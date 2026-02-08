class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []

        for c in operations:
            if c == 'D':
                stack.append(2 * stack[-1])
            elif c == 'C':
                stack.pop()
            elif c == '+':
                a = stack[-1]
                stack.pop()
                b = stack[-1]
                stack.append(a)
                stack.append(a + b)
            else:
                stack.append(int(c))
        res = 0
        while stack:
            res += stack[-1]
            stack.pop()
        return res



        