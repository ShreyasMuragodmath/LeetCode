class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mp = {}
        for i in range (len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        return max(mp, key=mp.get)

        