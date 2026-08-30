class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # We are trying to do a product of everything except current element
        # this reads as prefix/postfix sum/product type pattern

        output = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            output[i] = prefix # [1, 1, 2, 8]
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            output[i] *= postfix # [48, 24, 12, 8]
            postfix *= nums[i] 
        return output
            
