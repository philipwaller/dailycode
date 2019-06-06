
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def count(self):
        lhs = self.left.count() if self.left else 0
        rhs = self.right.count() if self.right else 0
        return 1 + lhs + rhs

    def serialize(self):
        val = self.val
        lhs = self.left.serialize() if self.left else None
        rhs = self.right.serialize() if self.right else None
        return [val, lhs, rhs]

    @classmethod
    def deserialize(cls, string):
        return cls('root', cls('left', cls('left.left')), cls('right'))

def count(node):
    return count(node.left) + count(node.right) + 1 if node else 0

def deepest(node):
    # @todo


node = Node(0, \
        Node(1, Node(1), Node(2, Node(1), Node(2))), \
        Node(2, Node(1, Node(1, Node(1)), Node(2, None, Node(2))), Node(2)) \
        ) 
print("{}".format(node.serialize()))

print("{} == {}".format(node.count(), count(node)))

