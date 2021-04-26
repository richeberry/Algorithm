def solution(board, moves):
    basketlist = []
    answer = 0

    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                basketlist.append(board[j][i-1])
                board[j][i-1] = 0

                if len(basketlist) > 1:
                    if basketlist[-1] == basketlist[-2]:
                        basketlist[-1].pop
                        basketlist[-1].pop
                        answer += 2
                break
    return answer