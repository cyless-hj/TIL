def solution(data, ext, val_ext, sort_by):
    key_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    
    answer = [x for x in data if x[key_dict.get(ext)] < val_ext]
    answer.sort(key = lambda x : (x[key_dict.get(sort_by)]))

    return answer