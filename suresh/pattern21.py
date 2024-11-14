n=int(input("enter the number"))
c=n
i=1
j=1
while(n):
    if i==0 or j==0 or i==n-1 or j==n-1:
        print(c,end=" ")
    else:
        print(n-1,end=" ")
        print()
