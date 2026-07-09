class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for i in strs:
            temp = 0
            for j in i:
                if ord(j) >= ord("a"):
                    temp = len(i)
                    break
                else:
                    temp *= 10
                    temp += ord(j) - ord("0")
            ans = max(ans, temp)
        return ans
