# 프로그래머스 _ 소수 찾기 210627


# 내 풀이
def solution(n):
    nlist = [True] * (n+1)
    m = int(n**0.5)
    for i in range(2,m+1):
        if nlist[i] == True:
            for j in range(i+i,n+1,i):
                nlist[j] == False
    return len([i for i in range(2,n+1) if nlist[i] == True])


# 다른 풀이

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)