# 약수의 합

n = int(input())
divisor = []
for i in range(1, n+1):
    if n%i == 0:
        divisor.append(i)

print(divisor)
print(sum(divisor))

# 짧은 함수 만들기 
def solution(n):
   return sum([i for i in range(1,n+1) if n%i==0])

print(solution(12))