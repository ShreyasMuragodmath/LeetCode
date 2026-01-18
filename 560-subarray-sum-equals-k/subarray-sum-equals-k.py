class Solution(object):
    def subarraySum(self, nums, k):
        curSum = 0
        res = 0
        prefix = {0:1}
        for n in nums:
            curSum += n
            if curSum-k in prefix:
                res += prefix[curSum-k]
            prefix[curSum] = prefix.get(curSum,0) + 1

        return res
