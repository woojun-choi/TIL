class Node(object):
    def __init__(self, dt=object()):
        self._data = dt
        self._next = None
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, dt=object()):
        self._data = dt
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, nt):
        self._next = nt
    
class SinglyLinkedList(object):
    def __init__(self, head=Node(), tail=Node(), num_nodes=0):
        self._head = head
        self._tail = tail
        self._num_nodes = num_nodes
        
    def __str__(self):
        if self.empty():
            return "[]"
        else:
            tmp_list = []  # Temporary list of strings
            cur = self._head            
            while cur != None:
                tmp_list.append("[%s]"%(cur.data))
                cur = cur.next
        
            return "->".join(tmp_list)
        
    def __len__(self):
        return self._num_nodes 
            
    def empty(self):
        return False if self.__len__() else True
        
    def insert(self, i=0, data=object()):
        if i < 0 or i > self._num_nodes:
            raise IndexError
        new_node = Node(data)
        if i == 0:
            new_node.next = self._head
            self._head = new_node
            if self.empty():
                self._tail = new_node
        elif i == self._num_nodes:
            self._tail.next = new_node
            self._tail = new_node
        else:
            pre_node = self._head
            for idx in range(i - 1):
                pre_node = pre_node.next
            new_node.next = pre_node.next
            pre_node.next = new_node
        self._num_nodes += 1

    def remove(self, i):
        if self.empty():
            pass
        elif i < 0 or i > self._num_nodes:
            raise IndexError
        
        del_node = self._head
        if i == 0:
            self._head = self._head.next
            del_node.next = None
            if self._num_nodes == 1:
                self._tail = None
        else:
            for idx in range(i - 1):
                del_node = del_node.next
            pre_node = del_node.next
            del_node.next = pre_node.next
            pre_node.next = None
            if i == self._num_nodes - 1:
                self._tail = del_node
        self._num_nodes -= 1

    def clear(self):
        del_node = self._head
        while del_node != None:
            temp = del_node
            del_node = del_node.next
            temp.next = None
        self._head, self._tail, self._num_nodes = None, None, 0
    
    def get(self, i):
        #if self.__len__() or i>self._num_nodes:
        #    raise IndexError
        if self.empty():
            raise IndexError
        elif i < 0 or i > self._num_nodes:
            raise IndexError
        #idx = 0
        idx_node = self._head
        for a in range(i):
            idx_node = idx_node.next
        return idx_node.data
    
    def pop(self, i=None):
        if self.empty():
            raise IndexError
        
        if i is None:
            i = self._num_nodes - 1
        elif i < 0 or i > self._num_nodes:
            raise IndexError
        
        pop_node = Node()
        if i == 0:
            pop_node = self._head
            self._head = self._head.next
            if self._num_nodes == 1:
                self._tail = None
        else:
            pre_node = self._head
            for idx in range(i - 1):
                pre_node = pre_node.next
            pop_node = pre_node.next
            pre_node.next = pop_node.next
            if i == self._num_nodes - 1:
                self._tail = pre_node
        
        self._num_nodes -= 1
        return pop_node.data
    
    def search(self, target, start=0):
        if self.empty():
            raise IndexError
        elif start < 0 or start >= self._num_nodes:
            raise IndexError
        
        cur_node = self._head
        i = 0
        for a in range(start):
            cur_node = cur_node.next
            i += 1
        
        for b in range(self._num_nodes-start):
            if cur_node.data == target:
                return cur_node.data, i
            cur_node = cur_node.next
            i += 1
        
        return None, -1

    def extend(self, sll):
        if not isinstance(sll, SinglyLinkedList):
            raise TypeError
        else:
            sll_node = sll._head
            while sll_node != None:
                self.insert(self._num_nodes, sll_node.data)
                sll_node = sll_node.next