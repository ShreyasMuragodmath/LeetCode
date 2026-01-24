class Solution(object):
    def rotate(self, nums, k):
        if len(nums) == 0 or len(nums) == 1:
            return 
        if len(nums) < k:
            k = k % len(nums)

        # while k != 0:
        #     nums.insert(0, nums[len(nums)-1])
        #     k -= 1
        #     nums.pop()
        r = len(nums) - k

        while r != 0:
            nums.append(nums[0])
            nums.pop(0)
            r -= 1


        