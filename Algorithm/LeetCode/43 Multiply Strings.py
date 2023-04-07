class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        def sTon(str_num):
            num = 0
            for idx, n in enumerate(str_num[::-1]):
                num += pow(10, idx) * dic[n]
            return num
        return str(sTon(num1) * sTon(num2))