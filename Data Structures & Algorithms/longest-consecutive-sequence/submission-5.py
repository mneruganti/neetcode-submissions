class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) # convert nums into a set
        longest = 0 # variable for longest length

        for n in nums: # iterate through all nums
            if (n - 1) not in numSet: # if left neighbor not in set
                length = 0; # start of a sequence (curr sequence length)
                while ((n + length) in numSet): # we iterate through each consecutive num until it is not in numSet
                    length += 1
                longest = max(length, longest) # take max
        return longest # return longest
        