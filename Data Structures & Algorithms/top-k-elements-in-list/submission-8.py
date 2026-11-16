class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqMap = {}
        minHeap = []

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        for key in freqMap.keys():
            heapq.heappush(minHeap, (freqMap[key], key))

            if (len(minHeap) > k):
                heapq.heappop(minHeap)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        return res

        
        
 