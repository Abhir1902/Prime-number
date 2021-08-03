n=int(input("Enter the number : "))
def prime(t):
    flag=0
    for i in range(2,t):
        if not t%i:
            flag=1
            break
    if (flag):
        print("The given number is not a prime number")
    else:
        print("The given number is a prime number")
prime(n)
