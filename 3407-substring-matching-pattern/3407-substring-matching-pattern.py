class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        if p == "*":
            return True

        first = []
        second = []
        signal = True
        for i in p:
            if i == "*":
                signal = False
            elif signal:
                first.append(i)
            else:
                second.append(i)

        first = "".join(first)
        second = "".join(second)
        i = 0
        while i <= len(s) - len(first):
            j = 0
            while j < len(first) and s[i + j] == first[j]:
                j += 1
            if j == len(first):
                if not second:
                    return True

                k = i + len(first)
                while k <= len(s) - len(second):
                    j = 0
                    while j < len(second) and s[k + j] == second[j]:
                        j += 1

                    if j == len(second):
                        return True

                    k += 1
            i += 1
        return False