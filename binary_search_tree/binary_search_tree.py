class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        def go(value, curr):
            if value > curr.value:
                if curr.right is None:
                    curr.right = BinarySearchTree(value)
                    return
                else:
                    go(value, curr.right)
            elif value < curr.value:
                if curr.left is None:
                    curr.left = BinarySearchTree(value)
                    return
                else:
                    go(value, curr.left)
        go(value, self)

    def contains(self, target):
        def go(value, curr):
            if value == curr.value:
                return True
            elif value > curr.value:
                if curr.right is None:
                    return False
                else:
                    return go(value, curr.right)
            elif value < curr.value:
                if curr.left is None:
                    return False
                else:
                    return go(value, curr.left)
        return go(target, self)

    def get_max(self):
        def go(curr):
            if curr.right is None:
                return curr.value
            return go(curr.right)
        return go(self)

    def for_each(self, cb):
        def go(curr):
            cb(curr.value)
            if curr.left:
                go(curr.left)
            if curr.right:
                go(curr.right)
        go(self)
