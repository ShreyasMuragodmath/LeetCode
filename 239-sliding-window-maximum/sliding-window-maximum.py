class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        q = collections.deque() # index
        l, r = 0,0

        while r < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[r]: # q non empty and right most element < nums[r]
                q.pop()
            q.append(r)

            # remove left val fom winodw (l out of bound)
            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res

        


        