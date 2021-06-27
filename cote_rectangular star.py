# 직사각형 별찍기

#가로 길이가 n, 세로 길이가 m인 직사각형 형태 출력

a,b = map(int, input().strip().split(' '))
for _ in range(b):
    print('*'*a)