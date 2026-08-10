class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # We need a hashmap to store the inital key, and the difference from the target as the value

        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            
            if (diff in hashMap):
                return [hashMap[diff], i]
            
            hashMap[n] = i
        return
        