class Solution(object):
    def isPalindrome(self, s):
        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not self.an(s[start]):
                start += 1
            while start < end and not self.an(s[end]):
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1 
        return True

    def an(self, s):
        return (ord('A') <= ord(s) <= ord('Z') or
                ord('a') <= ord(s) <= ord('z') or
                ord ('0') <= ord(s) <= ord('9'))

        