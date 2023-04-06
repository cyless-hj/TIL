class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            tmp = str(n)
            total = 0
            for i in range(len(tmp)):
                visited.add(int(tmp[i]))
                total += int(tmp[i])**2
            n = total
            if total == 1:
                return True
            if total in visited:
                return False