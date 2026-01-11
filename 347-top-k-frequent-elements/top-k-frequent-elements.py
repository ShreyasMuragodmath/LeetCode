class Solution(object):
    def topKFrequent(self, nums, k):
        mp = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in range(len(nums)):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
        for n, c in mp.items():
            freq[c].append(n)
        
        res = []

        for i in range(len(freq)-1, 0, -1): # -1 cz we have a 0th index 
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
