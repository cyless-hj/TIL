from collections import defaultdict

def solution(X, Y):
    answer = ''
    dic_x = defaultdict(int)
    dic_y = defaultdict(int)

    for n in X:
        dic_x[n] += 1

    for n in Y:
        dic_y[n] += 1

    intersection = set(dic_x.keys()) & set(dic_y.keys())

    strings = ""
    for n in list(intersection):
        count = min(dic_x[n], dic_y[n])
        strings += n * count

    result = sorted(strings, reverse = True)

    if not result:
        return "-1"

    if result[0] == "0":
        return "0"
    
    answer = "".join(result)

    return answer