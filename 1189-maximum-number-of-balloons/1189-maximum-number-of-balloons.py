class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            'b' : 0,
            'a' : 0,
            'l' : 0,
            'o' : 0,
            'n' : 0
        }
        for i in text:
            if i in balloon:
                balloon[i] += 1

        ans = float("inf")
        for i in balloon:
            if i == 'l' or i == 'o':
                balloon[i] //= 2
            ans = min(ans, balloon[i])
        return ans