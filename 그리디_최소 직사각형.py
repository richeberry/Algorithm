# Programmers _ Lv 1 _ 최소 직사각형


def solution(sizes):
    # 명함 크기 저장할 변수
    wallet = sizes[0]
    for i in sizes:
        # 가로 길이보다 세로 길이가 길면
        if i[0] < i[1]:
            # 명함 회전
            i[0], i[1] = i[1], i[0]
        # 지갑의 크기와 명함의 크기 비교 후 큰 값을 지갑의 크기로 선택
        wallet[0] = max(wallet[0], i[0])
        wallet[1] = max(wallet[1], i[1])
        # 면적 크기
        answer = wallet[0] * wallet[1]
    return answer