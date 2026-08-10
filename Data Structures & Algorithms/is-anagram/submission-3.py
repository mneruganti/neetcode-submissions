class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # O(nlogk) solution: return sorted(s) == sorted(t)

        if len(s) != len(t): return False

        hashMap1 = {}
        hashMap2 = {}

        for i in range(len(s)):

            hashMap1[s[i]] = hashMap1.get(s[i], 0) + 1
            hashMap2[t[i]] = hashMap2.get(t[i], 0) + 1

        return hashMap1 == hashMap2
        