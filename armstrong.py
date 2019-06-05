c=int(input())
i=c
d=0
while c!=0:
  b=c%10
  a=(b**3)
  c=c//10
  d=a+d
if i==d:
  print("yes")
else:
  print("no")
