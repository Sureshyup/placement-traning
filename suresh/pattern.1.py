n=int(input("enter the number"))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i%2==0):
            print(num+1,end=" ")
            num-=1
        else:
            print(num+1,end=" ")
            num=num+n-j
    print()    
