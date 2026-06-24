class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # create a hashset (no duplicates)
        numSet = set(nums)
        longest = 0

        for n in numSet: # iterate each num
            if (n-1) not in numSet: # if the number before it isn't in the set, we know its the start f a sequence
                length = 0

                while ((n + length) in numSet): # iterate through consecutive nums until its not in set anymore
                    length += 1
                longest = max(longest, length) # take max
        return longest

        