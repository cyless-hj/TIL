from itertools import permutations
from collections import deque

def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(expression, oper):
    num = deque()
    tmp = ''
    for s in expression:
        if s.isdigit():
            tmp += s
        else:
            num.append(tmp)
            tmp = ''
            num.append(s)
    num.append(tmp)
    
    for o in oper:
        queue = deque()
        while len(num) != 0:
            tmp = num.popleft()
            if tmp == o:
                queue.append(operation(queue.pop(), num.popleft(), o))
            else:
                queue.append(tmp)
        num = queue
            
    return abs(int(queue[0]))
    
def solution(expression):
    answer = []
    oper = ['+', '-', '*']
    oper = list(permutations(oper, 3))
    for i in oper:
        answer.append(calculate(expression, i))
    return max(answer)