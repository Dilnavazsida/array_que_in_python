user = int(input("enter the number to check it's prime or not"))

if user <=1:
    print("not prime")
else:

    for i in range(2,user):
        if user % i == 0:
            print("number not prime")
            break
    else:
        print("number is prime")