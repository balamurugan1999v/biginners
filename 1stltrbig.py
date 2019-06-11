num=input().split()
s1=[]
for i in num:
  if i[0]>='a' and i[0]<='z':
    f=ord(i[0])
    f=f-32
    y=chr(f)
    s1.append(y+i[1:])
  else:
    s1.append(i)
for i in s1:
  print(i,end=" ")
