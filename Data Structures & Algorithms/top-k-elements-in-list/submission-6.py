class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        freqMap = {}
        freq = [[] for x in range(len(nums) + 1)]

        for x in nums:
            freqMap[x] = freqMap.get(x, 0) + 1 # {1: 0, 2: 2, 3: 3}

        for n, c in freqMap.items():
            freq[c].append(n) # [[1], [], [2], [3]]

        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]: 
                results.append(x)
                
                if len(results) == k:
                    return results
 