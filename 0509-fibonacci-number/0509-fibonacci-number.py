class Solution:
    def fib(self, n: int) -> int:
        if n < 1:
            return 0

        first = 0
        second = 1
        n -= 1
        while n:
            first, second = second, first + second
            n -= 1

        return second
        
          