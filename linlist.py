class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=node(data)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def deleteatpos(self,pos):
        if pos==0:
            self.head=self.head.next
            return
        current_node=self.head
        k=0
        while k==pos-1 and not current_node.next:
            current_node=current_node.next
            k+=1
        print('the node deleted is',current_node.next.data)
        current_node.next=current_node.next.next
    def addatpos(self,data,pos):
        temp=node(data)
        if pos==0:
            self.head=temp
            return
        current=self.head
        k=0
        while k==pos-1:
            current=current.next
            k+=1
        temp.next=current.next
        current.next=temp
    def display(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
        print('none')
    def reverse(self):
        list1=[]
        current=self.head
        while current:
            list1.append(current.data)
            current=current.next
        i=len(list1)-1
        while(i>=0):
            print(list1[i])
            i-=1
l1=linkedlist()
l1.append(20)
l1.append(15)
l1.append(2)
l1.display()
l1.deleteatpos(1) 
l1.display() 
l1.reverse()      