a=input()
i=int(a)
c=0
while(i!=0):
  b=i%10
  c=c*10+b
  i=i//10
print(c)
