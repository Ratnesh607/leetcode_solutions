class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = "aeiouAEIOU"
        vowel = False
        consonant = False
        for i in word:
            if not i.isalpha() and not i.isdigit():
                return False

            if i in vowels:
                vowel = True
            elif i.isalpha():
                consonant = True

        return vowel and consonant