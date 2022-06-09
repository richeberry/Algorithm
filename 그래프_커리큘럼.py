# 이코테 _ Section 3 _ 커리큘럼 (위상 정렬)

# 커리큘럼

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프 초기화)
graph = [[] for _ in range(v + 1)]
# 강의 시간을 담는 리스트 초기화
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
    result = copy.deepcopy(lec) # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1): 
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + lec[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 위상 정렬을 수행한 결과
    for i in range(1, v + 1):
        print(result[i])

topology_sort()