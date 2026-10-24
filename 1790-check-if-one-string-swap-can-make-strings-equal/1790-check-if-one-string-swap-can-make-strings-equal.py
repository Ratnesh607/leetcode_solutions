class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        wrong = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                wrong.append(i)
                if len(wrong) > 2:
                    return False


        if not wrong:
            return True

        if len(wrong) != 2:
            return False

        return s1[wrong[0]] == s2[wrong[1]] and s1[wrong[1]] == s2[wrong[0]]
        