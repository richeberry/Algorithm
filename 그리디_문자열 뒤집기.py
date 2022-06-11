# 문자열 뒤집기

s = '0001100'

def stringback(s, x, y):
    s = list(s)
    diff = []
    cnt = 0

    for idx, i in enumerate(s):
        if len(diff) == 0: # diff에 아무것도 들어있지 않을 때 
            if i == x:
                diff.append(idx)
        else: # diff에 이미 원소가 들어있을 때
            if idx - diff[-1] == 1 and i == x: # 연속된 인덱스이면서 i가 x이면
                diff.append(idx)


    print('diff',diff)
    while len(set(s)) > 1:
        print('lens',len(set(s)))
        if len(set(s)) == 1:
            break
        cnt += 1
        print(cnt)
        for i in diff:
            s[i] = y
        print(s)
    return cnt

print(stringback(s, '0', '1'))

# 연속된 문자열이 아닐 경우 연속 된 것만 바꾸는 것 

for i in s:
    s.find('1', i, s[-1])