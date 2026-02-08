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
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(c))
        res = 0
        while stack:
            res += stack[-1]
            stack.pop()

        return res



        