class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
            
        ans = []
        carry = 0
        k = 0
        for i in range(len(num1) - 1, -1, -1):
            carry = 0
            a = int(num1[i])
            temp = k

            for j in range(len(num2) - 1, -1, -1):
                b = int(num2[j])
                if len(ans) > temp:
                    total = int(ans[temp]) + (a * b) + carry
                    ans[temp] = str(total % 10) 
                else:
                    total = a * b + carry
                    ans.append(str(total % 10))
                temp += 1
                carry = total // 10

            while carry:
                if len(ans) > temp:
                    total = int(ans[temp]) + carry
                    ans[temp] = str(total % 10) 
                else:
                    total = carry
                    ans.append(str(total % 10))
                carry = total // 10
                temp += 1

            k += 1

        return "".join(ans[::-1])
        