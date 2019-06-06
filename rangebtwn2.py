a=int(input())
b1,c1=input().split()
b=int(b1)
c=int(c1)
t=0
for x in range (b+1,c):
  if x==a:
    t=1
    break
if t==1:
  print('yes')
else:
  print('no')
