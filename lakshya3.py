a,b,c=map(int,input().split())

a-=1

e=(b-c)
if e<0:
    e*=-1
    e+=c-1
else:
    e+=c-1

if a>e:
    print("2")
elif e>a or (a==0 and e==0):
    print("1")
else:
    print("3")
