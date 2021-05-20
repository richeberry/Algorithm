# k번째 큰 수

import random
from itertools import combinations

def solution(n,k):
    n, k = map(int,input().split())
    n_list = [random.randint(1, 100) for _ in range(n)]
    answer = set() # 중복 제거
    for i in list(combinations(n_list,3)):
        answer.append(sum(i))
        answer.sort(reverse=True)
    return answer[k-1]




# 다른 풀이

n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1, n): # 중복 방지
            res.add(a[i]+a[j]+a[m])
res = list(res)
res.sort(reverse=True)
print(res[k-1])