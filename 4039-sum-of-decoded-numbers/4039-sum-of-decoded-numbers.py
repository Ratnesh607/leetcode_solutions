class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        Sum = 0
        for i in nums:
            w = i % 10
            d = str(i // 10)
            x = int(d[:w])
            y = int(d[w:])
            Sum = (Sum + pow(x, y, mod)) % mod

        return Sum

            
        