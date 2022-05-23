# Inflearn _ Section 3 카드 역배치(정올 기준)

# 내 풀이

card_lst = [i for i in range(1,20+1)]

for i in range(10):
    area = list(map(int, input().split()))
    area_lst = []
    tmp_lst = []
    area_lst = card_lst[area[0]-1:area[1]]
    tmp_lst = card_lst[area[1]:]
    card_lst = card_lst[:area[0]-1]
    for _ in range(len(area_lst)):
        card_lst.append(area_lst.pop())
    for k in tmp_lst:
        card_lst.append(k)

for i in card_lst:
    print(i, end = ' ')