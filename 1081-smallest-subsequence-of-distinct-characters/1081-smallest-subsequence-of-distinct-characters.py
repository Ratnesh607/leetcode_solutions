class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1

        res = []
        visited = set()

        for i in s:
            freq[i] -= 1
            if i in visited:
                continue

            while res and res[-1] > i and freq[res[-1]] > 0:
                visited.remove(res.pop())

            res.append(i)
            visited.add(i)

            
        return "".join(res)
