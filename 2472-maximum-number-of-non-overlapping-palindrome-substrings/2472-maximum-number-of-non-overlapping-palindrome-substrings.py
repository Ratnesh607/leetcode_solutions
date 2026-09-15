class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        isPalindrome = [[False] * n for _ in range(n)]
        for L in range(1, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                if i == j:
                    isPalindrome[i][j] = True
                elif i + 1 == j:
                    isPalindrome[i][j] = (s[i] == s[j])
                else:
                    isPalindrome[i][j] = (s[i] == s[j] and isPalindrome[i + 1][j - 1])

        t = [-1] * (n + 1)
        for i in range(k):
            t[i] = 0

        for length in range(k, n + 1):
            result = t[length - 1]
            j = length - 1
            for i in range(length - k + 1):
                if isPalindrome[i][j]:
                    result = max(result, 1 + t[i])

            t[length] = result
        return t[n]