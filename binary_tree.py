class Node:
    def __init__(self, value, left = None, right = None ):
        """

        :param value:
        :param left:
        :param right:
        """
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, root = None):
        self.root = Node(root)

    def preorder(self, node, transverse_string):
        """
        root -> left->right
        """
        if node != None:
            transverse_string += " " + str(node.value)
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
            tranverse_string += " " + str(node.value)
            tranverse_string = self.inorder(node.right, tranverse_string)
        return tranverse_string

    def postorder(self, node, tranverse_string ):
        """
         left -> right -> root
        """
        if node != None:
            tranverse_string = self.postorder(node.left, tranverse_string)
            tranverse_string = self.postorder(node.right, tranverse_string)
            tranverse_string += " " + str(node.value)
        return tranverse_string
"""
                  1
                /    \
               /      \
              2        3
             /  \      / \
            4    5    6  7
"""
trial = BinaryTree(1)
trial.root.right = Node(3)
trial.root.left = Node(2)
trial.root.left.left = Node(4)
trial.root.left.right = Node(5)
trial.root.right.left = Node(6)
trial.root.right.right = Node(7)
print(trial.print_tree("preorder"))
print(trial.print_tree())
print(trial.print_tree("Postorder"))