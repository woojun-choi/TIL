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
        if obj is not None and not isinstance(obj, Node):  
            raise TypeError("next should refer to Node object.")
        self._left = obj

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, obj):
        if obj is not None and not isinstance(obj, Node):  
            raise TypeError("next should refer to Node object.")
        self._right = obj

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, obj):
        if obj is not None and not isinstance(obj, Node):  
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
        #recusive
        # def insert_node(node, data): #함수 활용
        #     if data == node.data: #이미 값이 있다면
        #         return
        #     elif data < node.data: #값이 현재 노드보다 작다면
        #         if node.left is None:
        #             node.left = Node(data, parent=node)
        #             self._num_nodes += 1
        #         else:
        #             insert_node(node.left, data)
        #     else: #값이 현재 노드보다 크다면
        #         if node.right is None:
        #             node.right = Node(data, parent=node)
        #             self._num_nodes += 1
        #         else:
        #             insert_node(node.right, data)
        # #     return        
        # if self.empty(): # 비었으면 root로
        #     self._root = Node(data)
        #     self._num_nodes += 1
        # else:
        #     return insert_node(self._root, data)
        
        #non-recursive
        node = Node(data=data)
        if self.empty():
            self._root = node
            self._num_nodes += 1
            return
        cur = self._root
        while cur is not None:
            if data < cur.data:
                if cur.left is None:
                    node.parent = cur
                    cur.left = node
                    break
                cur = cur.left  # Go to the left 
            else: # data >= cur.data
                if cur.right is None:
                    node.parent = cur 
                    cur.right = node 
                    break
                cur = cur.right  # Go to the right # end of while
        self._num_nodes += 1

    #순회는 재귀가 아닌 while문을 사용할 것을 권장
    def preorder(self, get_node=False): #전위 순회
        traversal = [] # 결과값
        if self.empty(): # 예외 발생
            raise IndexError("BinarySearchTree is empty")
        stack = [self._root]
        while stack:
            node = stack.pop()
            traversal.append(node) if get_node else traversal.append(node.data) # get_node가 참이면 node, 거짓이면 node.data
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
        node = self._root # current node
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
        while node.left:
            node = node.left
        return node if get_node else node.data
    
    def max(self, root=None, get_node=False):
        node = root if root else self._root
        while node.right:
            node = node.right
        return node if get_node else node.data
    
    def search(self, data): 
        node = self._root
        if self.empty():
            raise IndexError("BinarySearchTree is empty")
        while node:
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def remove(self, data):
        remove_node = None #삭제 Node
        node = self._root # current
        node_parent = None # parent 저장용
        is_left_child = True #삭제 시 확인용 플래그
        
        if self.empty(): #예외 X, 아무것도 안하게
            return
        
        # while 1: # 삭제 노드 찾기 -무한 루프 가능성 있음
        #     if data == node.data:
        #         break
        #     else:
        #         if data < node.data:
        #             node = node.left
        #             is_left_child = True
        #         else:
        #             node = node.right
        #             is_left_child = False
        
        while node: # 삭제 노드 찾기
            if data == node.data:
                break
            elif data < node.data:
                # node_parent = node
                node = node.left
                is_left_child = True
            else:
                # node_parent = node
                node = node.right
                is_left_child = False
        if node is None:
            raise IndexError("No data to delete")
        
        remove_node = node
        node_parent = node.parent
        # 자식 0개
        if not node.left and not node.right:
            if node == self._root:
                self._root = None
            elif data < node.parent.data:
                node.parent.left = None
            else:
                node.parent.right = None
        
        # 자식 1개
        elif node.left and not node.right:
            if node == self._root:
                self._root = node.left
        elif node.left and node.right:
            if node == self._root:
                self._root = node.left
        
        # 자식 2개
        
        
        return remove_node
    
    def clear(self):
        #traversal = []
        if self.empty():
            return True
        stack = [self._root]
        temp = []
        while stack:
            node = stack.pop()
            temp.append(node) #if get_node else temp.append(node.data)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while temp:
            #traversal.append(temp.pop())
            clear_node = temp.pop()
            clear_node.parent = clear_node.left = clear_node.right = None
        self._root = None
        self._num_nodes = 0
        if self._num_nodes:
            return False
        else:
            return True
      

        #자식 X or 1개 -뭔가 안되는 듯?-?
        # if node.left is None: # 왼쪽 자식이 없을 때
        #     if node is self._root: # 삭제가 root면 오른쪽 연결
        #         remove_node = self._root
        #         self._root = node.right
        #     elif is_left_child:
        #         remove_node = node
        #         node.parent.left = node.right
        #     else:
        #         remove_node = node
        #         node.parent.right = node.right
        #     self._num_nodes -= 1
        # elif node.right is None: # 오른쪽 자식이 없을 때
        #     if node is self._root:
        #         remove_node = self._root
        #         self._root = node.left
        #     elif is_left_child:
        #         remove_node = node
        #         node.parent.left = node.left
        #     else:
        #         remove_node = node
        #         node.parent.right = node.left
        #     self._num_nodes -= 1
        
        '''
        remove_node = node # 삭제할 노드
        node_parent = node.parent # 혹시 몰라서
        # 자식 0개
        if not node.left and not node.right:
            if node == self._root:
                self._root = None
            if is_left_child:
                node_parent.left = None
                node.parent = None
            else:
                node_parent.right = None
                node.parent = None
            self._num_nodes -= 1
        
        #자식 1개
        elif node.left and not node.right:
            if node == self._root:
                self._root = node.left
            elif is_left_child:
                node_parent.left = node.left
                node.parent = node.left = node.right = None
            else:
                node.parent.right = node.left
                node.parent = node.left = node.right = None
            self._num_nodes -= 1
        
        elif not node.left and node.right:
            if node == self._root:
                self._root = node.right
            elif is_left_child:
                node_parent.left = node.right
                node.parent = node.left = node.right = None
            else:
                node_parent.right = node.right
                node.parent = node.left = node.right = None
            self._num_nodes -= 1
        
        # 자식 2개
        else:
            node_max_left = node.left
            is_left_child = True
            while node_max_left.right:  # 왼쪽에서 가장 큰 노드 찾기
                node_max_left = node_max_left.right
                is_left_child = False
            remove_node = node
            node.data = node_max_left.data
            if is_left_child:
                node_parent.left = node_max_left.left
            else:
                node_parent.right = node_max_left.right
            self._num_nodes -= 1
        '''
