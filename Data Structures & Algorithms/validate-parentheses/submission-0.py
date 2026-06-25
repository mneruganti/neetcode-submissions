class Solution:
    def isValid(self, s: str) -> bool:

        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["} # hashmap for open close pairs

        for c in s: # for each element in the stack
            if c in closeToOpen: # if it is a closing parenthesis

                # make sure stack is valid and make sure value at top
                # is the matching opening parenthesis
                if stack and stack[-1] == closeToOpen[c]:  
                    stack.pop() # pop from stack since we found a pair
                else:
                    return False # not matching means false
            else:
                stack.append(c) # we can add as many open parenthesis as possib;e
        return True if not stack else False # only true if stack is empty
        