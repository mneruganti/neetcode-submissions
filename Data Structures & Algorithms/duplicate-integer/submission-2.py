class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # not efficient - a hashmap takes more mem than a set
        '''hashmap = {}

        for x in nums:
            if x not in hashmap:
                hashmap.update({x: 1})
            else:
                return True
        return False
        '''

        hashset = set()

        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
        