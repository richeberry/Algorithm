# 이코테 _ 정렬 위에서 아래로

nums = [int(input()) for i in range(int(input()))]
for i in sorted(nums, reverse=True):
    print(i)