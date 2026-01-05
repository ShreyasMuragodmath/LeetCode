class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        ptr1, ptr2, count = 0, len(nums)-1, 0
        while(ptr1 != ptr2):
            if nums[ptr1] == val:
                count += 1
                nums[ptr1], nums[ptr2] = nums[ptr2], nums[ptr1]
                ptr2 = ptr2 - 1
            else:
                ptr1 = ptr1 + 1
        if ptr1 == ptr2:
            if nums[ptr1] == val:
                return len(nums) - count - 1
            
        return len(nums) - count
        