class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = [0]*26
        dists = 0
        for i in s:
            if freq[ord(i) - ord("a")] == 0:
                dists += 1
            freq[ord(i) - ord("a")] += 1

        freq.sort()
        count = 0
        delete = dists - k
        for i in freq:
            if delete <= 0:
                break
            if i:
                count += i
                delete -= 1

        return count