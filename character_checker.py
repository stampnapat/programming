# import string
# print(string.ascii_uppercase)
alpha = "abcdefghijklmnopqrstuvwxyz"
lower_case = list(alpha)
alphas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
upper_case = list(alphas)
count_upper = 0
count_lower = 0
arr = [ x for x in input() if x != " " and x != ""]

for char in arr :
    if char in upper_case :
        count_upper += 1
    else : 
        count_lower += 1

if count_lower > 0 and count_upper == 0:
    print("All Small Letter")
elif count_upper > 0 and count_lower == 0:
    print("All Capital Letter")
else : 
    print("Mix")
