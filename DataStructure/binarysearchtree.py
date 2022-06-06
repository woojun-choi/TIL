
class Node:
    def __init__(self, data=None, left=None, right=None, parent=None):
        self._data = data
        self._left = left
        self._right = right
        self._parent = parent

    @property  # getter
    def data(self):
        return self._data

    @data.setter  # setter
    def data(self, data):
        self._data = data

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, obj):
        if obj is not None and not isinstance(obj, Node):  # 예외사항
            raise TypeError("next should refer to Node object.")
        self._left = obj

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, obj):
        if obj is not None and not isinstance(obj, Node):  # 예외사항
            raise TypeError("next should refer to Node object.")
        self._right = obj

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, obj):
        if obj is not None and not isinstance(obj, Node):  # 예외사항
            raise TypeError("next should refer to Node object.")
        self._parent = obj

    def __str__(self):
        return "Node({})".format(self.data)
    
    def __repr__(self):
        return str(self)

    def count_children(self):
        if self._left is None and self._right is None:
            return 0
        elif self._left is None or self._right is None:
            return 1
        else:
            return 2

    def children(self):
        if self.count_children() == 2:
          return [self._left, self._right]
        elif self.count_children() == 1 and self._left:
          return [self._left]
        elif self.count_children() == 1 and self._right:
          return [self._right]
        else:
          return []


class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._num_nodes = 0

    def __len__(self):
        return self._num_nodes

    def empty(self):
        if self._num_nodes == 0:
            return True
        else:
            return False
    
    def insert(self, data):     
        def insert_node(node, data): #함수 활용
            if data == node.data: #이미 값이 있다면
                return
            elif data < node.data: #값이 현재 노드보다 작다면
                if node.left is None:
                    node.left = Node(data)
                    self._num_nodes += 1
                else:
                    insert_node(node.left, data)
            else: #값이 현재 노드보다 크다면
                if node.right is None:
                    node.right = Node(data)
                    self._num_nodes += 1
                else:
                    insert_node(node.right, data)
            return
        
        if self.empty():
            self._root = Node(data)
            self._num_nodes += 1
        else:
            return insert_node(self._root, data)

    #순회는 재귀가 아닌 while문을 사용할 것을 권장
    def preorder(self, get_node=False): #전위 순회
        traversal = []
        if self.empty():
            raise IndexError("BinarySearchTree is empty")
        stack = [self._root]
        while stack:
            node = stack.pop()
            traversal.append(node) if get_node else traversal.append(node.data)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return traversal
    
    def inorder(self, get_node=False): #중위 순회
        traversal = []
        if self.empty():
            raise IndexError("BinarySearchTree is empty")
        stack = []
        node = self._root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node) if get_node else traversal.append(node.data)
                node = node.right
        return traversal
    
    def postorder(self, get_node=False): #후위 순회
        traversal = []
        if self.empty():
            raise IndexError("BinarySearchTree is empty")
        stack = [self._root]
        temp = []
        while stack:
            node = stack.pop()
            temp.append(node) if get_node else temp.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while temp:
            traversal.append(temp.pop())
        return traversal

    def min(self, root=None, get_node=False):
        node = root if root else self._root
        while 1:
            if node.left:
                node = node.left
            else:
                break
        return node if get_node else node.data
    
    def max(self, root=None, get_node=False):
        node = root if root else self._root
        while 1:
            if node.right:
                node = node.right
            else:
                break
        return node if get_node else node.data
        
    def search(self, data):
        node = self._root
        while 1:
            if self.empty():
                raise IndexError("BinarySearchTree is empty")
            if node is None:
                return None
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right

    def remove(self, data):
        pass
    
    def clear(self):
        pass
