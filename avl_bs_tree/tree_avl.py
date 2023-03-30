
class Node:
    def __init__(self, left_child=None, right_child=None,
                 parent=None, value=None, balance=0):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value
        self.parent = parent
        self.balance = balance

    def get_height(self):
        highest = max(self._left_height(), self._right_height())
        return highest + 1

    def _left_height(self):
        height = 0
        current_child = self.left_child
        while current_child:
            height += 1
            current_child = current_child.left_child
        return height

    def _right_height(self):
        height = 0
        current_child = self.right_child
        while current_child:
            height += 1
            current_child = current_child.right_child
        return height

    def update_balance(self):  # zaktualizowanie balansu
        if self.right_child:
            right_height = self.right_child.get_height()
        else:
            right_height = 0
        if self.left_child:
            left_height = self.left_child.get_height()
        else:
            left_height = 0
        self.balance = right_height - left_height

    def to_string(self, depth=0):
        _str = ""
        if self.right_child:
            _str += self.right_child.to_string(depth + 1)
        _str += '\t' * depth + "->" + str(self.value) + "<\n"
        if self.left_child:
            _str += self.left_child.to_string(depth + 1)
        return _str


class AvlTree:
    def __init__(self, root=None, values=None):
        self.root = root
        if values is not None:
            for value in values:
                self.add(value)

    def add(self, value):
        if self.root is None:
            self.root = Node(value=value)
            return self.root
        node = self.root
        while node is not None:
            if value < node.value:
                if node.left_child is None:
                    node.left_child = Node(parent=node, value=value)
                    continue
                node = node.left_child
            elif value > node.value:
                if node.right_child is None:
                    node.right_child = Node(parent=node, value=value)
                    continue
                node = node.right_child
            elif value == node.value:
                break
        self._checking_balance(node)
        return node

    def _checking_balance(self, node):
        while node:
            if node.balance < -1 or node.balance > 1:
                self._adjust_balance(node)
                return

            if node.parent:
                if node.parent.left_child == node:
                    node.parent.balance -= 1
                else:
                    node.parent.balance += 1
                if node.parent.balance != 0:
                    node = node.parent
                    continue
            return

    def _adjust_balance(self, node):
        if node.balance > 0:
            if node.right_child.balance < 0:
                self._right_rotation(node.right_child)
            self._left_rotation(node)

        elif node.balance < 0:
            if node.left_child.balance > 0:
                self._left_rotation(node.left_child)
            self._right_rotation(node)

    def _left_rotation(self, node):
        pivot = node.right_child
        node.right_child = pivot.left_child

        if pivot.left_child:
            pivot.left_child.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node == node.parent.left_child:
            node.parent.left_child = pivot
        else:
            node.parent.right_child = pivot
        pivot.left_child = node
        node.parent = pivot

        node.update_balance()
        pivot.update_balance()

    def _get_root(self, node):
        if node.balance > 0:
            if node.right_child.balance < 0:
                return node.right_child.left_child
            else:
                return node.right_child
        else:
            if node.left_child.balance > 0:
                return node.left_child.right_child
            else:
                return node.left_child

    def _right_rotation(self, node):
        pivot = node.left_child
        node.left_child = pivot.right_child

        if pivot.right_child:
            pivot.right_child.parent = node

        pivot.parent = node.parent
        if node.parent is None:
            self.root = pivot
        elif node == node.parent.right_child:
            node.parent.right_child = pivot
        else:
            node.parent.left_child = pivot

        pivot.right_child = node
        node.parent = pivot

        node.update_balance()
        pivot.update_balance()

    def remove_node(self, value):
        node = self.find(value)
        if node.left_child is None or node.right_child is None:
            y = node
        else:
            y = self.find_succesor(node)
        if y.left_child is not None:
            x = y.left_child
        else:
            x = y.right_child
        if x is not None:
            x.parent = y.parent
        if y.parent is None:
            self.root = x
        else:
            if y == y.parent.left_child:
                y.parent.left_child = x
            else:
                y.parent.right_child = x
        if y != node:
            node.value = y.value
        node = y.parent
        if node is not None:
            node.update_balance()
            self._check_removed_balance(node)

    def _check_removed_balance(self, node):
        if node.balance > 1 or node.balance < -1:
            new_root = self._get_root(node)
            self._adjust_balance(node)

            if (new_root.balance == 0 and
                    new_root.balance == -1 or new_root.balance == 1):
                return

            node = new_root
        if node.parent:
            parent_balance = node.parent.balance

            if node.parent.left_child == node:
                node.parent.balance += 1
            else:
                node.parent.balance -= 1

            if (parent_balance != 0 or
                    node.parent.balance > 1 or node.parent.balance < -1):
                self._check_removed_balance(node.parent)

    def find(self, value):
        node = self.root
        while node is not None and node.value != value:
            if value < node.value:
                node = node.left_child
            elif value > node.value:
                node = node.right_child
        return node

    def find_succesor(self, node=None):
        node = node if node else self.root
        if node.right_child is not None:
            return self.find_min_key(node.right_child)
        node_tmp = node.parent
        while node_tmp is not None and node_tmp.left_child != node:
            node = node_tmp
            node_tmp = node_tmp.parent
        return node_tmp

    def find_min_key(self, node=None):
        node = node if node else self.root
        while node.left_child is not None:
            node = node.left_child
        return node

    def __str__(self):
        if not self.root:
            return ""
        return self.root.to_string()


if __name__ == "__main__":
    values = [10, 5, 7, 8, 9, 15, 2, 6, 90, 12, 0, 1, 3, 11, 13, 17, 4]
    avl = AvlTree(values=values)
    avl.remove_node(5)
    print(avl)
