class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        set3 = set(nums3)
        ans1 = set()
        ans2 = set()
        for i in set1:
            if i in set2 and i in set3:
                ans1.add(i)
            elif i in set2 or i in set3:
                ans2.add(i)

        for i in set2:
            if i in set1 and i in set3:
                ans1.add(i)
            elif i in set1 or i in set3:
                ans2.add(i)

        return list(ans1) + list(ans2)
        