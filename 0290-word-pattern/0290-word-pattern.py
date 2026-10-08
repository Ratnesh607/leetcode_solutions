class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = []
        word = []
        for i in s:
            if i == " ":
                word = "".join(word)
                words.append(word)
                word = []
            else:
                word.append(i)
        word = "".join(word)
        words.append(word)

        n = len(words)
        if len(pattern) != n:
            return False

        dict1 = {}
        dict2 = {}
        for i in range(n):
            if words[i] not in dict1:
                dict1[words[i]] = pattern[i]
            
            if pattern[i] not in dict2:
                dict2[pattern[i]] = words[i]

            if dict1[words[i]] != pattern[i] or dict2[pattern[i]] != words[i]:
                return False

        return True    