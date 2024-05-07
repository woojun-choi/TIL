
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
            raise TypeError("left should refer to Node object.")
        self._left = obj

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, obj):
        if obj is not None and not isinstance(obj, Node):  
            raise TypeError("right should refer to Node object.")
        self._right = obj

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, obj):
        if obj is not None and not isinstance(obj, Node):  
            raise TypeError("parent should refer to Node object.")
        self._parent = obj

    def __str__(self):
        return "Node({})".format(self.data)
    
    def __repr__(self):
        return str(self)

    def count_children(self):
        if not self.left and not self.right:
            return 0
        elif self.left and self.right:
            return 2
        else:
            return 1

    def children(self):
        if self.count_children() == 2:
          return [self.left, self.right]
        elif self.left:  # self.count_children() == 1 and => elif의 경우로 생각해보면 없어도 됨
          return [self.left]
        elif self._right:  # self.count_children() == 1 and
          return [self.right]
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
        while cur:  # is not None
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
        
        if self.empty(): #예외 X, 아무것도 안하게
            return
        
        node = self.search(data=data) # 삭제 노드 찾기
        if node is None:
            return
        # raise IndexError(node.parent, node.data, node.left, node.right, node.parent.left, node.parent.right, node.parent.data)
        # raise IndexError(self._root, self._root.data, self._root.left, self._root.right)
        
        remove_node = node # 삭제할 노드객체
        # 자식 0개
        if not node.left and not node.right:
            if node == self._root:
                self._root = None
            elif data < node.parent.data:
                node.parent.left = None
            else:
                node.parent.right = None

        # 자식 1개
        elif node.left and not node.right:  # 왼쪽 자식이 있을 때
            if node == self._root:
                node.left.parent = None
                self._root = node.left
            elif data < node.parent.data:
                node.left.parent = node.parent
                node.parent.left = node.left
            else:
                node.left.parent = node.parent
                node.parent.right = node.left
        elif not node.left and node.right:  # 오른쪽 자식이 있을 때 
            if node == self._root:
                node.right.parent = None
                self._root = node.right
            elif data < node.parent.data:
                node.right.parent = node.parent
                node.parent.left = node.right
            else:
                node.right.parent = node.parent
                node.parent.right = node.right

        # 자식 2개
        else:  # 왼쪽 최대가 아닌 오른쪽 최소로 교체해준다.
            node_min_right = self.min(root=node.right, get_node=True)  # 오른쪽 최소 구하기
            node.data, node_min_right.data = node_min_right.data, node.data # 값 서로 바꾸기
            #4-1: 삭제 노드 바로 아래 최소 노드가 있을 때
            if node.right == node_min_right:  # and node_min_right.count_children == 0
                if node_min_right.right:
                    node.right, node_min_right.right.parent = node_min_right.right, node
                else:
                    node.right = None
            #4-2: 최소 노드의 오른쪽 자식 노드가 존재할 때
            elif node_min_right.right:
                node_min_right.parent.left, node_min_right.right.parent = node_min_right.right, node_min_right.parent
            #4-3: 나머지
            else:
                node_min_right.parent.left = None
            remove_node = node_min_right
        
        self._num_nodes -= 1
        # raise IndexError(self.inorder(), self._root, remove_node)
        return remove_node
    
    def clear(self):
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
            clear_node = temp.pop()
            clear_node.parent = clear_node.left = clear_node.right = None
            self._num_nodes -= 1
        self._root = None
        if self._num_nodes:
            return False
        else:
            return True
