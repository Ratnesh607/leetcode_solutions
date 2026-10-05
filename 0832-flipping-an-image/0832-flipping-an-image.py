class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in image:
            l = 0
            r = len(i) - 1
            while l < r:
                i[l], i[r] = i[r], i[l]
                l += 1
                r -= 1
                
            for j in range(len(i)):
                if i[j]:
                    i[j] = 0
                else:
                    i[j] = 1
                
        return image