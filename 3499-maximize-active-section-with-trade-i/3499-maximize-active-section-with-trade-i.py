class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        countActive = 0
        for i in s:
            if i == "1":
                countActive += 1

        n = len(s)
        inactiveBlocks = []
        i = 0
        while i < n:
            if s[i] == "0":
                temp = i
                while i < n and s[i] == "0":
                    i += 1
                inactiveBlocks.append(i - temp)
            else:
                i += 1
                
        maxInactive = 0
        for i in range(len(inactiveBlocks) - 1):
            maxInactive = max(maxInactive, inactiveBlocks[i] + inactiveBlocks[i + 1])

        return maxInactive + countActive