class Solution(object):
    def firstMissingPositive(self, nums):

        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] < 1:
        #         nums.pop(i)
            
        # nums = set(nums)
        # nums = list(nums)
        # nums.sort()
        # count = 1
        # for num in nums:
        #     if num != count:
        #         return count
        #     count += 1
        # return count
        nums = set(nums)
        a = 1
        while(True):
            if a not in nums:
                return a
            a += 1



        