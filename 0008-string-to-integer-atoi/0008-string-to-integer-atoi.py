class Solution:
    def myAtoi(self, s: str) -> int:
        num = 0
        sign = 1
        started = False
        for i in s:
            if i == " " and not started:
                continue

            if (i == "-" or i == "+") and not started:
                started = True
                if i == "-":
                    sign = -1
                continue

            if ord("0") <= ord(i) <= ord("9"):
                started = True
                num *= 10
                num += int(i)

            else:
                break

        num *= sign
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num
