from distutils.command.build import build


class BuildTree:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def buildTree(self,data):
        if self.data == data:
            return
        
        if self.data > data:
            if self.left:
                self.left.buildTree(data)
            else:
                self.left = BuildTree(data)

        elif self.data < data:
            if self.right:
                self.right.buildTree(data)

            else:
                self.right = BuildTree(data)

    
    def preorder(self,root):
        if root:
            print(root.data)
            self.preorder(root.left)
            self.preorder(root.right)



a = BuildTree(10)
a.buildTree(2)
a.buildTree(8)
a.buildTree(80)
a.buildTree(11)
a.buildTree(1)
a.preorder(a)