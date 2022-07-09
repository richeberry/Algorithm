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
head = game[0][0] # 뱀이 처음 있을 위치

print(game)
# l = int(input())
l = 3
# direct = [] # 회전 방향을 담을 리스트
# for _ in range(l):
#     a, b = map(str, input().split())
#     direct.append((int(a), b))

direct = [(3, 'D'), (15, 'L'), (17, 'D')]

# 게임이 몇 초에 끝나는지 출력

tail = 0
cnt = 0
now = 0
while head != tail:
    for i in range(direct[now][0]):
        if direct[now][1] == 'D':
