from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    total = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length)
    while truck_weights:
        answer += 1
        total -= bridge[0]
        bridge.popleft()
        if total + truck_weights[0] > weight:
            bridge.append(0)
        else:
            wei = truck_weights.popleft()
            total += wei
            bridge.append(wei)
    answer += bridge_length
            
    return answer