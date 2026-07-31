class Solution:
    def romanToInt(self, s: str) -> int:
        nums = 0
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        prev = 0
        for i in range(len(s)-1,-1,-1):
            if roman[s[i]] < prev:
                nums-= roman[s[i]]
            else:
                nums+= roman[s[i]]
            prev = roman[s[i]]

        return nums
        