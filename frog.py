x = input().split()
x1 = int(x[0])
distance  = int(x[1])
count = 0

if x1 < distance :
	while distance > 0 :
		distance -= x1
		count += 1
	print(count)
elif x1 == distance :
	print(1)
else :
	print(2) 
