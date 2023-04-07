def solution(players, callings):
    answer = []
    name = {}
    rank = {}
    for idx, p in enumerate(players):
        rank[p] = idx + 1
        name[idx + 1] = p
    for call in callings:
        pre_rank = rank[call]
        post_rank = rank[call] - 1
        change_player = name[post_rank]
        
        name[pre_rank], name[pre_rank - 1] = name[pre_rank - 1], name[pre_rank]
        rank[call], rank[change_player] = rank[change_player], rank[call]
    answer = list(name.values())
    return answer