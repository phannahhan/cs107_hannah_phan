from enum import Enum


class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node:
            return BSTNode(key, val)
        if key < node.key:
            node.left = self._put(node.left, key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            return self._get(node.left, key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    def _removemin(self, node):
        # if left node doesn't exist, go to right node and delete null left node
        if not node.left:
            return node.right
        # Go left until finding a node with a null left link.
        # Replace that node by its right link.
        # Update subtree counts.
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            # if there is no right child
            if not node.right:
                return node.left
            # if there is no left child
            if not node.left:
                return node.right
            # if has both left and right, find min of right node as the new current node
            temp = node
            node = temp.right
            while node.left:
                node = node.left
            node.right = self._removemin(temp.right)
            node.left = temp.left
            
        # update the size of the nodes
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    @staticmethod
    def _size(node):
        return node.size if node else 0


class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        self.nodelists = []
        self.tree = tree
        self.traversalType = traversalType

        if self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        elif traversalType == DFSTraversalTypes.INORDER:
            self.inorder(tree)
        elif traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.nodelists) == 0:
            raise StopIteration()
        return self.nodelists.pop(0)

    def preorder(self, bst: BSTTable):
        def _traverse(bst: BSTNode):
            if not bst:
                return
            self.nodelists.append(bst)
            _traverse(bst.left)
            _traverse(bst.right)

        if len(bst) > 0:
            _traverse(bst._root)

    def inorder(self, bst: BSTTable):
        def _traverse(bst: BSTNode):
            if not bst:
                return
            _traverse(bst.left)
            self.nodelists.append(bst)
            _traverse(bst.right)

        if len(bst) > 0:
            _traverse(bst._root)

    def postorder(self, bst: BSTTable):
        def _traverse(bst: BSTNode):
            if not bst:
                return
            _traverse(bst.left)
            _traverse(bst.right)
            self.nodelists.append(bst)

        if len(bst) > 0:
            _traverse(bst._root)

# Demo Part A
# tree = BSTTable()
# tree.put(0, 'd')
# tree.put(2, 'c')
# tree.put(5, 'a')
# tree.put(1, 'b')
# print(tree._root)
# print(tree._removemin(tree._root))

# Demo Part B
# tree = BSTTable()
# tree.put(5, 'a')
# tree.put(1, 'b')
# tree.put(2, 'c')
# tree.put(0, 'd')
# tree.remove(5)
# print(tree)
# tree.remove(1)
# print(tree)

# Demo Part C
# input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
# bst = BSTTable()
# for key, val in input_array:
#     bst.put(key, val)
# traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
# for node in traversal:
#     print(str(node.key) + ', ' + node.val)

