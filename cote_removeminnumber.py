# 제일 작은 수 제거하기_210531


arr = [4,3,2,1]
'''
answer = -1
for i in arr:
    if i == min(arr):
        answer = arr.remove(i)
        if not arr:
            answer 
print(answer)
'''

def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))
        return arr
    else:
        return [-1]


