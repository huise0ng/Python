a,d,n=input().split()

a=int(a)
d=int(d)
n=int(n)

s=a
for i in range(2, n+1):
   s+=d

print(s)