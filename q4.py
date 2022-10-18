# ------------------------------------------------------ #
# abstract : assignment 1 Question 4 Tree
# author : hhk
# time : 2022.10.13
# ------------------------------------------------------ #

# --------- definition --------- #
class Node:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def Print(self):
        if self.data is None:
            return
        if self.left:
            self.left.Print()
        print(self.data,end=" "),
        if self.right:
            self.right.Print()

    def Search(self,val):
        if self.data:
            if self.data == val:
                print(self)
                return self
            elif self.data>val:
                if self.left is None:
                    print('left')
                    return None
                else:
                    self.left.Search(val)
            elif self.data<val:
                if self.right is None:
                    print('right')
                    return None
                else:
                    self.right.Search(val)
        else:
            return None


class Tree:
    def __init__(self,data = None):
        """
        initialize root node
        """
        self.root = Node(data)           # 根节点

    def GetRoot(self):
        """
        return root node
        """
        return self.root


    def Insert(self,val):
        """
        insert node
        """
        self.root.insert(val)

    def PrintTree(self):
        """
        print the tree
        """
        if self.root.data is None:
            print("Nothing in tree\n")
        else:
            print("Values in tree")
            self.root.Print()
            print('\n')

    def SearchTree(self,val):
        """
        search value by input val
        return node if value == input, return None otherwise
        """
        print(self.root.Search(val))
        # a = self.root.Search(val)
        # print(a)
        # return a
        # return self.root.Search(val)


    def Delete(self,val=None):
        """
        delete node according to input value;
        delete node, whose value equals to input, and its children
        """
        if val is None:
            del self.root
            self.root = Node()
            return
        if self.SearchTree(val):
            a = self.SearchTree(val)
            del a
        else:
            print("The value does not exist in the tree")
            return


# --------- main part --------- #

tree = Tree()
tree.Insert(8)
tree.Insert(10)
tree.Insert(1)
tree.Insert(6)
tree.Insert(15)
tree.PrintTree()

tree.PrintTree()

content = [1,5,99,15,100,35,23,20,16,13]
for num in content:
    tree.Insert(num)
tree.PrintTree()

