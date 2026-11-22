class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        Set = set()
        count = 0
        for i in words:
            if i in Set:
                count += 1
            else:
                s = i[1] + i[0]
                Set.add(s)
        return count
