class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Algo has to be in O(n) time so sorted() will not work here O(nlogn)
        # maybe two pointer
        # Consecutive = 1 + current element
        # If the value is not 1 +, we can move a pointer

        # we don't count duplicates so lets use a hashset

        # What makes the number a start of a sequence? It the number before it is not in
        # the hashset (curr - 1 not in hashSet)
        '''
        hashSet = set(nums) # (2,4,3,5)
        curr = max(hashSet) # 20
        removed = 1
        removed_max = 1

        while len(hashSet) > 1 and curr in hashSet:
            if (curr - 1) in hashSet:
                hashSet.remove(curr) # ()
                removed += 1 # 
                curr -= 1 # 
                
            else:
                hashSet.remove(curr)
                removed = 1
                curr = max(hashSet)
            
            removed_max = max(removed, removed_max)
        
        if len(hashSet) == 1 and (curr - 1) in hashSet:
            removed += 1
            removed_max = max(removed, removed_max)
        
        return removed_max
        '''
        hashSet = set(nums) 
        longest = 0

        for n in nums: 
            if (n-1) not in hashSet:
                length = 0

                while (n + length) in hashSet:
                    length += 1
                longest = max(length, longest)
        return longest

        