class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        freq1 = [0]*26
        for i in chars:
            freq1[ord(i) - ord("a")] += 1

        ans = 0
        for i in words:
            n = len(i)
            if n > len(chars):
                continue

            freq2 = [0]*26
            for j in range(n):
                idx = ord(i[j]) - ord("a")
                freq2[idx] += 1
                if not freq1[idx] or freq2[idx] > freq1[idx]:
                    break

                if j == n - 1:
                    ans += n
                    
        return ans