class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children=[]
        self.parent=None

    def add_children(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level +=1
            p=p.parent


        return level

    def print(self):
        spaces=' '*self.get_level()*3
        prefix=spaces+'|__'if self.parent else ''#conditional operator in python
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print()
def built():
        root=TreeNode("Electronic")
        laptop=TreeNode("laptop")
        laptop.add_children(TreeNode("Mac"))
        laptop.add_children(TreeNode("Surface"))
        laptop.add_children(TreeNode("Thinkpad"))

        cellphone=TreeNode("cellphone")
        cellphone.add_children(TreeNode("Iphone"))
        cellphone.add_children(TreeNode("Google Pixel"))
        cellphone.add_children(TreeNode("Vivo"))

        tv=TreeNode("Tv")
        tv.add_children(TreeNode("samsung"))
        tv.add_children(TreeNode("LG"))
        root.add_children(laptop)
        root.add_children(cellphone)
        root.add_children(tv)
        root.print()

if __name__=="__main__":
    built()