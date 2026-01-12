class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = 1 + mp.get(nums[i],0)
        res = []
        for k, v in mp.items():
            if v > len(nums)//3:
                res.append(k)
        return res