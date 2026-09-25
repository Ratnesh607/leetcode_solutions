class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        self.s = expression
        self.n = len(expression)
        self.idx = 0

        def getUnit():
            result = set()
            if self.s[self.idx] == "{":
                self.idx += 1
                result = performUnion()
            else:
                result = {self.s[self.idx]}
            self.idx += 1
            return result

        def performConcat():
            result = {""}
            while self.idx < self.n and (
                self.s[self.idx] == "{" or self.s[self.idx].isalpha()):
                temp = getUnit()
                concatResult = set()
                for left in result:
                    for right in temp:
                        concatResult.add(left + right)
                result = concatResult
            return result

        def performUnion():
            result = set()
            while True:
                temp = performConcat()
                for i in temp:
                    result.add(i)

                if self.idx < self.n and self.s[self.idx] == ",":
                    self.idx += 1
                else:
                    break

            return result
        st = performUnion()
        return sorted(st)