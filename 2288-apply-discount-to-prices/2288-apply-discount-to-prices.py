class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        dis = discount / 100
        res = []
        i = 0
        while i < len(sentence):
            if sentence[i] == "$":
                j = i + 1
                num = 0
                while j < len(sentence) and "0" <= sentence[j] <= "9":
                    num *= 10
                    num += int(sentence[j])
                    j += 1

                if j > i + 1 and (j == len(sentence) or sentence[j] == " "):
                    price = num * (1 - dis)
                    res.append("$" + format(price, ".2f"))
                    i = j
                else:
                    res.append(sentence[i])
                    i += 1
            else:
                res.append(sentence[i])
                i += 1

        return "".join(res)