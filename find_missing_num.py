import array as ar

arr = ar.array('i',[10,20,30,40,50,60,70,90])
n=9

def missingNum(arr,n):
    first =arr[0]
    last = first + (n-1) * 10
    excepted_sum = n * (first+last) // 2
    sm = sum(arr)
    return excepted_sum - sm
print("missing num : ",missingNum(arr,n))

