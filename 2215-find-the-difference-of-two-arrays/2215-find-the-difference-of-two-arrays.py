class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        freq = {}
        ans = [[], []]

        for i in nums1:
            freq[i] = 1
        
        for i in nums2:
            if i in freq and freq[i] == 1:
                freq[i] = 0
            elif i not in freq:
                freq[i] = -1

        for i in nums1:
            if i in freq and freq[i] == 1:
                ans[0].append(i)
                del freq[i]

        for i in nums2:
            if i in freq and freq[i] == -1:
                ans[1].append(i)
                del freq[i]
        
        return ans