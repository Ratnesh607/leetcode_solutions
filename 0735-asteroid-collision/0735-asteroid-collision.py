class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(asteroids):
            if ans == []:
                ans.append(asteroids[i])
                i += 1
            elif asteroids[i] < 0 and ans[-1] > 0:
                if abs(asteroids[i]) < ans[-1]:
                    i += 1
                elif abs(asteroids[i]) > ans[-1]:
                    ans.pop()
                else:
                    ans.pop()
                    i += 1
            else:
                ans.append(asteroids[i])
                i += 1
        return ans