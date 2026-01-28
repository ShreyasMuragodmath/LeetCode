class Solution(object):
    def trap(self, nums):
        if not nums:
            return 0

        l,r = 0,len(nums)-1
        lm,rm = nums[l],nums[r]
        res = 0
        while l < r:
            if lm < rm:
                l += 1
                lm = max(lm, nums[l])
                res += lm - nums[l]
            else:
                r -= 1
                rm = max(rm, nums[r])
                res += rm - nums[r]
        return res
            





        