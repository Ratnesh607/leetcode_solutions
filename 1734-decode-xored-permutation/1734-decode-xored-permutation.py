class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        x = 0
        for i in range(1, n+1):
            x ^= i
        
        perm = [0] * n
        perm[0] = x
        for i in range(1, n - 1, 2):
            perm[0] ^= encoded[i]
        
        for i in range(1, n):
            perm[i] = perm[i - 1] ^ encoded[i - 1]

        return perm 

        