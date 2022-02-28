
# Programmers Lv.3 _ 정수삼각형 

def solution(triangle):
    for num in range(1, len(triangle)): # 둘째 줄부터 (첫째 줄은 숫자가 1이므로)
        for idx in range(num+1): # idx 값으로 비교
            if idx == 0: # 가장 왼쪽이면
                triangle[num][idx] += triangle[num-1][idx] # 윗줄의 인덱스 값을 더함 (윗줄에서 숫자 두개 중 max값 고를 수 없음)
            elif idx == num: # 가장 오른쪽
                triangle[num][idx] += triangle[num-1][-1] # 윗줄의 인덱스 값을 더함
            else: # 가운데 숫자들
                triangle[num][idx] += max(triangle[num-1][idx-1], triangle[num-1][idx]) # 윗줄의 두 값 중에서 더 큰 값을 더함
    print(triangle)
    return max(triangle[-1])