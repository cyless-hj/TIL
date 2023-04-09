class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        n = len(x)
        start, end = '', ''

        if n % 2 == 0:
            start = x[:n // 2]
            end = x[:n // 2 - 1:-1]
        else:
            start = x[:n // 2]
            end = x[:n // 2:-1]
        if start == end:
            return True
        return False