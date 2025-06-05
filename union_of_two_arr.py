import array as ar

arr = ar.array('i',[1,2,3,4,5])
arr2 = ar.array('i',[1,2,5,6,7])
union = ar.array('i')
for i in arr:
    if i not in union:
        union.append(i)
for j in arr2:
    if j not in union:
        union.append(j)
print(union,end=" ")