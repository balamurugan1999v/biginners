a=input()
temp=0
for x in a:
  if (x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U'):
    temp=1
if temp==1:
  print("yes")
else:
  print("no")
