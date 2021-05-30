# 하샤드 수

def solution(x):
	x = str(x)
	num = 0
	for i in range(len(x)):
		num += int(x[i])
	if int(x) % num == 0:
		return True
	else: return False

print(solution(6804))


'''
def solution(x):
	x = str(x)
	num = 0
	for i in range(len(x)):
		num += int(x[i])
	if int(x) % int(num) == 0:
		answer = 'true'
	else: answer = 'false'
	return answer
	'''

#다른 풀이

def Harshad(n):
    # n은 하샤드 수 인가요?
    return n % sum([int(c) for c in str(n)]) == 0


