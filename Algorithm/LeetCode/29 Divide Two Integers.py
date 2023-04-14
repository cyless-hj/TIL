class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        answer = 0
        sign = 1

        if dividend * divisor < 0:
            sign = -1

        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend - divisor >= 0:
            x = 0
            while dividend - (divisor << 1 << x) > 0:
                x += 1
            dividend -= (divisor << x)
            answer += (2 ** x)

        answer *= sign

        return answer