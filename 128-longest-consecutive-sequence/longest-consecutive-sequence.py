from collections import defaultdict
class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        mp = defaultdict(int)
        key = 0
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        length = 1
        mp[key] = length
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                length += 1
                mp[key] = length
            else:
                key += 1
                length = 1
                mp[key] = 1
        return max(mp.values())
        







        