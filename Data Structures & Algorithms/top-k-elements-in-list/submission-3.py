class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countMap = {}
        res = []
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0) # get the frequency of the nums
            
        for n, c in countMap.items(): # loop through the pairs
            freq[c].append(n) # at the index of the count, add n to the list
        
        for i in range(len(freq) - 1, 0, -1): # iterate from backwards
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res

        

        # Time Complexity: O(n)
        # Space Complexity: O(n)
            
            
        