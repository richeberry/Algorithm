# Inflearn _ Section 3 숫자만 추출

word = input()
num = '' # 추출할 숫자 변수 초기화
for i in word: 
    if ord(i) < 65: # 아스키 코드 알파벳의 숫자보다 작으면 정수이므로
        num += i

num = int(num)
divisor = 0 # 약수 저장할 변수 초기화

for i in range(1, num+1):
    if num % i == 0: # 나누어 떨어지면 약수이므로
        divisor += 1 # 약수 개수 + 1

print(num)
print(divisor)
