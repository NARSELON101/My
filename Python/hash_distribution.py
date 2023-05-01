class binary_tree:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    rtnList = []
    def add(self, x):
        if self.value == None:
            self.value = x
            return
        else:
            if x < self.value:
                if self.left == None:
                    self.left = binary_tree(x)
                else:
                    self.left.add(x)
            elif self.value < x:
                    if self.right == None:
                        self.right = binary_tree(x)
                    else:
                        self.right.add(x)

    def InorderTravesal(self):


        if self.left != None:
            self.left.InorderTravesal()
        
        self.rtnList.append(self.value)

        if self.right != None:
            self.right.InorderTravesal()
        
    def printRoot(self):
        print(self.right.right.value)
    
tree = binary_tree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.printRoot()


