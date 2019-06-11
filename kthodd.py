a1,b1=input().split()
a=int(a1)
b=int(b1)
co=0
num=input().split()
s1=[]
for i in num:
  s1.append(int(i))
for i in range(a):
  if co==b:
    break
  if (s1[i]%2)!=0:
    co+=1
    c=s1[i]
print (c)
