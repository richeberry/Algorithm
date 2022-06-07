# 이코테 _ 그래프 _ 팀 결성 (서로소 알고리즘)

# 0 = 팀 합치기 연산 (두 팀을 합치는 연산)
# 1 = 같은 팀 여부 확인 연산 (두 학생이 같은 팀에 속하는지 확인)

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(0, n + 1):
    parent[i] = i

# 각 연산을 하나씩 확인
for i in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0: # 팀 합치기 연산일 경우
        union_parent(parent, a, b)
    else: # 찾기 연산일 경우
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")