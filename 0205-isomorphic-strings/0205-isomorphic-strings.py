class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        dict1 = {}
        dict2 = {}
        for i in range(n):
            if s[i] not in dict1:
                dict1[s[i]] = t[i]
            
            if t[i] not in dict2:
                dict2[t[i]] = s[i]

            if dict1[s[i]] != t[i] or dict2[t[i]] != s[i]:
                return False

        return True
        