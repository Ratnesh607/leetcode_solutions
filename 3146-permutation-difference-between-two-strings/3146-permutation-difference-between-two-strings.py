class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        ans = 0
        index = [-1]*26
        for i in range(len(s)):
            index[ord(s[i]) - ord("a")] = i
        for i in range(len(t)):
            ans += abs(index[ord(t[i]) - ord("a")] - i)
        return ans