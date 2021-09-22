class Node:
    def __init__(self, data):
        self.data = data
        self.left =None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = Node(root)


    def insert(self, new_data):
        self.insert_it(new_data, self.root)


    def insert_it(self, new_data, at_node):
        if at_node is None:
            at_node = Node(new_data)
        elif at_node.data < new_data:
            if at_node.right is None:
                at_node.right = Node(new_data)
            else:
                self.insert_it(new_data, at_node.right)
        elif at_node.data > new_data:
            if at_node.left is None:
                at_node.left = Node(new_data)
            else:
                self.insert_it(new_data, at_node.left)
        else:
            print(f"{new_data = } already exists in the BST")


    def preorder(self, node, transverse_string):
        """
        root -> left->right
        """
        if node != None:
            transverse_string += " " + str(node.data)
            transverse_string = self.preorder(node.left, transverse_string)
            transverse_string = self.preorder(node.right, transverse_string)
        return transverse_string

    def print_tree(self, tranverse_type = "inorder"):
        if tranverse_type.lower() == "preorder":
            return self.preorder(self.root, transverse_string="Preorder= ")
        elif tranverse_type.lower() == "inorder":
            return self.inorder(self.root,tranverse_string="Inorder= ")
        elif tranverse_type.lower() == "postorder":
            return self.postorder(self.root,tranverse_string="Postorder= ")


    def inorder(self, node, tranverse_string ):
        """
         left -> root -> right
        """
        if node != None:
            tranverse_string = self.inorder(node.left, tranverse_string)
            tranverse_string += " " + str(node.data)
            tranverse_string = self.inorder(node.right, tranverse_string)
        return tranverse_string


    def postorder(self, node, tranverse_string ):
        """
         left -> right -> root
        """
        if node != None:
            tranverse_string = self.postorder(node.left, tranverse_string)
            tranverse_string = self.postorder(node.right, tranverse_string)
            tranverse_string += " " + str(node.data)
        return tranverse_string

trial = BST(10)
trial.insert(13)
trial.insert(2)
trial.insert(6)
trial.insert(8)
trial.insert(17)
trial.insert(9)
"""
            10
           /   \
          8     13
        /   \     \
       6     9     17
      /
     2 
"""
print(trial.print_tree("Preorder"))
print(trial.print_tree())
print(trial.print_tree("postorder"))