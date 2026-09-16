class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        def findPower(a, b):
            if b == 0:
                return 1

            half = findPower(a, b // 2)
            result = (half * half) % MOD
            if b % 2 == 1:
                result = (result * a) % MOD

            return result
        size = n + k
        fact = [1] * size
        invFact = [1] * size
        for i in range(2, size):
            fact[i] = (fact[i - 1] * i) % MOD

        invFact[size - 1] = findPower(fact[size - 1], MOD - 2)
        for i in range(size - 2, -1, -1):
            invFact[i] = (invFact[i + 1] * (i + 1)) % MOD

        N = n + k - 1
        R = 2 * k
        result = fact[N]
        result = (result * invFact[R]) % MOD
        result = (result * invFact[N - R]) % MOD

        return result