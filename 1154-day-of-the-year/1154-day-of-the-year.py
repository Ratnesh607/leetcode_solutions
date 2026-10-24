class Solution:
    def dayOfYear(self, date: str) -> int:
        months = [31,28,31,30,31,30,31,31,30,31,30,31]
        year = 1000 * int(date[0]) + 100 * int(date[1]) + 10 * int(date[2]) + int(date[3])
        if year % 4 == 0 and year != 1900:
            months[1] += 1

        month = 10 * int(date[5]) + int(date[6])
        return sum(months[:month - 1]) + (10 * int(date[8]) + int(date[9]))