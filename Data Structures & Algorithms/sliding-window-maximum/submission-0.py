class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []
        q = collections.deque() # kick from front and bacl
        l, r = 0, 0
        
        while r < len(nums):

            # deque stores indicies, so q[-1] is the index at back of deque
            # and nums[q[-1]] gets the value at the index at the back
            # if this value is less than the value on the right, pop it 
            # because we want the queue to be decreasing
            while q and nums[q[-1]] < nums[r]: 
                q.pop()
            q.append(r) # add value 

            # q[0] index of current maximum bc its front of queue and queue is decreasing
            # so if the largest index is no longer within the left window (start)
            # we can remove it as it is stale data in the new window
            if l > q[0]: 
                q.popleft()

            # We need to fill the window until k elements
            if (r + 1) >= k:
                res.append(nums[q[0]]) # first full window - record max 
                l += 1 # shrink window
            r += 1 # expand window

        return res

        