class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        result = []
        digitFreq = [0] * 10
        for i in digits:
            digitFreq[i] += 1

        for i in range(1,10):
            if digitFreq[i] == 0:
                continue
            digitFreq[i] -= 1

            for j in range(10):
                if digitFreq[j] == 0:
                    continue
                digitFreq[j] -= 1

                for k in range(0,9,2):
                    if digitFreq[k] == 0:
                        continue
                    result.append(i*100+j*10+k)
                    
                digitFreq[j] += 1
            digitFreq[i] += 1
        return result