# 이코테 _ 그래프 _ 신장트리 _ 크루스칼 알고리즘

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루드 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = a
    else:
        parent[a] = b

edges = []
result = 0
