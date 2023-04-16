class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class List_2:
    def __init__(self):
        self.start_node = None

    def print_l(self):
        if self.start_node is None:
            print("список пустой")
            return
        n = self.start_node
        while n is not None:
            print(n.data, end=" ")
            n = n.next
        print()

    def insert_start(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node

    def del_start (self):
        if self.start_node is None:
            print("список пустой")
            return
        self.start_node = self.start_node.next

    def del_end (self):
        if self.start_node is None:
            print("список пустой")
            return
        n = self.start_node
        while n.next.next:
            n = n.next
        n.next = None

    def search(self, x):
        n = self.start_node
        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False

            



l1 = List_2(4)
l1.insert_start(3)
l1.insert_start(2)
l1.insert_start(1)
l1.insert_end(5)
l1.print_l()

#l1.del_start()
#l1.print_l()

#l1.del_end()
#l1.print_l()

print(l1.search(4))    

