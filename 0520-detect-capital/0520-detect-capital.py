class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        if ord("A") <= ord(word[0]) <= ord("Z"):
            if ord("A") <= ord(word[1]) <= ord("Z"):
                signal = -1  # for UPERCASE
            else:
                signal = 1 # for Title Case

        else:
            signal = 0  # for all lower case

        for i in range(1, len(word)):
            # for Title Case
            if signal == 1 and  not (ord("a") <= ord(word[i]) <= ord("z")):
                return False

            # for UPERCASE
            if signal == -1 and  not (ord("A") <= ord(word[i]) <= ord("Z")): 
                return False

            # for all lower case
            if signal == 0 and (ord("A") <= ord(word[i]) <= ord("Z")):
                return False

        return True

        