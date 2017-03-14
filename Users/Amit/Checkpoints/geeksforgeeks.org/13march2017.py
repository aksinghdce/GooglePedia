
# coding: utf-8

# [Rearrange characters in a string such that no two adjacent are same](http://www.geeksforgeeks.org/rearrange-characters-string-no-two-adjacent/)

# In[29]:

def adj_chars_not_same(inpt):
    st = list(inpt)
    q = 0
    p = q - 1
    while q < len(st) and p < len(st):
        p += 1
        q += 1
        while q < len(st) and st[p] == st[q]:
            q += 1
        if q < len(st):
            p += 1
            st[p], st[q] = st[q], st[p]
            q = p + 1
        else:
            break
    if p == q - 1:
        return "".join(st)
    else:
        return "Not Possible"


# In[30]:

adj_chars_not_same("aaabc")


# In[31]:

adj_chars_not_same("aa")


# In[32]:

adj_chars_not_same("aaabb")


# In[33]:

adj_chars_not_same("aaaabc")

