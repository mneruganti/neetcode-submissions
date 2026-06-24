# zxyzzxy
# star at z, move to y, if the two characters are different, we expand window
# if the two characters are the same OR already encountered (hashmap), shrink window
# we go from z -> x -> y, no issues, expand window
# we encounter the second z - move beginning of window to z's location. Start over
# time complexity: O(n)
# space complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = 0
        charSet = set()
        left = 0

        for r in range(len(s)):
            while (s[r] in charSet): # if the current element is in the set
                charSet.remove(s[left])
                left += 1
            charSet.add(s[r]) # if an element is not in the char set, add it (no duplicates)
            length = max(r - left + 1, length)

        return length
        # abc (len = 3) remove a -> bc and now right is at b, left is at pos 1 (first b)