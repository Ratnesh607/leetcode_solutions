class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        freq = {}
        count = 0
        for i in arr:
            key = i % k
            if key in freq:
                count += 1
                freq[key] -= 1
                if freq[key] == 0:
                    del freq[key]
            else:
                if key:
                    key = k - key
                if key not in freq:
                    freq[key] = 0
                freq[key] += 1
        return count * 2 == len(arr)        