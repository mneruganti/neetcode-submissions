class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string_1 = {}
        string_2 = {}

        for ch in s:
            if ch in string_1:
                string_1[ch] = string_1[ch] + 1
            else:
                string_1[ch] = 1
        
        for ch in t:
            if ch in string_2:
                string_2[ch] = string_2[ch] + 1
            else:
                string_2[ch] = 1
        
        return string_1 == string_2