import sys 
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if t == "": return ""

        countT, window = {},{}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        need = len(countT)
        have = 0
        res, resLen = [-1,-1], sys.maxint
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l,r]
                    resLen = (r - l + 1)

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                l += 1

        return s[res[0]:res[1]+1] if resLen != sys.maxint else ""



                



        