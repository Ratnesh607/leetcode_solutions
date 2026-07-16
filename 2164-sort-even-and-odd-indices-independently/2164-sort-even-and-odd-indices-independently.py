class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        for i in range(len(nums)):
            if i % 2:
                odd.append(nums[i])
            else:
                even.append(nums[i])
        even.sort()
        odd.sort(reverse = True)

        i = 0
        j = 0
        ans = []
        
        for num in range(len(nums)):
            if num%2:
                ans.append(odd[i])
                i += 1
            else:
                ans.append(even[j])
                j += 1
        return ans