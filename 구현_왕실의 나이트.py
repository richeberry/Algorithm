# 이것이 코딩테스트다 _ 구현 왕실의 나이트

knight = list(''.join(input())) # 리스트로 받아오기

knight[0] = ord(knight[0])-96 #행의 알파벳을 숫자로 변경
knight[1] = int(knight[1]) # 문자열로 받은 열을 숫자로 변경
moves = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)] # 나이트가 움직일 수 있는 경우의 수

cnt = 0 # 움직일 수 있는 자리의 개수
for move in moves:
    now = [x+y for x,y in zip(knight,move)] # 나이트가 움직일 수 있는 경우의 수를 현재 위치와 더함(이동)
    if min(now) > 0 and max(now) < 9: # 더한 자리의 최솟값이 1 이상이고, 최댓값이 8 이하면 체스판 안에 있으므로
        cnt += 1 # 움직일 수 있는 자리이다.

print(cnt)