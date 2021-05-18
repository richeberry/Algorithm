arr=[4,4,4,3,3]

def solution(arr):
    answer = []

    for i, value in enumerate(arr):
        if i == 0:
            answer.append(arr[i])
        elif arr[i] != arr[i-1]:
          answer.append(arr[i])

    return answer

print(solution(arr))


def solution(arr):
    answer = []

    for i, value in enumerate(arr):
        if i == 0 or arr[i] != arr[i-1]: #단순하게, 위에 코드 한 문장으로 넣어줌
            answer.append(arr[i])
    return answer


def no_continuous(arr):
    answer = []
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer

print(no_continuous(arr))

