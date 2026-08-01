class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = {}

        res = []
        freq = [[] for x in range(len(nums) + 1)]

        for n in nums:
            '''
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1
            '''
            freqMap[n] = 1 + freqMap.get(n, 0)
        
        for n, c in freqMap.items():
            freq[c].append(n)
        
        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                res.append(x)
                
                if len(res) == k:
                    return res
    
        