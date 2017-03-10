
# coding: utf-8

# In[4]:

# Problem-1 Give an algorithm for finding maximum element in binary tree (not binary search tree)
# The problem is similar to finding the height of a binary tree (the same algorithm that
# is there for binary search tree in ./BinaryTree.ipynb)

class Node(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
    def get_data(self):
        return self.data
    def set_data(self, new_data):
        self.data = new_data
    def get_left(self):
        return self.left
    def set_left(self, new_left):
        self.left = new_left
    def get_right(self):
        return self.right
    def set_right(self, new_right):
        self.right = new_right
class BinaryTree(object):
    def __init__(self):
        self.root = None
    def get_root(self):
        return self.root
    def insert_random_location(self, node):
        if self.root == None:
            self.root = node
        else:
            curr = self.root
            pred = None
            import random
            while curr != None:
                pred = curr
                if random.random() > 0.5:
                    curr = curr.get_right()
                else:
                    curr = curr.get_left()
            assert curr == None
            if pred.get_left() == None:
                pred.set_left(node)
            else:
                pred.set_right(node)
    def display_postorder(self):
        curr = self.root
        visited = set()
        stack = list()
        # curr gets visited for the first time means curr gets touched
        # if curr has a left NOT in visited, then visit left
        # if curr has right NOT in visited, then visit right
        # if curr has no left and no right, then print curr and add curr to visited
        # unstack and check if left is visited, if left is not visited, then visit left
        while curr != None or len(stack) > 0:
            stack.append(curr)
            left = curr.get_left()
            right = curr.get_right()
            #Base condition: leaf node or a node with both children visited
            if ((left == None) or left in visited) and ((right == None) or right in visited):
                visited.add(curr)
                print curr.get_data()
                if len(stack) > 1:
                    stack.pop()
                    curr = stack.pop()
                    continue
                else:
                    return
            if (left != None) and (left not in visited):
                curr = left
            if (right != None) and (right not in visited):
                curr = right
    def display(self):
        # display inorder
        curr = self.root
        stack = list()
        while curr or len(stack)>0:
            # append the node being visited
            while curr != None:
                stack.append(curr)
                curr = curr.get_left()
            if len(stack) > 0:
                curr = stack.pop()
                print curr.get_data()
                curr = curr.get_right()
    # height of an empty tree is -1, height of a tree with just one node is 0
    # height ::= number of edges connecting the root with the deepest leaf
    def height(self, root):
        if root == None:
            return -1
        else:
            return 1 + max(self.height(root.get_left()), self.height(root.get_right()))
#     def graphical_display(self):
#         import matplotlib.pyplot as plt
#         %matplotlib inline
#         plt.axis('off')
#         fig, ax = plt.subplots()
#         plt.axis([0, 100, 0, 100])
#         curr = self.root
#         x = 50
#         y = 90
#         display_data = list()
#         stack = list()
#         while curr or len(stack)>0:
#             while curr:
#                 display_data.append((x, y, curr.get_data()))
#                 stack.append(curr)
#                 curr = curr.get_left()
#                 x = x - 5
#                 y = y - 5
#             if len(stack)>0:
#                 curr = stack.pop()
#                 x = x + 5
#                 y = y - 5
#                 X, Y, data = display_data.pop()
#                 ax.add_artist(plt.Circle((X, Y), 1))
#                 ax.text(X, Y, str(data))
#                 curr = curr.get_right()
    def graphical_display(self):
        import matplotlib.pyplot as plt
        from matplotlib.lines import Line2D
        get_ipython().magic(u'matplotlib inline')
        plt.axis('off')
        fig, ax = plt.subplots()
        plt.axis([0, 100, 0, 100])
        curr = self.root
        x = 50
        y = 90
        display_data = list()
        stack = list()
        while curr or len(stack)>0:
            while curr:
                display_data.append((x, y, curr.get_data()))
                stack.append(curr)
                curr = curr.get_left()
                x = x - 5
                y = y - 5
            if len(stack)>0:
                curr = stack.pop()
                x_, y_, data = display_data.pop()
                plt.axis('off')
                ax.add_artist(plt.Circle((x_, y_), 1))
                ax.text(x_, y_, str(data))
                curr = curr.get_right()
                y = y_ - 5
                x = x_ + 5


# In[1]:

#bt.display_postorder()


# In[2]:

#bt.height(bt.get_root())


# In[3]:

#bt.display()

