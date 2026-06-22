class Solution:
    def isPalindrome(self, s: str) -> bool:

        if len(s) == 0: return True

        str_arr = [char for char in s.lower() if char.isalnum()]
        left, right = 0, (len(str_arr) - 1)

        while (left < right):
            if (str_arr[left] != str_arr[right]):
                return False
            right -= 1
            left += 1
        
        return True
        