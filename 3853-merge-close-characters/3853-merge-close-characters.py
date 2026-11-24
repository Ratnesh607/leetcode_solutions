class Solution:
    def mergeCharacters(self, s: str, k: int) -> str:
        letters = [-1]*26
        ans = []
        idx = 0
        for i in range(len(s)):
            curr = ord(s[i]) - ord("a")
            if letters[curr] == -1 or idx - letters[curr] > k:
                ans.append(s[i])
                letters[curr] = idx
                idx += 1
                
        return "".join(ans)
