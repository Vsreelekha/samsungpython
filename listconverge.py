class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self,num):
        self.head = None
        
    def ins_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        current = self.head
        if not current:
            return
        print("Linked List elements:", end=' ')
        while current:
            print(current.data, '->', end=' ')
            current = current.next
        print()


def create_list(num):
    print("Linked List : ", num)
    linked_list = LinkedList(num)
    
    while True:
        data = input("Enter value for node: ")
        linked_list.ins_at_end(data)
        choice = input("Enter\n1) Add more nodes\n2) to exit\n")
        if choice == '2':
            break
    return linked_list


def check_intersection(list1, list2):
    nodes_set = set()
    temp = list1.head
    while temp:
        nodes_set.add(temp)
        temp = temp.next
    temp = list2.head
    index = 0
    while temp:
        if temp in nodes_set:
            return index
        temp = temp.next
        index += 1
    return -1


list1 = create_list(1)
list2 = create_list(2)
position = check_intersection(list1, list2)

if position == -1:
    print("The linked lists do not intersect")
else:
    print("The linked lists intersect at node position", position)