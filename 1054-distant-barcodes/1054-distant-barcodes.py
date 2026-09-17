class Solution:
    def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
        freq = {}
        for i in barcodes:
            freq[i] = freq.get(i, 0) + 1

        freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        ans = [0] * len(barcodes)
        i = 0
        for j in freq:
            for k in range(j[1]):
                ans[i] = j[0]
                i += 2
                if i >= len(barcodes):
                    i = 1
        return ans
        