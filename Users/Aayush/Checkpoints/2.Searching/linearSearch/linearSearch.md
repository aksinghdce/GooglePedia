
Problem Statement - Linear search for an item in a list.

Pseudo Code - <img src="../images/linearSearchPseudo.jpg">


```python
# Python Program for Linear search
def linearSearch(A, search):
    for item in A:
        if(item == search):
            return True
    return False
```


```python
# Execution
A = [1,2,3,4,5]
search = 4
out = linearSearch(A,search)
print out
```

    True



```python
Asymptotic Analysis :
    
    Time Complexity = O(n)
```
