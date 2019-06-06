a=input()
b=len(a)
c=b//2
if (b%2)!=0:
  print(a[0:c],end=""),print('*',end=""),print(a[c+1:b+1],end="")
else:
  print(a[0:c-1],end=""),print('**',end=""),print(a[c+1:b+1],end="")
