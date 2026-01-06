class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # mp = {}
        # for i in range (len(nums)):
        #     mp[nums[i]] = mp.get(nums[i], 0) + 1
        # return max(mp, key=mp.get)

        count = 0
        ans = -1

        for curr in nums:
            if count == 0:
                ans = curr

            if ans == curr:
                count += 1
            else:
                count -= 1

        return ans

        