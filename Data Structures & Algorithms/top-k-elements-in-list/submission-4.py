class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # This is the map to COUNT the initale frequency of every element in the list
        countMap = {}

        # result array to hold top k elements
        res = [] 

        # list of lists where the frequency is the index and the list of values
        # that have this frequency are the values
        freq = [[] for i in range(len(nums) + 1)]

        # populate hashmap
        for n in nums:
            countMap[n] = 1 + countMap.get(n, 0)

        # get the n = value, c = count from hashmap
        for n, c in countMap.items():
            freq[c].append(n) # add the value at that specific frequency

        for i in range(len(freq) - 1, 0, -1):
            for x in freq[i]:
                res.append(x)

                if len(res) == k:
                    return res
            