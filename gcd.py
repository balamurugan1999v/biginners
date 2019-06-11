a,b=input().split()
i=int(a)
j=int(b)
if i>j:
  x=i
  i=j
  j=x
c=i
while(c!=0):
  if (i%c)==0 and (j%c)==0:
    t=c
    break
  c-=1
print(t)
