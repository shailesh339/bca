class node:
    def __init__(self, data, next = None):
        self.data = data 
        self.next = next 

def show (head):
    #temp = head
    while temp  == head:
        print(temp.data, end=" >>  ")
        temp = temp.next
        #if temp == head :
            #break

head = node (10)
second = node(20)
third = node(30)
fourth = node(40)

head.next= second
second.next = third
third.next = fourth
fourth.next = head

show(head)

