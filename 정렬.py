# 선택 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 값 스와이프

print(array)


# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법(뒤부터 앞으로 가며 적절한 위치 찾기)
        if array[j] < array[j - 1]: # 한 칸씩 왼쪽으로 이동
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break

print(array)


# 퀵 정렬 

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    if len(array) <= 1: # 리스트가 하나의 원소만 가지고 있다면 종료
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 피벗보다 작은 분할된 왼쪽 부분
    right_side = [x for x in tail if x >= pivot] # 피벗보다 큰 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))


# 계수 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2] # 모든 원소의 값이 0보다 크거나 같다고 가정

count = [0] * (max(array)+1) # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만ㄴ큼 인덱스 출력


# sorted()
# key를 활용한 소스코드

array =[('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return(data[1])

result = sorted(array, key=setting)
print(result)