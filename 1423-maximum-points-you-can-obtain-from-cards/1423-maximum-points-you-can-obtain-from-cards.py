class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = len(cardPoints)
        prev = 0
        total = 0
        for i in range (k):
            prev += cardPoints[i]
        for i in range((l-k),l):
            total += cardPoints[i]
        if prev < total:
            prev = total
        for i in range((l-k+1),l):
            total += cardPoints[(i+k-1)%l]
            total -= cardPoints[i-1]
            if prev < total:
                prev = total  
        return prev       
        