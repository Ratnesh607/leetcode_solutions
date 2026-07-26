class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 3:
            return 1
        s = [1,2,2]
        status = True
        i = 2
        count = 1
        while len(s) < n:
            if status:
                for j in range(s[i]):
                    s.append(1)
                    if len(s) <= n:
                        count += 1
            else:
                for j in range(s[i]):
                    s.append(2)
            i += 1
            status = not status

        return count
        
        