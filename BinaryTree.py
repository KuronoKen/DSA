class BSTNode:
    def __init__(self, data:int=None):
        self.data = data
        self.left = None
        self.right = None
        pass

class BST:
    def __init__(self,root:BSTNode=None):
        self.root = root
        pass
    def insert(self,data):
        pointer = self.root
        if not pointer:
            self.root = BSTNode(data)
        while pointer != None:
            if data >= pointer.data:
                if pointer.right == None:
                    pointer.right = BSTNode(data)
                    break
                else:
                    pointer = pointer.right
            elif data < pointer.data:
                if pointer.left == None:
                    pointer.left = BSTNode(data)
                    break
                else:
                    pointer = pointer.left
    def preorder(self):
        def preordertraverse(node:BSTNode,preor):
            if node:
                preor = preor + "-> " + str(node.data) + " "
                preor = preordertraverse(node.left,preor)
                preor = preordertraverse(node.right,preor)
            return preor
        preortext = "Preorder: "
        print(preordertraverse(self.root,preortext))
    def is_empty(self):
        if self.root:
            return False
        else:
            return True
    def inorder(self):
        def ordertraverse(node:BSTNode,order):
            if node:
                order = ordertraverse(node.left,order)
                order = order + "-> " + str(node.data) + " "
                order = ordertraverse(node.right,order)
            return order
        text = "Inorder: "
        print(ordertraverse(self.root,text))
    def postorder(self):
        def ordertraverse(node:BSTNode,order):
            if node:
                order = ordertraverse(node.left,order)
                order = ordertraverse(node.right,order)
                order = order + "-> " + str(node.data) + " "
            return order
        text = "Postorder: "
        print(ordertraverse(self.root,text))
    def traverse(self):
        if not self.is_empty():
            self.preorder()
            self.inorder()
            self.postorder()
        else:
            print("This is an empty binary search tree.")
    def find_max(self,start=None):
        pointer = self.root
        if start:
            pointer = start
        maxnum = None
        if pointer:
            while pointer != None:
                if maxnum == None:
                    maxnum = pointer.data
                elif pointer.data > maxnum:
                    maxnum = pointer.data
                pointer = pointer.right
        return maxnum
    def find_min(self):
        pointer = self.root
        minnum = None
        if pointer:
            while pointer != None:
                if minnum == None:
                    minnum = pointer.data
                elif pointer.data < minnum:
                    minnum = pointer.data
                pointer = pointer.left
        return minnum
    def delete(self,data,start:BSTNode=None,formerstart=None):
        pointer = self.root
        former = None
        if start:
            pointer = start
            former = formerstart
        while pointer:
            if pointer.data != data:
                if data >= pointer.data:
                    former = pointer
                    pointer = pointer.right
                elif data < pointer.data:
                    former = pointer
                    pointer = pointer.left
            else:
                if not pointer.left and not pointer.right:
                    if former == None:
                        self.root = None
                    else:
                        if pointer == former.left:
                            former.left = None
                        elif pointer == former.right:
                            former.right = None
                elif bool(pointer.left) != bool(pointer.right):
                    if pointer.left:
                        if former == None:
                            self.root = pointer.left
                        else:
                            if pointer == former.left:
                                former.left = pointer.left
                            elif pointer == former.right:
                                former.right = pointer.left
                    elif pointer.right:
                        if former == None:
                            self.root = pointer.right
                        else:
                            if pointer == former.left:
                                former.left = pointer.right
                            elif pointer == former.right:
                                former.right = pointer.right
                elif pointer.left and pointer.right:
                    maxnumofleft = self.find_max(pointer.left)
                    pointer.data = maxnumofleft
                    self.delete(maxnumofleft,pointer.left,pointer)
                return data
        print("Delete Error, "+ str(data) + " is not found in Binary Search Tree.")
        return None



def main():
  my_bst = BST()
  while 1:
    text = input()
    if text == "Done":
      break
    condition, data = text.split(": ")
    if condition == "I":
      my_bst.insert(int(data))
    elif condition == "D":
      my_bst.delete(int(data))
    else:
      print("Invalid Condition")
  my_bst.traverse()

main()