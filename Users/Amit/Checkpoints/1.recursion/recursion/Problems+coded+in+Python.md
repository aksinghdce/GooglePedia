
# Modular expression: pow(A,B)%C


```python
def modExpression(A, B, C, mul=1):
    if B == 0:
        if C == 1:
            return 0
        else:
            return 1
    if B == 1:
        print (mul*A)%C
        return (mul*A)%C
    
    # make the multiple simplified
    if mul > C:
        mul = mul%C
        
    modExpression(A, B-1, C, mul*A)
```


```python
x = modExpression(25, 304, 7)
```

    4

