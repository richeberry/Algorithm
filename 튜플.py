# Programmers _ 2019 카카오 인턴십 _ 튜플


s = "{{20,111},{111}}"

data = [[] for _ in range(len(s)//2)]
answer = []
cnt = 0
for i in range(len(s)):

    if s[i] == '{': 
        continue
    elif s[i].isdecimal():
        data[cnt].append(s[i])
    elif s[i] == '}':
        cnt += 1


data.sort(key=len)

for i in range(len(data)): # 빈 리스트 제거
    if len(data[i]) > 0:
        data = data[i:]
        break

print(answer)
for i in data:
    print(i)
    for j in i:
        print(j)
        if int(j) not in answer:
            answer.append(int(j))

print(answer)