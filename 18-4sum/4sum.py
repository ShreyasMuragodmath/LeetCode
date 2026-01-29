class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res, quad = [], []# current quadruplent in construction

        def kSum(k, start, target): #target changes as the quad is building
            if k != 2:
                for i in range(start, len(nums) - k + 1):# we want atlest k values to make the quad
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    kSum(k-1, i+1, target - nums[i])
                    quad.pop()
                return 
            # base case Two Sum
            l, r = start, len(nums)-1
            while l < r:
                if nums[l] + nums[r] < target:
                     l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        kSum(4, 0, target)
        return res


