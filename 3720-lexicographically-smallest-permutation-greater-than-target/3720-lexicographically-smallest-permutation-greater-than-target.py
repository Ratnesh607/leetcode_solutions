class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1

        n = len(target)
        matched = 0
        while matched < n:
            idx = ord(target[matched]) - ord('a')
            if count[idx] == 0:
                break
            count[idx] -= 1
            matched += 1

        if matched < n:
            idx = ord(target[matched]) - ord('a')
            for j in range(idx + 1, 26):
                if count[j] > 0:
                    count[j] -= 1
                    ans = target[:matched] + chr(j + ord('a'))
                    for k in range(26):
                        ans += chr(k + ord('a')) * count[k]

                    return ans
        for i in range(matched - 1, -1, -1):
            idx = ord(target[i]) - ord('a')
            count[idx] += 1
            for j in range(idx + 1, 26):
                if count[j] > 0:
                    count[j] -= 1
                    ans = target[:i] + chr(j + ord('a'))
                    for k in range(26):
                        ans += chr(k + ord('a')) * count[k]

                    return ans

        return ""