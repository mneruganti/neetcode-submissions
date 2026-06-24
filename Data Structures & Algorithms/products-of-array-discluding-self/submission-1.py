class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] = prefix # in each spot, put what the current prefix is
            prefix *= nums[i] # calculate next prefix
        postfix = 1

        # start: len(nums) - 1: last index
        # stop: exclusive right before -1 = index 0
        # step: decrement by 1
        for i in range(len(nums) - 1, -1, -1):

            # from the back, multiply the postfix to get the final values
            res[i] *= postfix

            # calculate next postfix
            postfix *= nums[i]
        return res

       
        