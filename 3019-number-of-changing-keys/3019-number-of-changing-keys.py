class Solution:
    def countKeyChanges(self, s: str) -> int:
        if "A" <= s[0] <= "Z":
            prev = ord(s[0]) - ord("A")
        else:
            prev = ord(s[0]) - ord("a")
            
        count = 0
        for i in s:
            if "A" <= i <= "Z":
                curr = ord(i) - ord("A")
            else:
                curr = ord(i) - ord("a")

            if prev != curr:
                count += 1
            prev = curr
            
        return count
