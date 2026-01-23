class Solution(object):
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # i is not the first element and the element is same as the prev element (A)
                continue
            l,r = i + 1, len(nums) - 1 # B,C
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    # update pointers 
                    l += 1 #first element of the dublicate elemets
                           # r updates itself as the sum has now changed (from the above code)
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 #last element of the dublicate elements
        return res
                

                
        