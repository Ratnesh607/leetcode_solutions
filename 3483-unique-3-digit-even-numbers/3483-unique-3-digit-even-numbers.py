class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digitFreq = [0] * 10
        count = 0
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
                    count += 1
                
                digitFreq[j] += 1
            digitFreq[i] += 1
        return count
        