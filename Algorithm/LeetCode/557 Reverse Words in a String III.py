class Solution:
    def reverseWords(self, s: str) -> str:
        answer = ''
        string = s.split()
        for sp in string:
            answer += sp[::-1] + ' '
        answer = answer[:-1]
        return answer