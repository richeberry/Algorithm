# Inflearn _ Section 3 카드 역배치(정올 기준)

# 내 풀이

card_lst = [i for i in range(1,20+1)]

for i in range(10):
    area = list(map(int, input().split()))
    area_lst = [] # 역배치 할 리스트
    tmp_lst = [] # 뒤에 붙는 리스트
    area_lst = card_lst[area[0]-1:area[1]] # 역배치할 리스트 담음
    tmp_lst = card_lst[area[1]:]
    card_lst = card_lst[:area[0]-1]
    for _ in range(len(area_lst)):
        card_lst.append(area_lst.pop()) # pop하면서 카드 리스트에 더하기
    for k in tmp_lst:
        card_lst.append(k) # 뒤에 남은 리스트 붙이기

for i in card_lst:
    print(i, end = ' ')

# 인프런 풀이

a = [i for i in range(1,20+1)]
for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], a[e-i] = a[e-i], a[s+i] # 제일 처음 수와 끝 수의 자리를 바꿔줌
