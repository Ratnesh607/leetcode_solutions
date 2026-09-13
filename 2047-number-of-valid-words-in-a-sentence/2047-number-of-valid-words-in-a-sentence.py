class Solution:
    def countValidWords(self, sentence: str) -> int:
        word = []
        count = 0
        for i in sentence:
            if i != " ":
                word.append(i)
            elif not word:
                continue

            else:
                signal = True
                hyphen = 0
                for j in range(len(word)):
                    if "0" <= word[j] <= "9":
                        signal = False
                        break

                    if word[j] == "-":
                        hyphen += 1
                        if hyphen > 1:
                            signal = False
                            break

                        if j == 0 or j == len(word) - 1:
                            signal = False
                            break

                        if not ("a" <= word[j - 1] <= "z"):
                            signal = False
                            break

                        if not ("a" <= word[j + 1] <= "z"):
                            signal = False
                            break

                    if word[j] in ("!", ".", ","):
                        if j != len(word) - 1:
                            signal = False
                            break

                if signal:
                    count += 1
                word = []

        if word:
            signal = True
            hyphen = 0
            for j in range(len(word)):
                if "0" <= word[j] <= "9":
                    signal = False
                    break

                if word[j] == "-":
                    hyphen += 1
                    if hyphen > 1:
                        signal = False
                        break

                    if j == 0 or j == len(word) - 1:
                        signal = False
                        break

                    if not ("a" <= word[j - 1] <= "z"):
                        signal = False
                        break

                    if not ("a" <= word[j + 1] <= "z"):
                        signal = False
                        break

                if word[j] in ("!", ".", ","):
                    if j != len(word) - 1:
                        signal = False
                        break

            if signal:
                count += 1
        return count