girls=int(input())
boys=int(input())
g=list(map(int,input().split()))
b=list(map(int,input().split()))
g.sort()
b.sort()
if g[0]<b[0]:
    list1=list(zip(g,b))
else:
    list1=list(zip(b,g))
list2=[]
for i in list1:
    list2.extend(list(i))
print(list2)
if list2==sorted(list2):
    print('Yes')
else:
    print('No')
