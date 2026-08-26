class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            freq[i] = freq.get(i, 0) + 1

        Set = set()
        for i in freq:
            Set.add(freq[i])
            
        return len(Set) == len(freq)