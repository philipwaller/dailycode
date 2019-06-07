
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
    if not node.left and not node.right:
        return (node, 1)

    if not node.left:
        return increment_depth(deepest(node.right))

    if not node.right:
        return increment_depth(deepest(node.left))

    return increment_depth(
            max(deepest(node.left), deepest(node.right), key=lambda x: x[1]))

def increment_depth(node_depth):
    node, depth = node_depth
    return (node, depth + 1)


node = Node('root', 
        Node('left', \
            Node('left.left'), \
            Node('left.right', Node('left.right.left'), Node('left.right.right'))), \
        Node('right', \
            Node('right.left', \
                Node('right.left.left', Node('right.left.left.left')), \
                Node('right.right', None, Node('right.right.right'))), \
            Node('right.right')) \
        ) 

print("{}".format(node.serialize()))
print("{} == {}".format(node.count(), count(node)))

deepest_node = deepest(node)
print("{} : {}".format(deepest_node[0].serialize(), deepest_node[1]))

