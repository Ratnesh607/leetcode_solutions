class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Set = set()
        for i in nums:
            if i not in Set:
                Set.add(i)
            else:
                return True
                break
        else:
            return False  
        
