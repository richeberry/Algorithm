# Programmers _ Lv.2 오픈채팅방 2019 KAKAO BLIND RECRUITMENT


def solution(record, id=[], answer=[]):
    for r in record:
        id.append(r.split()[1]) 
    dic_id = {x : '' for x in id} # 바뀌는 닉네임을 계속 업데이트하며 아이디와 최종 닉네임을 딕셔너리에 저장

    for r in record:
        if len(r.split()) > 2: # Leave일 때 닉네임은 바뀌지 않으므로 제외
            dic_id.update({r.split()[1]:r.split()[2]})

    for r in record:
        if r.split()[0] == 'Enter': # Change일 때는 채팅방에 아무런 변화가 없으므로 출력하지 않음
            answer.append(f'{dic_id[r.split()[1]]}님이 들어왔습니다.')
        elif r.split()[0] == 'Leave':
            answer.append(f'{dic_id[r.split()[1]]}님이 나갔습니다.')

    return answer