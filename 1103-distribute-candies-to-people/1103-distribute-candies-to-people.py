class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        ans = [0]*num_people
        i = 1
        while candies >= i:
            ans[(i - 1) % num_people] += i
            candies -= i
            i += 1
        ans[(i - 1) % num_people] += candies
        return ans
        