# 이코테 _ 정렬 성적이 낮은 순서로 학생 출력하기.py

# 내풀이

array = []
for i in range(int(input())): # array에 한꺼번에 값 더해줌
    array.append(list(map(str, input().split())))

for i in array:
    i[1] = int(i[1]) # 점수만 숫자로 변환

def setting(data): # 점수로 변환하는 함수 만듦
    return(data[1])

result = sorted(array, key=setting) # 점수를 기준으로 정렬 

for i in result: # 이름만 출력 
    print(i[0], end=' ')


# 책 

n = int(input()) # n명의 학생 정보를 받아 리스트에 저장 
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1]))) # 이름은 문자열로, 점수는 숫자로 변환하여 저장

array = sorted(array, key=lambda student: student[1]) # 키를 이용하여 점수를 기준으로 정렬 

for student in array: # student lambda 이름과 같이 해야함
    print(student[0], end=' ') 