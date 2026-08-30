class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # hashmap: key: sorted array of the word, value: word that has the same sorted form
        hashMap = {}# sorted(s) for s in strs: []}

        for s in strs:
            key = "".join(sorted(s))

            if key in hashMap:
                hashMap.get(key).append(s)
            else:
                hashMap[key] = [s]
        return list(hashMap.values())
        