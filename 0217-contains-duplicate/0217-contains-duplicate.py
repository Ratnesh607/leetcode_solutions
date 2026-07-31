class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Dict = set()
        for i in nums:
            if i not in Dict:
                Dict.add(i)
            else:
                return True
                break
        else:
            return False  
        