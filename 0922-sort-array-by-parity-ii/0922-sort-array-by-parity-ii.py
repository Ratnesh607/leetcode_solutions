class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd = 1
        for even in range(0, len(nums), 2):
            if nums[even] % 2:
                while nums[odd] % 2:
                    odd += 2

                nums[even], nums[odd] = nums[odd], nums[even]
                
        return nums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # i = 0
        # ans = [0]*len(nums)
        # even = 0
        # odd = 1
        # while i < len(nums):
        #     if nums[i]%2 == 0:
        #         ans[even] = nums[i]
        #         even += 2
        #     else:
        #         ans[odd] = nums[i]
        #         odd += 2
        #     i += 1
        # return ans
        