class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        decreases = 0
        ans = 0

        while happiness and k > 0:
            temp = happiness.pop() - decreases
            if temp > 0:
                ans += temp

            decreases += 1
            k -= 1
        return ans       