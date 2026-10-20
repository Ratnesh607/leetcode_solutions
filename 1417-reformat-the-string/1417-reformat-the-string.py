class Solution:
    def reformat(self, s: str) -> str:
        Digit = [0]*10
        Letter = [0]*26
        countDigit = 0
        countLetter = 0
        for i in s:
            if ord("0") <= ord(i) <= ord("9"):
                Digit[ord(i) - ord("0")] += 1
                countDigit += 1
            else:
                Letter[ord(i) - ord("a")] += 1
                countLetter += 1

        if abs(countLetter - countDigit) > 1:
            return ""

        result = []
        if abs(countLetter - countDigit) == 0:
            i = 0
            j = 0
            while countLetter:
                while i < 10 and not Digit[i]:
                    i += 1
                while j < 26 and not Letter[j]:
                    j += 1

                result.append(chr(i + ord("0")))
                Digit[i] -= 1
                result.append(chr(j + ord("a")))
                Letter[j] -= 1
                countLetter -= 1
            
            return "".join(result)

        if countLetter > countDigit:
            i = 0
            j = 0
            while j < 26 and not Letter[j]:
                j += 1
            result.append(chr(j + ord("a")))
            Letter[j] -= 1
            while countDigit:
                while i < 10 and not Digit[i]:
                    i += 1
                while j < 26 and not Letter[j]:
                    j += 1

                result.append(chr(i + ord("0")))
                Digit[i] -= 1
                result.append(chr(j + ord("a")))
                Letter[j] -= 1
                countDigit -= 1
            
            return "".join(result)

        if countLetter < countDigit:
            i = 0
            j = 0
            while i < 10 and not Digit[i]:
                i += 1
            result.append(chr(i + ord("0")))
            Digit[i] -= 1
            while countLetter:
                while i < 10 and not Digit[i]:
                    i += 1
                while j < 26 and not Letter[j]:
                    j += 1

                result.append(chr(j + ord("a")))
                Letter[j] -= 1
                result.append(chr(i + ord("0")))
                Digit[i] -= 1
                countLetter -= 1
            
            return "".join(result)

                
