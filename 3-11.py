# x = int(input())
# if x < 0 :
#     print(-(x%3), -(x%11))
# else :
#     print(x%3, x%11)



def  mod(n,m):	    
    result = 0	
    for i in range(len(n)):
        print(i)
        result = (result * 10 + int(n[i])) % m	    
        print(f"result{result}")
    return result	
n = input()	
print(mod(n,3),mod(n,11))
