class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashMap = {}

        for word in strs:
            sorted_word = "".join(sorted(word)) #nlogn

            if sorted_word in hashMap:
                hashMap[sorted_word].append(word)
            else:
                hashMap[sorted_word] = [word]
        return list(hashMap.values())
        