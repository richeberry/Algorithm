# 무지의 먹방 라이브

food_times = [3, 1, 2]
k = 5

answer = 0
quo = k // len(food_times)
divided = k % len(food_times)
print('quo, divided', quo, divided)


for i in range(len(food_times)):
    food_times[i] -= quo

for i in food_times:
    if i == 0:
        food_times.pop(food_times[i-1])

print(food_times)

for i in range(divided):
    print(i)