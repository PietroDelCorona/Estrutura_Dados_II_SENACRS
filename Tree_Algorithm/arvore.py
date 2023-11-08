# ChatGPT

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            return "Traversal type not recognized."

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.data) + " ")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.data) + " ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.data) + " ")
        return traversal

# Criando uma árvore de exemplo
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Exemplo de impressão da árvore em ordem pré-fixada (preorder)
print("Árvore em pré-ordem (preorder):", tree.print_tree("preorder"))

# Exemplo de impressão da árvore em ordem central (inorder)
print("Árvore em ordem central (inorder):", tree.print_tree("inorder"))

# Exemplo de impressão da árvore em ordem pós-fixada (postorder)
print("Árvore em pós-ordem (postorder):", tree.print_tree("postorder"))