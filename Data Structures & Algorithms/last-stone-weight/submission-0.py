import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # we need to build a max heap because we are always trying to access the two largest stones
        # if the stone weights are equal, pop both from the max heap (two heapq.heappop())
        # if x < y, calculate new weight = y - x, pop stone x, and replace stone y with new weight
        # loop through all stones until length == 1 or 0

        stones = [-s for s in stones]
        heapq.heapify(stones)
        print(stones)

        while (len(stones) > 1):
            x = heapq.heappop(stones)
            print(x)
            y = heapq.heappop(stones)
            print(y)

            if (x == y):
                print("equal")
                continue
            elif (x < y):
                
                new_weight = x-y
                print("NW: x < y", new_weight)
                heapq.heappush(stones, new_weight)
            else:
                new_weight = y-x
                print("NW: x > y", new_weight)
                heapq.heappush(stones, new_weight)

        
        return -stones[0] if len(stones) == 1 else 0


        