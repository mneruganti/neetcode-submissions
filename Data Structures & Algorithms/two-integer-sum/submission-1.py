class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # nums = [3,4,5,6], target = 7

        prevMap = {} # val: index

        for i, n in enumerate(nums): # 3: 0, 4: 1, 5: 2, etc
            diff = target - n # 4, 3, 2, etc

            if diff in prevMap:
                return [prevMap[diff], i] # returns [0, 1]
            
            prevMap[n] = i # 3: 0
        return
        