import numpy as np
class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
            
        sufix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= sufix
            sufix *= nums[i]
        return res




        

