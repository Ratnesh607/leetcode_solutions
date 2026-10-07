class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq1 = {}
        freq2 = {}
        ans1 = 0
        ans2 = 0        
        for i in nums1:
            freq1[i] = freq1.get(i, 0) + 1

        for i in nums2:
            if i in freq1:
                ans1 += freq1[i]
                del freq1[i]
            freq2[i] = freq2.get(i, 0) + 1

        for i in nums1:
            if i in freq2:
                ans2 += freq2[i]
                del freq2[i]

        return [ans1, ans2]