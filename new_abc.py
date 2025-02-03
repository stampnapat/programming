arr = sorted(list(map(int, input().split())))
abc = input().lower()
for i in abc :
    if i == "a":
        print(arr[0], end=" ")
    elif i == "b":
        print(arr[1], end=" ")
    else:   
        print(arr[2], end=" ")
    



