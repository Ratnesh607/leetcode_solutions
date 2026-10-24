class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        aMonthAlice = 10 * int(arriveAlice[0]) + int(arriveAlice[1])
        aDateAlice = 10 * int(arriveAlice[3]) + int(arriveAlice[4])
        lMonthAlice = 10 * int(leaveAlice[0]) + int(leaveAlice[1])
        lDateAlice = 10 * int(leaveAlice[3]) + int(leaveAlice[4])

        aMonthBob = 10 * int(arriveBob[0]) + int(arriveBob[1])
        aDateBob = 10 * int(arriveBob[3]) + int(arriveBob[4])
        lMonthBob = 10 * int(leaveBob[0]) + int(leaveBob[1])
        lDateBob = 10 * int(leaveBob[3]) + int(leaveBob[4])

        aMonthAlice = sum(month[:aMonthAlice - 1]) + aDateAlice
        lMonthAlice = sum(month[:lMonthAlice - 1]) + lDateAlice
        aMonthBob = sum(month[:aMonthBob - 1]) + aDateBob
        lMonthBob = sum(month[:lMonthBob - 1]) + lDateBob

        start = max(aMonthAlice, aMonthBob)
        end = min(lMonthAlice, lMonthBob)
        return max(0, end - start + 1)