from math import sqrt

def solution(begin, end):
    answer = [0] * (end - begin + 1)
    is_odd = begin % 2 == 1
    
    for num in range(begin, end + 1):
    	i = num - begin
    	
    	division = 1
    	s = int(sqrt(num))
    	for j in range(2, s + 1):
    		divider = num // j
    		if num % j == 0:
    			if divider <= 10000000:
    				division = divider
    				break
    			else:
    				division = j
    	
    	answer[i] = division
    	is_odd = not is_odd
    
    if begin == 1:
    	answer[0] = 0
    return answer