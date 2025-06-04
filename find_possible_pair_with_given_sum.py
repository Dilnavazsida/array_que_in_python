import array as ar
def fun(arr,total_sum):
    pair = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == total_sum:
                pair.append((arr[i],arr[j]))
    return pair


arr = ar.array('i',[2,5,6,7,4,3,5,8,3])
total_sum = 11

result = fun(arr,total_sum)
print("possible pair is ",result)