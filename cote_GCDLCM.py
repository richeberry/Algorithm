# 최대공약수 최소공배수 - 유클리드 호제법

def gcd(n,m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n, m)
    else:
        return n

def solution(n,m):
    return [gcd(n,m),int(m*n/gcd(n,m))]


print(gcd(72,30))
print(solution(72,30))

