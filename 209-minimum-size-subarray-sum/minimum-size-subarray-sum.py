import sys
class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        sum_s = 0
        res = sys.maxint

        for r in range (len(nums)):
            sum_s += nums[r]
            while sum_s >= target:
                sum_s -= nums[l]
                l += 1
                res = min(res, r - l + 2)
        if res == sys.maxint:
            return 0
        else:
            return res



        