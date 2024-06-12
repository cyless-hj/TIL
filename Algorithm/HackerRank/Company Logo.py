if __name__ == '__main__':
    s = input()
    
    dic = dict.fromkeys(list(s), 0)
    
    for alpha in s:
        dic[alpha] = dic.get(alpha) + 1
        
    arr = list(dic.items())
    arr.sort(key=lambda x: (-x[1], x[0]))
        
    for i in range(3):
        print(f"{arr[i][0]} {arr[i][1]}")