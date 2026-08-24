class Solution:
    def isValid(self, s: str) -> bool:

        # hashmap mapping open bracket to its closed bracket
        # stack to put close brackets


        stack = []
        closeToOpen = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in closeToOpen:
                if stack and (stack[-1] == closeToOpen[ch]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
            

        