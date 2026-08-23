class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        for i in words:
            k = 0
            for j in i:
                if pref[k] != j:
                    break
                k += 1
                if k == len(pref):
                    count += 1
                    break
        return count