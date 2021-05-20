# k번째 수

# 내 풀이
import random

T = int(input())
n,s,e,k = map(int, input().split())
for t in range(1, T+1):
    n_list = [random.randint(5,500) for i in range(n)]
    n_slice = sorted(n_list[s-1:e])
    kth = n_slice[k]
    print('#%d %d' %(t, kth)) 

# Inflearn 풀이

T = int(input())
for t in range(T):
    n,s,e,k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    print('#%d %d' %(t+1, a[k-1]))