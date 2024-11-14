def add(a,b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        return add(a+1,b-1)
print(add(2,5))


    
