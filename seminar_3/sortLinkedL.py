class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class List_2:
    def __init__(self):
        self.start_node = None
        self.end_node = None


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
            self.end_node = new_node #1
            return
        
        new_node.next = self.start_node
        self.start_node.prev = new_node
        self.start_node = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            self.end_node = new_node #1
            return
        
        n = self.start_node
        while n.next:
            n = n.next
        n.next = new_node
        new_node.prev = n
        self.end_node = new_node #1

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
    
    def revers(self):
        temp = self.start_node
        self.start_node = self.end_node
        self.end_node = temp

        n = self.start_node
        while n:
            temp = n.prev
            n.next = n.prev
            n.prev = next
            n = n.next          


l2 = List_2()
l2.insert_start(3)
l2.insert_start(2)
l2.insert_start(1)
l2.insert_end(4)
l2.insert_end(5)
l2.insert_end(6)
l2.insert_end(7)

l2.print_l()

l2.revers()
l2.print_l()

