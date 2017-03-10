
# coding: utf-8

# # LCA for a binary tree:
# 
# ## Definition:
# 
# ### My words:
# 
# The common ancestor of two given nodes that is farthest from the root is called the lowest common ancestor of the two nodes.
# 
# ### Wikipedia:
# 
# Let T be a rooted tree. The lowest common ancestor between two nodes n1 and n2 is defined as the lowest node in T that has both n1 and n2 as descendants (where we allow a node to be a descendant of itself).
# 
# The LCA of n1 and n2 in T is the shared ancestor of n1 and n2 that is located farthest from the root. Computation of lowest common ancestors may be useful, for instance, as part of a procedure for determining the distance between pairs of nodes in a tree: the distance from n1 to n2 can be computed as the distance from the root to n1, plus the distance from the root to n2, minus twice the distance from the root to their lowest common ancestor. 

# # Algorithm:
# 
# Method 1 (By Storing root to n1 and root to n2 paths):
# 
# Following is simple O(n) algorithm to find LCA of n1 and n2.
# 1. Find path from root to n1 and store it in a vector or array.
# 2. Find path from root to n2 and store it in another vector or array.
# 3. Traverse both paths till the values in arrays are same. Return the common element just before the mismatch.

# In[2]:

from BinarySearchTree import TreeNode, BST


# In[3]:

from Binary_Tree import Node, BinaryTree


# In[4]:

# Create the BinaryTree
import random
nodes = [int(random.random() * 100) for _ in xrange(10)]
unique = set()
[unique.add(data) for data in nodes]
nodes = list(unique)


# In[5]:

nodes


# In[6]:

bt = BinaryTree()
for node_data in nodes:
    node = Node()
    node.set_data(node_data)
    bt.insert_random_location(node)


# In[7]:

bt.graphical_display()

