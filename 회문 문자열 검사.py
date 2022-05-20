# Inflearn _ Section 3 회문 문자열 검사

for i in range(int(input())):
    txt = ','.join(input().lower()).split(',') # 대소문자 구분하지 않으므로 소문자로만 비교 
    txt_reverse = [] # 뒤집은 단어 저장할 변수
    for j in range(len(txt)):
        txt_reverse.append(txt[-(j+1)]) # 뒤부터 알파벳 하나씩 저장
    if txt == txt_reverse: # 두 리스트가 같으면
        print('YES') 
    else: # 다르면 
        print('NO')