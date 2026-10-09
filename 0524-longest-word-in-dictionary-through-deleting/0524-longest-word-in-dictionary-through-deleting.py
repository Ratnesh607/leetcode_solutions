class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        idx = -1
        for i in range(len(dictionary)):
            j = 0
            k = 0
            while j < len(dictionary[i]) and k < len(s):
                if dictionary[i][j] == s[k]:
                    j += 1
                k += 1
            if j == len(dictionary[i]):
                if idx != -1 and len(dictionary[i]) > len(dictionary[idx]):
                    idx = i
                elif idx != -1 and len(dictionary[i]) == len(dictionary[idx]) and dictionary[i] < dictionary[idx]:
                    idx = i
                if idx == -1:
                    idx = i

        return dictionary[idx] if idx != -1 else ""        