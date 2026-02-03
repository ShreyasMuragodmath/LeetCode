class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1)>len(s2):
            return False

        mp = {}
        for i in range (len(s1)):
            mp[s1[i]] = 1 + mp.get(s1[i], 0)

        l = 0
        count = {}
        for r in range(len(s2)):
            count[s2[r]] = count.get(s2[r],0) + 1

            if (r - l + 1) > len(s1):
                count[s2[l]] -= 1
                if count[s2[l]] == 0:
                    del count[s2[l]]
                l += 1
            if mp == count:
                return True
        return False




        