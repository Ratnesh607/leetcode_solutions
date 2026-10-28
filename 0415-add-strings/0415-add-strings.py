class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        ans = []
        carry = 0
        i = -1
        while i >= -len(num1) or i >= -len(num2) or carry:
            a = int(num1[i]) if i >= -len(num1) else 0
            b = int(num2[i]) if i >= -len(num2) else 0

            total = a + b + carry
            ans.append(str(total % 10))
            carry = total // 10
            i -= 1

        return "".join(ans[::-1])
        