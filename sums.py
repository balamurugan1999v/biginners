a=int(input())
num=input().split()
s1=[]
c=0
for i in num:
  s1.append(int(i))
for i in range(a):
  c=s1[i]+c
print(c)
