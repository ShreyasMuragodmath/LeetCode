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
        ## TLE for large array

        # r = len(nums) - k
        # while r != 0:
        #     nums.append(nums[0])
        #     nums.pop(0)
        #     r -= 1
        ## Slow runtime
        
        def reverse_(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        
        reverse_(0,len(nums)-1)
        reverse_(0,k-1)
        reverse_(k,len(nums)-1)

        




        