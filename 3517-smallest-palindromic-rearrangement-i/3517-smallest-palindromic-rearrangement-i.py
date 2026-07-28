class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = {}        
        n = len(s)
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        ans1 = []
        mid = 0
        for i in sorted(freq):
            if freq[i] % 2:
                mid = i
                freq[i] -= 1
            ans1.extend(i * (freq[i] // 2))

        ans2 = ans1[::-1]
        if mid:
            ans1.append(mid) 
        ans1 += ans2
        return "".join(ans1)        