class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp:
                return True
            mp[nums[i]] = i
        return False
        