class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        freq = [0]*26
        l = 0
        answer = 0
        for i in range(len(s)):
            freq[ord(s[i])-ord("a")] +=1
            while (freq[ord(s[i])-ord("a")] >2):
                freq[ord(s[l])-ord("a")] -=1
                l+=1
            answer = max(answer, i-l+1)
        return answer