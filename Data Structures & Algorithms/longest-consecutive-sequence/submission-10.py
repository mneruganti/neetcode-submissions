class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashSet = set(nums)
        longest = 0

        for x in hashSet:
            if (x - 1) not in hashSet:
                length = 0
                while (x + length) in hashSet:
                    length += 1
                    
                longest = max(length, longest)
        return longest


        