import heapq

def solution(book_time):
    answer = 1
    book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time.sort(key=lambda x: x[0])
    
    heap = []
    for start, end in book_time:
        if not heap:
            heapq.heappush(heap, end)
            continue
        if heap[0] <= start:
            heapq.heappop(heap)
        else:
            answer += 1
        
        heapq.heappush(heap, end + 10)
    
    return answer