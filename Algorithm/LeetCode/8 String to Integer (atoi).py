class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        string = ''
        answer = 0
        for i in s:
            if not string:
                if i.isdigit() or i in ['-','+']:
                    string = i
                else:
                    break
            else:
                if i.isdigit():
                    string += i
                else:
                    break
        
        if not string or string in ['-','+']:
            pass
        elif int(string) < -(2 ** 31):
            answer = -(2 ** 31)
        elif int(string) > (2 ** 31) - 1:
            answer = (2 ** 31) - 1
        else:
            answer = int(string)
        
        return answer