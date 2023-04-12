class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            answer = int(str(x)[::-1])
        else:
            answer = -1 * int(str(x)[:0:-1])
        
        if answer not in range(-2**31, 2**31):
            answer = 0
        return answer