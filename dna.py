n=input()

list=[]
for i in range(len(n)):
    list.append(n[i])

oddlist=[]
for i in range(len(n)):
    if int(list[i])%2!=0:
        oddlist.append(list[i])
ele=''
for element in oddlist:
    ele+=element
print(ele)
