class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closeToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c in closeToOpen: # closeing paranthesis
                if stack and stack[-1] == closeToOpen[c]: # at some case 'open' and 'close' must exist together to be true
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c) # opening paranthesis
        return True if not stack else False


        