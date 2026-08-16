class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        rem = 0
        for i in word:
            rem *= 10
            rem += ord(i) - ord("0")
            rem %= m
            if rem:
                ans.append(0)
            else:
                ans.append(1)
        return ans      