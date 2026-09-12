class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        m = len(bank)
        n = len(bank[0])
        count = 0
        prev = 0
        for i in bank:
            current = 0
            for j in i:
                if j == "1":
                    current += 1
            count += current * prev
            if current != 0:
                prev = current

        return count
        