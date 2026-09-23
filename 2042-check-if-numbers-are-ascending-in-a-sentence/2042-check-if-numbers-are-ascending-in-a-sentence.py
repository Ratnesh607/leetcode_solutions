class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        prev = 0
        curr = ""
        for i in range(len(s)):
            if "0" <= s[i] <= "9":
                curr += s[i]
            elif curr:
                curr = int(curr)
                if curr <= prev:
                    return False
                prev = curr
                curr = ""
        if curr and int(curr) <= prev:
            return False
        return True