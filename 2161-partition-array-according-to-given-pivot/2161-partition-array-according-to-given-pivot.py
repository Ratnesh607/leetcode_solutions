class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        minArr = []
        maxArr = []
        eqArr = []
        for i in nums:
            if i < pivot:
                minArr.append(i)
            elif i == pivot:
                eqArr.append(i)
            else:
                maxArr.append(i)
        return minArr + eqArr + maxArr
        