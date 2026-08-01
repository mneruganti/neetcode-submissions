class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dup_set = set()

        for n in nums:
            if n in dup_set:
                return True
            else:
                dup_set.add(n)
        return False
        