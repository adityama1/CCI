class Treenode:
    num_of_elements = 0

    def __init__(self, cargo, left_ptr=None, right_ptr=None):
        self.cargo = cargo
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr
        self.num_of_elements += 1

    def hasLeftChild(self):
        return self.left_ptr

    def hasRightChild(self):
        return self.right_ptr


class BuildTree:

    def __init__(self):
        self.root = None

    def put(self, value):
        if not self.root:
            self.root = Treenode(value)

        else:
            self._put(self.root,value)

    def _put(self, currentNode, value):
        if value <= currentNode.cargo:
            if currentNode.hasLeftChild():
                self._put(currentNode.left_ptr, value)
            else:
                currentNode.left_ptr = Treenode(value)
        else:
            if currentNode.hasRightChild():
                self._put(currentNode.right_ptr,value)
            else:
                currentNode.right_ptr = Treenode(value)

    def printInorder(self,root):
        if root is None:
            return
        else:
            self.printInorder(root.left_ptr)
            print root.cargo
            self.printInorder(root.right_ptr)

'''
    def __iter__(self):
       if self:
          if self.root.hasLeftChild():
              for elem in self.root.left_ptr:
                  yield elem
          yield self.root.cargo
          if self.root.hasRightChild():
              for elem in self.root.right_ptr:
                  yield elem
'''


def main():
    mytree = BuildTree()
    mytree.put(7)
    mytree.put(6)
    mytree.put(11)
    mytree.put(3)
    mytree.put(2)
    mytree.put(12)
    mytree.put(20)
    mytree.put(-2)
    mytree.printInorder(mytree.root)

if __name__ == '__main__':
    main()