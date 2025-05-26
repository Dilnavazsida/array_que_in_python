import array as ar
arr = ar.array('i')
# user pase thi puchve che ke ketla element tamare array ni andar nakh va che 
user = int(input("how many element you want to enter : "))
for i in range(user):
    user = int(input("Enter element "))
    # append function ni madad thi array ni andar value add karaviye chiye 
    arr.append(user)
print("orignal array ",arr)

#  ek function banayvu che je array ne reverse karse 
def fun(arr):
    return arr[::-1]

# aya function call kyru che 
rev = fun(arr)

# aya reverse array ne print karayvu che without any round or square brekets
for i in range(len(arr)):
    print(rev[i],end=" ")
print()
mn = min(arr)
print("minimum is ",mn)

mx = max(arr)
print("maximum is ",mx)