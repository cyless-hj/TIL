class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        answer = 0
        dic = {}
        for task in tasks:
            dic[task] = dic.get(task, 0) + 1
        
        cnt_list = list(dic.values())
        max_cnt = max(cnt_list)
        max_cnt_cnt = cnt_list.count(max_cnt)
        answer = max_cnt + (max_cnt - 1) * n + max_cnt_cnt - 1
        return max(answer, len(tasks))