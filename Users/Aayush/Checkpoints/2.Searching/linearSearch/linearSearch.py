
# coding: utf-8

# Problem Statement - Linear search for an item in a list.

# Pseudo Code - <img src="../images/linearSearchPseudo.jpg">

# In[1]:

# Python Program for Linear search
def linearSearch(A, search):
    for item in A:
        if(item == search):
            return True
    return False


# In[4]:

# Execution
A = [1,2,3,4,5]
search = 4
out = linearSearch(A,search)
print out


# In[ ]:

Asymptotic Analysis :
    
    Time Complexity = O(n)

