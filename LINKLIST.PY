# Step 1: Create a Node class to hold data and the reference to the next node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Step 2: Create a LinkedList class to manage the nodes
class LinkedList:
    def __init__(self):
        self.head = None

    # Method to add a new node to the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Method to print the linked list elements
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> None")

# --- Testing the Linked List ---
if __name__ == "__main__":
    # Initialize an empty linked list
    my_list = LinkedList()

    print("Adding elements to the Linked List...")
    my_list.append(10)
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    # Display the final linked list
    print("Linked List Output:")
    my_list.display()