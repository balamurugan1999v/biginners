c=int(input())
d=c
a=0
while c!=0:
  b=c%10
  c=c//10
  a=(a*10)+b
if a==d:
  print("yes")
else:
  print("no")
