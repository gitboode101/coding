from package.ListNode import NodeList
class LinkedList :
    def __init__(self) :
        self.head = None
    def add_items(self,value) :
        new_node = NodeList(value)
        if self.head is None :
            self.head = new_node 
            return 
        curr = self.head
        while curr.next is not None :
            curr = curr.next
        curr.next = new_node 
    def list_loop_print(self) :
        curr = self.head 
        while curr is not None :
            print(curr.value ,end="-..-> ")
            curr = curr.next
        print("None")              
