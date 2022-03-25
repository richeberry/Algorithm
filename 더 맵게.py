# Programmers _ Lv.2 더 맵게 (heap)

import heapq

def solution(scoville, k):
    cnt = 0
    sco = [] # 빈 리스트에 힙을 넣고 빼면서 게산

    for i in scoville:
        heapq.heappush(sco,i)
    
    while sco[0] < k:
        try:
            heapq.heappush(sco, heapq.heappop(sco) + heapq.heappop(sco)*2)
        except IndexError:
                return -1
        cnt += 1
    return cnt



'''
# 몇몇 테스트 실패

scoville = [1, 2, 3, 9, 10, 12]
k = 7

def solution(scoville, k):
    cnt = 0
    while scoville[0] < k:
        try:
            scoville.sort()
            mix = scoville[0] + (scoville[1]*2)
            scoville.pop(0)
            scoville.pop(0)
            scoville[0] = mix
            cnt += 1
        except IndexError:
            return -1

    return cnt
'''