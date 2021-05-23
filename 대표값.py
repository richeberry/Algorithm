
n = int(input())
num = list(map(int, input().split()))
mean = round((sum(num)/len(num)))
numMin = float('inf') #infinity
for idx, x in enumerate(num):
    means = abs(x-mean)
    if means < numMin: 
        numMin = means
        score = x
        answer = idx+1
    elif means == numMin:
        if x > score:
            score = x
            answer = idx+1
print(mean, answer)


# round는 round_half_even 방식을 택한다 
# -> 정확하게 중간에 있으면 짝수쪽을 택함 / 아니라면 그대로 반올림
# ex)
a = 4.5
print(round(a))
b = 4.51
print(round(b))
