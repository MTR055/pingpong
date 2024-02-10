a=int(input())
b=int(input())
def sum(a,b):
    sum=[]
    lastsum=0
    if a<0 and b<0:
        a=-a
        b=-b
    if a<0 and b>0:
        a=-a
    if a>0 and b<0:
        b=-b

    for i in range(a,b+1):
        count = 0
        for j in range(2,i):
            if i%j==0:
                count+=1
        if count==0:
            sum.append(i)

    for ele in sum:
        lastsum+=ele

    return lastsum


print(sum(a,b))