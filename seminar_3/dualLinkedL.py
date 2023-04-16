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
        if self.start_node is None:
            self.start_node = new_node
            return
        
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n

    def del_start(self):
        if self.start_node is None:
            print("список пустой")
            return
        self.start_node = self.start_node.next
        self.start_node.prev = None

    def del_end(self):
        if self.start_node is None:
            print("список пустой")
            return
        n = self.start_node
        while n.next.next:
            n = n.next
        n.next = None
        #n.prev = None не необходимости так как и так удалена прямая ссылка

    def search(self, x):
        n = self.start_node
        while n is not None:
            if n.data == x:
                return True
            n = n.next
        return False

            



l2 = List_2()
l2.insert_start(3)
l2.insert_start(2)
l2.insert_start(1)
l2.insert_end(4)
l2.insert_end(5)

l2.print_l()

l2.del_start()
l2.print_l()

l2.del_end()
l2.print_l()

print(l2.search(2))    

