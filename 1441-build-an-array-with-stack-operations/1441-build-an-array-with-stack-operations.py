class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        s = []
        count = 0
        for i in target:
            for j in range(count, i - 1):
                s.append("Push")
                s.append("Pop")
            s.append("Push")
            count = i
        return s
