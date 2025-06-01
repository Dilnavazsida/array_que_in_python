import array as ar



def fun(arr1,arr2,n,m):
    arr1[m:]=arr2
    a1 = arr1.tolist()
    a1.sort()
    a2 = ar.array('i',a1)
    print(a2)

arr1 = ar.array('i',[10,20,30,0,0,0])
arr2 = ar.array('i',[40,50,60])

n= len(arr2)
m= len(arr1)-n
fun(arr1,arr2,m,n)