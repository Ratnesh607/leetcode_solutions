class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = [False]*26
        for i in sentence:
            seen[ord(i) - ord("a")] = True
            
        for i in seen:
            if not i:
                return False
        return True
        