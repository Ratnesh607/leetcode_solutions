class Solution:
    def canWinNim(self, n: int) -> bool:
        if n <= 3 or n % 4 != 0:
            return True
        return False

        