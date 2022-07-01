# 무지의 먹방 라이브


def solution(food_times, k):
    from collections import deque

    data = deque()

    for i in food_times:
        data.append(i)


    for i in range(k):
        data[0] -= 1
        data.rotate(-1)
        if data[0] == 0:
            data.popleft()

    return data[0]