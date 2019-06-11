a1,b1=input().split()
a=int(a1)
b=int(b1)
r=0
s1=[]
num=input().split()
for i in num:
  s1.append(i)
s1.sort()
print(s1[b-1])
