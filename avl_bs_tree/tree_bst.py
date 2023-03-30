class BstNode:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def __str__(self):
        return str(self.value)


def traverse_preorder(node):
    if node:
        print(node.value)
    if node.left:
        traverse_preorder(node.left)
    if node.right:
        traverse_preorder(node.right)
    return


def traverse_inorder(node):
    if node.left:
        traverse_inorder(node.left)

    print(node)

    if node.right:
        traverse_inorder(node.right)


def traverse_postorder(node):
    if node.left:
        traverse_postorder(node.left)

    if node.right:
        traverse_postorder(node.right)

    print(node)


def search_bst(root, key):
    if key is None:
        return 0
    if key == root.value:
        return True
    if key < root.value:
        if root.left:
            return search_bst(root.left, key)
        return False
    elif key > root.value:
        if root.right:
            return search_bst(root.right, key)
        return False


def insert_bst(root, value):
    if root is None:
        return BstNode(value)
    if value == root.value:
        return root
    if value < root.value:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root


def find_minimum(root):
    current_node = root
    while current_node.left is not None:
        current_node = current_node.left
    return current_node


def delete_node_bst(root, value):
    if root is None:
        return root

    if value < root.value:
        root.left = delete_node_bst(root.left, value)

    elif value > root.value:
        root.right = delete_node_bst(root.right, value)

    else:
        if root.left is None:
            temp_root = root.right
            root = None
            return temp_root

        elif root.right is None:
            temp_root = root.left
            root = None
            return temp_root

        temp_successor = find_minimum(root.right)
        root.value = temp_successor.value
        root.right = delete_node_bst(root.right, temp_successor.value)
    return root


def print_tree_bst(root, indent=0):
    if root is not None:
        print_tree_bst(root.right, indent + 1)
        print(' ' * 4 * indent + '>' + str(root.value))
        print_tree_bst(root.left, indent + 1)


def main():
    root = BstNode(8)
    root.left = BstNode(3)
    root.right = BstNode(10)
    # root.left.left = BstNode(1)
    root.left.right = BstNode(6)
    root.left.right.left = BstNode(4)
    root.left.right.right = BstNode(7)
    root.right.right = BstNode(14)
    root.right.right.left = BstNode(13)
    # delete_node_bst(root, 6)
    # delete_node_bst(root, 4)
    # delete_node_bst(root, 7)
    insert_bst(root, 1)
    # print(traverse_inorder(root))
    print_tree_bst(root)
    # print(search_bst(root, 3))


if __name__ == "__main__":
    main()