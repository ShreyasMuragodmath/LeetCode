class Solution(object):
    def mergeAlternately(self, word1, word2):
        l, r = 0, 0
        flag1, flag2 = 0, 0
        merge = ""
        while(flag1 == 0 or flag2 == 0):
            if flag1 == 0:
                merge = merge + word1[l]
            else:
                merge = merge + word2[r:]
                return merge
            if flag2 == 0:
                merge = merge + word2[r]
            else:
                merge = merge + word1[l+1:]
                return merge

            l, r = l + 1, r + 1
            if l>=len(word1):
                flag1 = 1
            if r>=len(word2):
                flag2 = 1
        return merge


        