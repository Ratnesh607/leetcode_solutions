class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            freq = {}
            for i in s:
                freq[i] = freq.get(i, 0) + 1
                if freq[i] == 2:
                    return True

            return False

        wrong = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                wrong.append(i)
                if len(wrong) > 2:
                    return False

        if len(wrong) != 2:
            return False

        return s[wrong[0]] == goal[wrong[1]] and s[wrong[1]] == goal[wrong[0]]
        