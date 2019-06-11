a=input()
j=int(a)
num=input().split()
s1=[]
s2=[]
for i in num:
  s1.append(int(i))
  s2.append(int(i))
s2.sort()
for i in range(j):
  if s1[i]!=s2[i]:
    c=i
    break
print(c)
