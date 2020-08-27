"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from stack.stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right is None:
                new_node = BSTNode(value)
                self.right = new_node

            else:
                self.right.insert(value)

        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)

            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if self.value > target:
            if self.left is None:
                return False
        else:
            if self.right is None:
                return False
            found = self.right.contains(target)
            return found

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

        # iterate get_max()
        # start at the root(self)
        # keep going right until you can't anymore
        # --> stop when cur_node.right is None
        cur_node = self
        while cur_node.right is not None:
            cur_node = cur_node.right
            return cur_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Start at the root
        # fn(self.value)
        fn(self.value)

        # If self.left is not None:
        if self.left is not None:
            # Go left
            self.left.for_each(fn)
        # If self.right is not None:
        if self.right is not None:
            # Go right
            self.right.for_each(fn)

    def for_each_iterative(self, fn):
        # Depth first traversal iterative
        # Start at the root
        cur_node = self

        stack = Stack()
        stack.push(cur_node)
        # While the stack is not empty:
        while len(stack) > 0:
            cur_node = stack.pop()
            # Push right
            if cur_node.right is not None:
                stack.push(cur_node.right)
            # Push left
            if cur_node.left is not None:
                stack.push(cur_node.left)
            # Do the thing with the current node
            fn(cur_node.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        pass

    # BFT
    # Start at the root
    # Push it onto the queue
    # While the queue is not empty:
    # -Cur_node = Remove from the queue
    # -Add cur_node children to the queue
    # Process cur_node

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.bft_print()
# bst.dft_print()
#
# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()



