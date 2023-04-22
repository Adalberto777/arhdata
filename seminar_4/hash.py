class Hash_table:
    def __init__(self):
        self.size = 10
        self.table = [[] for i in range(self.size)]
        #[[[0, 'fdg'], [10,'gffg'], [100,'fggffg']],[[2,'fdf'],[22, 'dffd']],[],[],[],[],[],[],[],[]]


    def hash(self, key):
        return key % self.size


    def insert(self, key, val): # key = 10 val = 'dsds'
        index = self.hash(key) # index = 0
        for i in range(len(self.table[index])): # [[0, 'fdg'], [10,'gffg'], [100,'fggffg']]
            if self.table[index][i][0] == key:
                self.table[index][i][1] = val
                return
        self.table[index].append([key, val])


    def printTable(self):
        for i in self.table:
            if len(i) != 0:
                print(*i )

    def searh(self, key):
        index = self.hash(key)
        for i in self.table[index]:
            if i[0] == key:
                return i[1]
        


hashTable = Hash_table()
hashTable.insert(0, 'A')
hashTable.insert(10, 'l')
hashTable.insert(100, 'b')
hashTable.insert(1000, 'e')
hashTable.insert(1, 'r')
hashTable.insert(11, 't')
hashTable.insert(111, '!')

hashTable.printTable()

hashTable.insert(111, '&')
hashTable.printTable()
print(hashTable.searh(0))
print(hashTable.searh(3))
