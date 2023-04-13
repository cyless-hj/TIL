class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        answer = True
        stack = []

        for s in s_list:
            if s in ['[', '(', '{']:
                stack.append(s)
            elif len(stack) != 0:
                if (s == ']' and stack[-1] == '[') or (s == '}' and stack[-1] == '{') or (s == ')' and stack[-1] == '('): 
                    stack.pop()
                else:
                    answer = False
                    break
            else:
                answer = False
                break
                
        if len(stack) != 0:
            answer = False
            
        return answer