class Solution(object):
    def mergeAlternately(self, word1, word2):
        # l, r = 0, 0
        # flag1, flag2 = 0, 0
        # merge = ""
        # while(flag1 == 0 or flag2 == 0):
        #     if flag1 == 0:
        #         merge = merge + word1[l]
        #     else:
        #         merge = merge + word2[r:]
        #         return merge
        #     if flag2 == 0:
        #         merge = merge + word2[r]
        #     else:
        #         merge = merge + word1[l+1:]
        #         return merge

        #     l, r = l + 1, r + 1
        #     if l>=len(word1):
        #         flag1 = 1
        #     if r>=len(word2):
        #         flag2 = 1
        # return merge
        l,r = 0,0
        merge = ""
        while (l<len(word1) and r<len(word2)):
            merge = merge + word1[l]
            merge = merge + word2[r]
            l+=1
            r+=1

        while l<len(word1):
            merge = merge + word1[l]
            l+=1
        
        while r<len(word2):
            merge = merge + word2[r]
            r+=1
        return merge



        