class Solution:
    def reformat(self, s: str) -> str:
        Digit = []
        Letter = []
        for i in s:
            if i.isdigit():
                Digit.append(i)
            else:
                Letter.append(i)

        if abs(len(Digit) - len(Letter)) > 1:
            return ""

        if len(Digit) > len(Letter):
            Digit, Letter = Letter, Digit

        ans = []
        for i in range(len(Digit)):
            ans.append(Letter[i])
            ans.append(Digit[i])

        if len(Letter) > len(Digit):
            ans.append(Letter[-1])
        return "".join(ans)
                
