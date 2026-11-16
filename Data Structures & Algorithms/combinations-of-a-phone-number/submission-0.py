class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        # res = []
        # hashmap of num mapped to letters
        # backtrack(i, curStr):

        # Base Case: if len(curStr) == len(digits): 
            # res.append(curStr)
            # return
        # for l in letters_of_num_at_i:
            # backtrack(i + 1, curStr + l)
        
        res = []
        # hashmap of num mapped to letters
        letterMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
        
            for l in letterMap[digits[i]]:
                backtrack(i + 1, curStr + l)
        if digits:
            backtrack(0, "")
        
        return res
        


        
        