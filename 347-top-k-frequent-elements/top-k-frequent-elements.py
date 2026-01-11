class Solution(object):
    def topKFrequent(self, nums, k):
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        
        ans = []
        while(k!=0):
            res = max(mp, key=mp.get)
            ans.append(res)
            mp.pop(res)
            k -= 1
        return ans
