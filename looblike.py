nums = int(input())
arr = input().split()
l = []
max_ = 0
for num in nums:
    round_count = 0
    for u in nums-1-num:
        if arr[num] == arr[u]:
            round_count += 1
    max_ = max(round_count,max)
    if round_count == max_:
        l.append

