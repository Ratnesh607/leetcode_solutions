class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n == 0:
            return "0"
            
        ans = []
        separator = 0
        while n:
            digit = n % 10
            ans.append(str(digit))
            separator += 1
            if separator == 3 and n > 9:
                ans.append(".")
                separator = 0
            n //= 10
        return "".join(ans[::-1])
        