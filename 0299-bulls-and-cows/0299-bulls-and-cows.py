class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        count1 = [0]*10
        count2 = [0]*10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                count1[ord(secret[i])- ord("0")] += 1
                count2[ord(guess[i])-ord("0")] += 1

        for i in range(10):
            cows += min(count1[i], count2[i])
        
        return str(bulls)+"A"+str(cows)+"B"