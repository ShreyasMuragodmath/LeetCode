class Solution(object):
    def topKFrequent(self, nums, k):
        mp = {}
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        
        ans = []
        while(k!=0):
            ans.append(max(mp, key=mp.get))
            mp.pop(max(mp, key=mp.get))
            k -= 1
        return ans
