class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        dict1 = {}
        dict2 = {}
       
        for i in range(len(s)):
                dict1[s[i]] = dict1.get(s[i], 0) + 1
                dict2[t[i]] = dict2.get(t[i], 0) + 1
        return dict1 == dict2
            

        