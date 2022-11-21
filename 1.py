n=int(input())
p=''
while n>0:
  b=n%3
  n=n//3
  p+=str(b)
print(p)
