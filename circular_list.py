class node:
    def __init__(self, data, next = None):
        self.data = data 
        self.next = next 

def show (head):
    temp = head
    while temp is not  None:
        print(temp.data, end=" >>  ")
        temp = temp.next
        if temp == head :
            break

head = node (10)
second = node(20)
third = node(30)
fourth = node(40)

head.next= second
second.next = third
third.next = fourth
fourth.next = head
#
#show(head)
# typ add element at head
# new = node(66)
# new.next = head
# temp = head
# while temp.next != head:
#     temp = temp.next
# temp.next = new
# head = new

# show(head)
# to add element at center 
pos = 3
new = node(303)
temp = head
for i in  range(pos-2):
    temp = temp.next
new.next = temp.next
temp.next = new
show(head)

