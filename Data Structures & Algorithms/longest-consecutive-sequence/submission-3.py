class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        remove_dup = set(nums)
        sorted_set = sorted(remove_dup)
        curr_length = 1
        max_length = 1

        for i in range(len(sorted_set) - 1):
            if abs((sorted_set[i + 1] - sorted_set[i])) == 1:
                curr_length += 1
                if curr_length > max_length:
                    max_length = curr_length
            else:
                curr_length = 1
        return max(max_length, curr_length)