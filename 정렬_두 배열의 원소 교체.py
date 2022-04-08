# 이코테 _ 정렬 두 배열의 원소 교체

n,k = map(int, input().split())

a = sorted(list(map(int, input().split()))) # 리스트를 받아 정렬
b = sorted(list(map(int, input().split())))

for i in range(k):
    a[i], b[-(i+1)] = b[-(i+1)],a[i] # A의 작은 순서대로 B의 큰 값과 K번 스와프

print(sum(a))