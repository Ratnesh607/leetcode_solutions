class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = 0
        count = 0
        char = chars[0]
        for i in range(n):
            if char == chars[i]:
                count += 1
            else:
                chars[l] = char
                l += 1
                if count > 1:
                    for digit in str(count):
                        chars[l] = digit
                        l += 1
                count = 1
                char = chars[i]

        chars[l] = char
        l += 1
        if count > 1:
            for digit in str(count):
                chars[l] = digit
                l += 1

        return l