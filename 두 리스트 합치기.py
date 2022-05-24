# Inflearn _ Section 3 두 리스트 합치기

import sys
sys.stdin = open('in1.txt', 'rt')
lst = []
for i in range(2):
    size = int(input())
    for j in map(int, input().split()):
        lst.append(j)

print(sorted(lst))