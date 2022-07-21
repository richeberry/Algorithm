# Programmers _ Lv2 _ 주식 가격


# deque

def solution(prices):
    
    from collections import deque

    queue = deque(prices)
    answer = []

    while queue:
        cnt = 0
        now = queue.popleft()
        for q in queue:
            cnt += 1
            if now > q:
                break
        answer.append(cnt)

    return answer

