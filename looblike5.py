n = int(input())
arr = input().split()
d = {}
l = []
m = []
maxs = 0
new_list = []
for i in arr:
    if i not in l:
        d[i] = 1
        l.append(i)
    else :
        d[i] += 1
         
for a,b in d.items():
    a = int(a)
    if b > maxs:
        new_list = [a]
        maxs = max(maxs,b)
    elif b == maxs:
        new_list.append(a)
new_list = sorted(new_list)
new_list = list(map(str,new_list))
     
print(" ".join(new_list))
"""n = int(input())
arr = input().split()

# Convert elements to integers if necessary
arr = list(map(int, arr))

# Dictionary to count frequencies
d = {}
for num in arr:
    if num in d:
        d[num] += 1
    else:
        d[num] = 1

# Find the maximum frequency
max_freq = max(d.values())

# Find all elements with the maximum frequency
most_frequent_elements = [key for key, value in d.items() if value == max_freq]

# Sort the elements
most_frequent_elements_sorted = sorted(most_frequent_elements)

# Print the result
print(" ".join(map(str, most_frequent_elements_sorted)))"""

