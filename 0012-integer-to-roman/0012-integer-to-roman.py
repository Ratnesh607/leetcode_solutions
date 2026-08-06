class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        value = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        i = 0
        ans = []
        while num:
            temp = num // value[i]
            if temp:
                while temp:
                    ans.append(roman[i])
                    temp -= 1
                num %= value[i]
            i += 1
            
        return "".join(ans)
        
        