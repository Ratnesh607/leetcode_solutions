class Solution:
    def splitSentence(self, sentence: str) -> list:
        words = []
        word = []
        for i in sentence:
            if i != " ":
                word.append(i)
            else:
                word = "".join(word)
                words.append(word)
                word = []
        word = "".join(word)
        words.append(word)

        return words

    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        sentence = self.splitSentence(sentence)
        dictionary = set(dictionary)
        for i in range(len(sentence)):
            word = ""
            for j in range(len(sentence[i])):
                word += sentence[i][j]
                if word in dictionary:
                    sentence[i] = word
                    break

        return " ".join(sentence)
