class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:
        banned = {}
        for i in bannedWords:
            banned[i] = True
        count = 0
        for i in message:
            if i in banned:
                count += 1
            if count == 2:
                return True
        return False
        