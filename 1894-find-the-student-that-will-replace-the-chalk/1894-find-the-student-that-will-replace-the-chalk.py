class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        k %= total
        
        for i in range(len(chalk)):
            if chalk[i] > k:
                return i
            k -= chalk[i]