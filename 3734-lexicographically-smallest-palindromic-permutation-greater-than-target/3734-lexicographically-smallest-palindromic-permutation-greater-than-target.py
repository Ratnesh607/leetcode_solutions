class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        midChar = ""
        for i in range(26):
            if count[i] % 2 == 1:
                if midChar:
                    return ""
                midChar = chr(i + ord('a'))

        half = len(s) // 2
        halfCount = [0] * 26
        for i in range(26):
            halfCount[i] = count[i] // 2

        curr = []
        def build_smallest():
            while len(curr) < half:
                for ch in range(26):
                    if halfCount[ch] == 0:
                        continue
                    curr.append(chr(ch + ord('a')))
                    halfCount[ch] -= 1
                    break

            left = ''.join(curr)
            right = left[::-1]

            if midChar:
                return left + midChar + right
            return left + right

        def solve(i):
            if i == half:
                left = ''.join(curr)
                right = left[::-1]
                if midChar:
                    candidate = left + midChar + right
                else:
                    candidate = left + right

                if candidate > target:
                    return candidate

                return ""
            targetIdx = ord(target[i]) - ord('a')

            for ch in range(targetIdx, 26):
                if halfCount[ch] == 0:
                    continue
                curr.append(chr(ch + ord('a')))
                halfCount[ch] -= 1
                if ch == targetIdx:
                    result = solve(i + 1)
                    if result:
                        return result
                else:

                    result = build_smallest()
                    if result > target:
                        return result

                    for c in curr[i + 1:]:
                        halfCount[ord(c) - ord('a')] += 1
                    del curr[i + 1:]
                curr.pop()
                halfCount[ch] += 1
            return ""
        return solve(0)