class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        reverse = True
        i = 1
        while time > 0:
            if i == n:
                reverse = False
            if i == 1:
                reverse = True
            if reverse:
                i += 1
            else:
                i -= 1
            time -= 1
        return i       