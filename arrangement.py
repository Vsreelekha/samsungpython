girls=int(input())
boys=int(input())
g=list(map(int,input().split()))
b=list(map(int,input().split()))
list1=list(zip(g,b))
list2=[]
for i in list1:
    list2.extend(list(i))
print(list2)
if sorted(list2):
    print('Yes')
else:
    print('No')
