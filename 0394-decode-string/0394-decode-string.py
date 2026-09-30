class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        word = ""
        for i in s:
            if "0" <= i <= "9":
                num = num * 10 + int(i)

            elif i == "[":
                stack.append((word, num))
                word = ""
                num = 0

            elif i == "]":
                prev, count = stack.pop()
                word = prev + word * count

            else:
                word += i
        return word