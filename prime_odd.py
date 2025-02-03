time = int(input())
l = []
for x in range(time) :
	num = int(input())
	if num % 2 == 0 and num != 2:
		l.append("F")
	else :
		l.append("T")

for num in l :
	print(num)

