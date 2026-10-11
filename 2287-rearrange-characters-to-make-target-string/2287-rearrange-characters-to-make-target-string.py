class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        freq1 = {}
        freq2 = {}
        for i in target:
            freq1[i] = freq1.get(i, 0) + 1
            freq2[i] = freq2.get(i, 0)

        for i in s:
            if i in freq2:
                freq2[i] += 1

        ans = float("inf")
        for i in freq2:
            freq2[i] //= freq1[i]
            ans = min(ans, freq2[i])

        return ans
        