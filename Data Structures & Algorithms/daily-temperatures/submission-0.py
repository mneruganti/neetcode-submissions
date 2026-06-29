class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures): # get index + temp
            while stack and t > stack[-1][0]: # while stack inst empty and the current element is greater than top of stack
                stackT, stackInd = stack.pop() # get stack top and index
                result[stackInd] = i - stackInd # at the stackInd, store current index - minus stack index (how many days have passed)
            stack.append([t, i]) # append new entry to top of stack
        return result 
        