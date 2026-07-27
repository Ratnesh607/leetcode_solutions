class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)
        for i in shifts:
            if i[2] == 1:
                diff[i[0]] += 1
                diff[i[1] + 1] -= 1
            else:
                diff[i[0]] -= 1
                diff[i[1] + 1] += 1

        shift = 0
        s = list(s)
        for i in range(n):
            shift += diff[i]
            char = (ord(s[i]) - ord('a') + shift) % 26
            s[i] = chr(char + ord('a'))

        return "".join(s)