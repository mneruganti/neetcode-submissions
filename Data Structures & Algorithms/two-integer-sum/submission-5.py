class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i] # 4, 3

            if diff in hashMap:
                return [hashMap[diff], i]
            
            hashMap[nums[i]] = i # {3: 0}
        return []
        