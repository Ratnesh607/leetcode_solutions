class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result = []
        
        sum = 0
        if k>0:
            l=1
            r=k
            for i in range(l,r+1):
                sum += code[i]

            for i in range(len(code)):
                result.append(sum)
                sum -= code[l%len(code)]
                l+=1
                r+=1
                sum += code[r%len(code)]
            
        elif k<0:
            l=len(code)-abs(k)
            r=len(code)-1
            for i in range(l,r+1):
                sum += code[i]

            for i in range(len(code)):
                result.append(sum)
                sum -= code[l%len(code)]
                l+=1
                r+=1
                sum += code[r%len(code)]
        else:
            result = [i*0 for i in range(len(code)) ]
        
        # for i in range()
            

        return result
            