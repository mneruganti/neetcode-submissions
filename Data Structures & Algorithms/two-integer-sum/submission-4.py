class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n # 4, 3

            if (diff in hashMap):
                return [hashMap[diff], i]
            
            hashMap[n] = i
        
        # {4: 0, 3: 1}