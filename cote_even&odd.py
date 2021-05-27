# 짝수와 홀수
'''
n = 3
if n%2==0: 
    print("Even")
else:
    print("Odd")


def solution(num):
    return "Even" if num%2==0 else "Odd"

print(solution(12381))
'''

# 다른 풀이
'''
def evenOrOdd(num):
    return ["Even", "Odd"][num & 1]
'''

print([3 & 1])
print([4 & 1])

print(bin(3&1))
print(bin(4&1))
print(bin(5&1))
print(bin(6&1))