n=input("Enter any string:")
l=n.split()
print(l)
c=len(l)
print(c)
s=" "

for i in range(c-1):
    s=s+l[i][0]+"."
s=s+l[-1][0]
print(s)