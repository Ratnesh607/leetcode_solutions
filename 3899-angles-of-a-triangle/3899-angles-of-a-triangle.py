class Solution:
    def internalAngles(self, sides: list[int]) -> list[float]:
        sides.sort()
        a,b,c = sides
        if a + b <= c:
            return []

        angle_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
        angle_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
        angle_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

        return [math.degrees(angle_A), math.degrees(angle_B), math.degrees(angle_C)]