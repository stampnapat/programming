times = int(input())
arr = input()
l_ardrain = ["A", "B", "C"]
l_bruno = ["B", "A", "B", "C"]
l_goran = ["C", "C", "A", "A", "B", "B"]

ardrain_score = 0
bruno_score = 0
goran_score = 0

for i in range(times):  
    if arr[i] == l_ardrain[i % len(l_ardrain)]:
        ardrain_score += 1
    if arr[i] == l_bruno[i % len(l_bruno)]:
        bruno_score += 1
    if arr[i] == l_goran[i % len(l_goran)]:
        goran_score += 1

d = {
    "Adrian": ardrain_score,
    "Bruno": bruno_score,
    "Goran": goran_score
}

maxs = max(d.values())
winners = [name for name, score in d.items() if score == maxs]

print(maxs)
for name in sorted(winners):
    print(name)

