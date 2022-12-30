def solution(nums):
    answer = 0
    pon_len = len(nums) // 2
    uniq = set(nums)
    if len(uniq) <= pon_len:
        answer = len(uniq)
    else:
        answer = pon_len
    return answer