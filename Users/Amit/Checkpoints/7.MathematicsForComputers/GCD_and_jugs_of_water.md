
# Problem: Find an algorithm that describes the steps to obtain 3 gallons of watter using only two jugs or sizes 21 and 26 gallons each.

[MIT Course on Mathematics for Computing](file:///home/oem/Desktop/Desktop%20Content/books/Computer%20Education/Resources/MIT_Course_6.042j_Mathematics_For_Computers/6-042j-fall-2010/contents/readings/MIT6_042JF10_chap04.pdf)

We need GCD of 21 and 26. If 3 is a multiple of GCD(21, 26) then we can keep filling the 21 gallons jug through 26 gallons jug. We would need to keep emptying the 26 gallons jug each time it's filled up until we are left with just 3 gallons of water in the jug with the capacity of 21 gallons.


```python
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)
```


```python
gcd(26, 21)
```




    1



3 is a multiple of 1 and hence the algorithm will terminate with a valid answer.


```python

```
