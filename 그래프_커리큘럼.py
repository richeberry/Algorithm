# 이코테 _ Section 3 _ 커리큘럼 (위상 정렬)

# 커리큘럼

from collections import deque
import copy

v = int(input())
indegree = [0] * (v + 1)
graph = [[] for _ in range(v + 1)]
lec = [0] * (v + 1)

# 방향 그래프의 간선 정보 입력받기
for i in range(1, v + 1):
    data = list(map(int, input().split()))
    lec[i] = data[0] # 첫번째 원소는 강의 시간을 담고 있음
    for x in data[1:-1]: # 1번째 원소부터 -1 전의 원소까지는 필요한 강의 번호
        indegree[i] += 1 # 하나씩 방문해야하므로 차수에 1 더하기
        graph[x].append(i) # 

# indegree [0, 0, 1, 1, 2, 1]
# graph [[], [2, 3, 4], [], [4, 5], [], []]
# lec [0, 10, 10, 4, 4, 3]
# result [0, 10, 10, 4, 4, 3]

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(lec)
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + lec[i])
            indegree[i] -= 1