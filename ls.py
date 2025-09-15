l=list()
n=int(input("Enter no.of inputs to be inserted"))
print("enter",n,"values")
for i in range(n):
    l.append(int(input()))
s=int(input("Enter element to be searched"))
#for i in range(len(l)-1):
#    if l[i]==s:
#        print(s,"is fond at location",i+1)
#        break
#else:
#    print(s,"is not found in list")
if s in l:
    print(s,"is fond at location",l.index(s))
else:
    print(s,"is not found in list")
