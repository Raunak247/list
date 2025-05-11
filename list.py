list1 = [12,-7,5,64,-14]
list2 = [12,14,-95,3]

print("Positive elements in list1:")
for i in list1:
    if i<=0:
        
        continue
    else:
        print(i,end=" ")


print("\nPositive elements in list2:")
for i in list2:
    if i<0:
        continue
    else:
        print(i,end=" ")