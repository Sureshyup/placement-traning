def perfect_number():
    n=int(input("enter the number"))
    sum=0
    temp=n
    for i in range(1,n+1):
        if n%i==0:
            sum=sum+i
    print(sum)
    if sum==temp:
        print("it is a perfect number",temp)
    else:
        print("is not a perfect number",temp)
perfect_number()
