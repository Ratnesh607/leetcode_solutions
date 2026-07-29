class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half = n // 2

        freq = [0] * 26
        for i in range(half):
            freq[ord(s[i]) - ord('a')] += 1

        def perm(rem):
            acc = 1
            for i in range(26):
                f = freq[i]
                if not f:
                    continue

                if f > rem:
                    return 0

                acc *= comb(rem, f)
                if acc > k:
                    return acc
                rem -= f
            return acc

        left = []
        start = 0
        for i in range(half):
            selected = False
            for j in range(26):
                if not freq[j]:
                    continue

                freq[j] -= 1
                p = perm(half - i - 1)
                if start + p >= k:
                    left.append(chr(j + ord('a')))
                    selected = True
                    break

                freq[j] += 1
                start += p
            if not selected:
                return ""

        left = "".join(left)
        mid = s[half] if n % 2 else ""
        return left + mid + left[::-1]