class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # k closest points - minHeap and pop k top elements

        # we want to map each point to a distance, so we can store
        # a min heap that contains tuples like this: (distance, index)

        # iterate through points using index i and compute distance per point,
        # push into minHeap (distance, i)
        # once all elements are in min heap, have a loop run k times and pop the
        # k elements off, get the index (second element of tuple), access the 
        # point from points[i], and append it to res

        res = []
        minHeap = []

        for i in range(len(points)):
            distance = math.sqrt((0 - points[i][0]) ** 2 + (0 - points[i][1]) ** 2)
            heapq.heappush(minHeap, (distance, i))
        
        for i in range(k):
            index = heapq.heappop(minHeap)
            res.append(points[index[1]])
        return res
        