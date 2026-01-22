class Solution(object):
    def twoSum(self, nums, k):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0, len(nums)-1
        while l<r:
            if nums[l] + nums[r] == k:
                return [l+1, r+1]
            if nums[l] + nums[r] < k:
                l+=1
                continue
            else:
                r-=1

        