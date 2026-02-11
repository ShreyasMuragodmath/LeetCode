class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == "+":
                sec = stack.pop()
                first = stack.pop()
                stack.append(first + sec)
            elif t =="-":
                sec = stack.pop()
                first = stack.pop()
                stack.append(first - sec)
            elif t =="/":
                sec = stack.pop()
                first = stack.pop()
                stack.append(int(float(first) / sec))

            elif t == "*":
                sec = stack.pop()
                first = stack.pop()
                stack.append(first * sec)

            else:
                stack.append(int(t))
        return stack[0]
