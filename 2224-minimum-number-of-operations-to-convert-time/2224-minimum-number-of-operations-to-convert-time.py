class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        currentHour = 10 * int(current[0]) + int(current[1])
        currentMinutes = 10 * int(current[3]) + int(current[4])

        correctHour = 10 * int(correct[0]) + int(correct[1])
        correctMinutes = 10 * int(correct[3]) + int(correct[4])

        diff = (correctHour * 60 + correctMinutes) - (currentHour * 60 + currentMinutes)

        count = diff // 60
        diff %= 60

        count += diff // 15
        diff %= 15
        
        count += diff // 5
        diff %= 5
        
        count += diff // 1
        return count