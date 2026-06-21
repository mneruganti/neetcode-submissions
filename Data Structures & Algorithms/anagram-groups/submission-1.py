class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashList = {}

        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in hashList:
                hashList[sorted_word].append(word)
            else:
                hashList[sorted_word] = [word] 
        
        return list(hashList.values())