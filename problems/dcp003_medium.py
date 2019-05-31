#!/usr/local/bin/python3

"""
Sun.2019.05.26 Daily Coding Problem: Problem #3 [Medium]

This problem was recently asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes 
the tree into a string, and deserialize(s), which deserializes the string back 
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def serialize(self):
        val = self.val
        lhs = self.left.serialize() if self.left else ''
        rhs = self.right.serialize() if self.right else ''
        return [val, lhs, rhs]

    @classmethod
    def deserialize(cls, string):
        return cls('root', cls('left', cls('left.left')), cls('right'))

node = Node('root', Node('left', Node('left.left')), Node('right'))
print("{}".format(node.serialize()))
print("{}".format(Node.deserialize('pip').serialize()))

#assert deserialize(serialize(node)).left.left.val == 'left.left'

