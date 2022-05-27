# 이코테 _ 이진탐색 떡볶이 떡 만들기

n,m = list(map(int, input().split()))
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 수행(반복)
result = 0
while start <= end: # 자를 떡이 더 길다면
    total = 0
    mid = (start + end) // 2 
    for x in array:
        if x > mid: # 중간 값보다 길면 늘이기
            total += x - mid
    
    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)