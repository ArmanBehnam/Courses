lst=[]
i=0
while i<3:
    print ('Enter a number:')
    x=input()
    lst.append(x)
    i=i+1
lst.sort()
print(lst[0]+','+lst[1]+','+lst[2])