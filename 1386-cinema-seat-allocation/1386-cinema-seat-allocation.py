class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = {}
        for i in reservedSeats:
            if i[1] == 1 or i[1] == 10:
                continue
            if i[0] not in seats:
                seats[i[0]] = [True, True, True]

            if i[1] < 6 and seats[i[0]][0]:
                seats[i[0]][0] = False

            if 3 < i[1] < 8 and seats[i[0]][1]:
                seats[i[0]][1] = False

            if 5 < i[1] and seats[i[0]][2]:
                seats[i[0]][2] = False

        count = (n - len(seats)) * 2
        for i in seats:
            if seats[i][0] or seats[i][1] or seats[i][2]:
                count += 1

        return count
