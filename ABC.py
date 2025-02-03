num = list(input().strip())
char = list(input().strip())
num = [x for x in num if x != " " ]
char = [x for x in char if x != " "]
opp = ''


if char[0] > char[1] and char[1] > char[2] :
    opp = "more"

elif char[0] < char[1] and char[1] < char[2] :
    opp = "less"

else :
    opp = "mid"

x = len(char)
if opp == "more":
    for i in range(x):
        for u in range(0,x-i-1):
            if num[u] < num[u+1]:
                num[u], num[u+1] = num[u+1], num[u]

elif opp == "less" :
    for i in range(x):
        for u in range(0,x-i-1):
            if num[u] > num[u+1]:
                num[u], num[u+1] = num[u+1], num[u]

else :
    num[0], num[1], num[2] = num[0], num[1], num[2] 

print(" ".join(num))


# for i in range(num): 
#     for u in range(0,num-i);
#         for 
# print(num)
# print(len(num))
# print(char)
# print(len(char))