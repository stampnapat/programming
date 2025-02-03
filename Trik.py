position = list(input())
position = [n for n in position if n != "" and n != " "]
# print(position)
change_position = [1]
for i in position :
    if i == "A": # 1 --> 2 or 2 --> 1
        if change_position[0] == 1:
            change_position[0] = 2
        elif change_position[0] == 2:
            change_position[0] = 1
    
    elif i == "B": # 2 --> 3 or 3 --> 2
        if change_position[0] == 2:
            change_position[0] = 3
        elif change_position[0] == 3:
            change_position[0] = 2

    elif i == "C" : #3 --> 1 or 1 --> 3
        if change_position[0] == 3:
            change_position[0] = 1
        elif change_position[0] == 1:
            change_position[0] = 3
change_position = change_position[0]
print(change_position)