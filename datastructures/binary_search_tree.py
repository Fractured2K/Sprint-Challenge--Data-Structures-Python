# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        """
        Inserts value into tree as a node
        """
        # Compare value to current node value
        if value < self.value:
            # Check to see if node is a leaf
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # Recursively call the next node until a node is inserted
                self.left.insert(value)
        else:
            # Check to see if node is a leaf
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                # Recursively call the next node until a node is inserted
                self.right.insert(value)

    def contains(self, target):
        """
        Checks to see if a node exists in the tree
        """
        # Return true if current nodes value is the target
        if self.value == target:
            return True

        # Compare target with current node
        if target < self.value:
            # Check if the next node exists
            if self.left is None:
                return False

            # Recursively look at the left node
            return self.left.contains(target)
        else:
            # Check if the next node exists
            if self.right is None:
                return False

            # Recursively look at the right node
            return self.right.contains(target)

    def get_max(self):
        """
        Gets the highest value in the tree
        """
        # Check if current node points to a right node
        # If not return the current nodes value
        if self.right is None:
            return self.value

        # Recursively call get max until the furthest right node is reached
        return self.right.get_max()

        # Iterative solution
        # while self.right is not None:
        #     self = self.right

        # return self.value

    def for_each(self, cb):
        # Wrap value in cb
        cb(self.value)

        # Recursively traverse through every node, invoking the cb
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Hint:  Use a recursive, depth first traversal
    # Print all the values in order from low to high
    def in_order_print(self, node):
        """
        Using the In order traversal method to print all nodes in order
        """
        # Recursively call left node
        if self.left:
            self.left.in_order_print(node)

        # print node on stack unwind
        print(self.value)

        # Recursively call right node
        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Instantiate queue
        queue = Queue()
        # Enqueue root node
        queue.enqueue(node)

        # Iterate over tree while queue is not empty
        while queue.len() > 0:
            # Remove last node from queue
            node = queue.dequeue()
            # Print current node value
            print(node.value)

            # Add current nodes left pointer node to queue if it exists
            if node.left is not None:
                queue.enqueue(node.left)

            # Add current nodes right pointer node to queue if it exists
            if node.right is not None:
                queue.enqueue(node.right)

    def dft_print(self, node):
        # Instantiate stack
        stack = Stack()
        # Add node to stack
        stack.push(node)

        # Iterate over tree while the queue is not empty
        while stack.len() > 0:
            # Pop first node out of stack
            node = stack.pop()
            print(node.value)

            # Add current nodes left pointer node to stack if it exists
            if node.left is not None:
                stack.push(node.left)

            # Add current nodes right pointer node to stack if it exists
            if node.right is not None:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
