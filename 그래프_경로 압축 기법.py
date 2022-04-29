# 이코테 _ 서로소 집합 _ 경로 압축 기법 소스코드

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
