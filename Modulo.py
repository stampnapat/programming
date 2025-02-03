s = set()
for n in range(10):
    char = int(input())
    num = char%42
    s.add(num)
print(len(s))







# l.sort()
# for i in range(10):
#     l.remove(l[i])
#     if l[0] not in l :
#         count += 1
#     # for u in range(0,10-1-i):
#     #     if l[u] != l[u+1]:
#     #         count += 1 
# print(count)

# รับค่าจำนวนเต็ม 10 ค่า	
# nums = [int(input()) for _ in range(10)]	
# # คำนวณค่า modulo 42 และเก็บเศษที่ไม่ซ้ำกันในเซต	
# remainders = {num % 42 for num in nums}	
# # แสดงจำนวนเศษที่ไม่ซ้ำกัน	
# print(remainders)
# print(len(remainders))
