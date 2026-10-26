class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashTable = defaultdict(list)

        for x in strs:
            count_arr = [0]*26

            for c in x:
                count_arr[ord(c) - ord('a')] += 1
            
            count_arr_tup = tuple(count_arr)

            hashTable[count_arr_tup].append(x)
        return list(hashTable.values())
        
        