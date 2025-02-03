array = list(input())
row1, row2, row3, row4, row5 = "", "", "", "", ""
count = 1
for i in range(1,len(array)+1) :
    print(i)
    if i == 1 :
        if 1 - len(array) == 0 :
            row1 += "..#.."
            row2 += ".#.#."
            row3 += f"#.{array[i-1]}.#"
            row4 += ".#.#."
            row5 += "..#.."
        else :
            row1 += "..#"
            row2 += ".#.#"
            row3 += f"#.{array[i-1]}.#"
            row4 += ".#.#."
            row5 += "..#"

    elif i % 3 == 0  :
        if count - len(array) == 0 :
            row1 += "...*.."
            row2 += ".*.*."
            row3 += f"*.{array[i-1]}.*"
            row4 += ".*.*."
            row5 += "..*.."
        else :
            row1 += "...*"
            row2 += ".*.*"
            row3 += f"*.{array[i]}.*"
            row4 += ".*.*."
            row5 += "..*.."

    else :
        if count - len(array) == 0 :
            row1 += "...#.."
            row2 += ".#.#."
            row3 += f"#.{array[i]}.#"
            row4 += ".#.#."
            row5 += "..#.."     
        else :
            row1 += "...#"
            row2 += ".#.#"
            row3 += f"#.{array[i]}.#"
            row4 += ".#.#."
            row5 += "..#.."
    
    count +=1 

#เหลือ row 3, 4
# row1 += ".."
# row2 += "."
# row5 += ".."
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
