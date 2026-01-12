class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """                
        count = 0
        n = len(nums)
        i = 0
        
        while(i<n):
            if(nums[i] == 2):
                nums.append(2)
                nums.pop(i)
                i -= 1
                n -= 1
            elif(nums[i] == 0):
                count += 1
                nums.pop(i)
                i -= 1
                n -= 1
            i += 1
        while(count != 0):
            nums.insert(0,0)
            count -= 1


