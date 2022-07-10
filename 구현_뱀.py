# 이코테 _ 구현 _ 뱀

n = 6

game = [[0] * n for _ in range(n)]
# print(game)

# k = int(input())
k = 3

# 사과 표시 _ game에 사과 위치를 1로 표시
# for _ in range(k):
#     a, b = map(int, input().split())
#     game[a-1][b-1] = 'apple'


# 사과가 있는 게임
game = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 'apple', 0], [0, 0, 0, 'apple', 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 'apple', 0, 0, 0], [0, 0, 0, 0, 0, 0]]
game[0][0] = 1
tail = 0
cnt = 0
noww = 0 # 현재 행 위치
nowh = 0 # 현재 열 위치
head = game[noww][nowh] # 뱀이 처음 있을 위치
print(head)
print(game)
# l = int(input())
l = 3
# direct = [] # 회전 방향을 담을 리스트
# for _ in range(l):
#     a, b = map(str, input().split())
#     direct.append((int(a), b))

direct = [(3, 'D'), (15, 'L'), (17, 'D')]

# 게임이 몇 초에 끝나는지 출력


while head != tail:
    for i in range(len(direct)):
        print("i", i)
        if direct[i][1] == 'D':
            for j in range(direct[i][0]):
                game[noww][nowh] = 1

                noww += 1
                cnt += 1
                head = (noww, nowh)
            print(game)
            print("noww", noww)
            print("head", head)
        elif direct[i][1] == 'L':
            for j in range(direct[i][0]):
                print("j", j)
                game[noww][nowh] = 1
                nowh += 1
                cnt += 1
                head = (noww, nowh)
                print("noww", noww)
                print("head", head)
            print(game)
