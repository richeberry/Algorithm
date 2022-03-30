# 기능 개발

progresses = [93, 30, 55] # 작업의 진도 _ 각 기능은 진도가 100%일 때 서비스에 반영
speeds = [1, 30, 5] # 작업의 개발 속도
# 각 배포마다 몇 개의 기능이 배포되는지 

# -> 배포에 얼마나 날짜가 걸리는지는 상관 없음

import heapq
from collections import deque

# heapq.heapify(progresses)

# print(progresses)

lst = dict(zip(speeds,progresses))


# for i in range(len(progresses)):
#     progresses[i] += speeds[i]
#     print(progresses)

