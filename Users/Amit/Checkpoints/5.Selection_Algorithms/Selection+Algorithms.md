
# Selection Algorithms

### [QuickSelect](https://en.wikipedia.org/wiki/Quickselect)

- Wikipedia Says:
    1. In computer science, quickselect is a selection algorithm to find the kth smallest element in an unordered list. It is related to the quicksort sorting algorithm.

## Let's understand QuickSort

### Divide and Conquer Idea: 

#### Divide: 
    The idea is to find a pivot. The pivot is an index q in the array A[p:r], such that all elements of A[p:q-1] are less than or equal to A[q], which is less than or equal to elements of A[q+1:r].
    
    A[p:q-1] and/or A[q+1:r] are/is possibly empty.

#### Conquer:
    Sort the array A[p:r] by recursive calls to Divide
    
#### Combine
    Merge the sorted arrays A[p:q-1] and A[q+1:r]. Because the sub arrays are sorted, the whole array is already sorted. Conbine is basically not reqired.

### Let's write the Partition Function

Algorithm for partition:

1. input to the algorithm: Array, p = start index, r= end index
    1. Initialize i = p - 1 : i is the index that tells that elements from p to i (inclusive) are smaller than Array[r]
2. Traverse the array: j=0 to j < r
    if Array[j] is smaller than or equal to Array[r]:
    then, move Array[j] to Array[i+1] and update i to i+1: Now till i everything is smaller than Array[r]
    also increment j to make it ready for the next iteration and look at a brand new element in the Array that is smaller in index than r.
    Repeat this step for new j
3. Loop has ended: j must be equal to r now
    Now i+1 is the first element that is greater than or equal to Array[r]
    swap (i+1)th position and rth position:
    At this stage, till i everything is smaller than Array[r]
    return i+1: i+1 is the pivot.


```python
def partition(array, p,r):
    print "**********Working within p:" + str(p) + " and r:" + str(r)
    # initialize data for entering the loop
    i = p - 1
    x = 0
    if r < len(array):
        x = array[r] 
    j = p
    while j < r:
        if array[j] <= x:
            i = i + 1
            print "Swap intermediate i:" + str(i) + " and j:" + str(j)
            array[i], array[j] = array[j], array[i]
            j = j + 1
        else:
            j = j + 1
    # here j = r - 1
    # verify by print array[j] == array[r-1]
    # hence, increment j
    print "Swap (i + 1):" + str(i+1) + " and j:" + str(j)
    if i < j:
        array[i+1], array[j] = array[j], array[i+1]
    return i+1

def quicksort(A, p , r):
    if p < r:
        q = partition(A, p, r)
        print A[p:q], A[q], A[q+1:r]
        quicksort(A, 0, q-1)
        quicksort(A, q+1, r)
    else:
        return
    
```


```python
A = [6, 0, 5, 13, 13, 2, 1, 2]
quicksort(A, 0, len(A) - 1)
```

    **********Working within p:0 and r:7
    Swap intermediate i:0 and j:1
    Swap intermediate i:1 and j:5
    Swap intermediate i:2 and j:6
    Swap (i + 1):3 and j:7
    [0, 2, 1] 2 [13, 6, 5]
    **********Working within p:0 and r:2
    Swap intermediate i:0 and j:0
    Swap (i + 1):1 and j:2
    [0] 1 []
    **********Working within p:4 and r:7
    Swap intermediate i:4 and j:4
    Swap intermediate i:5 and j:5
    Swap intermediate i:6 and j:6
    Swap (i + 1):7 and j:7
    [13, 6, 5] 13 []
    **********Working within p:0 and r:6
    Swap intermediate i:0 and j:0
    Swap intermediate i:1 and j:1
    Swap intermediate i:2 and j:2
    Swap intermediate i:3 and j:3
    Swap (i + 1):4 and j:6
    [0, 1, 2, 2] 5 [6]
    **********Working within p:0 and r:3
    Swap intermediate i:0 and j:0
    Swap intermediate i:1 and j:1
    Swap intermediate i:2 and j:2
    Swap (i + 1):3 and j:3
    [0, 1, 2] 2 []
    **********Working within p:0 and r:2
    Swap intermediate i:0 and j:0
    Swap intermediate i:1 and j:1
    Swap (i + 1):2 and j:2
    [0, 1] 2 []
    **********Working within p:0 and r:1
    Swap intermediate i:0 and j:0
    Swap (i + 1):1 and j:1
    [0] 1 []
    **********Working within p:5 and r:6
    Swap intermediate i:5 and j:5
    Swap (i + 1):6 and j:6
    [6] 13 []
    **********Working within p:0 and r:5
    Swap intermediate i:0 and j:0
    Swap intermediate i:1 and j:1
    Swap intermediate i:2 and j:2
    Swap intermediate i:3 and j:3
    Swap intermediate i:4 and j:4
    Swap (i + 1):5 and j:5
    [0, 1, 2, 2, 5] 6 []
    **********Working within p:0 and r:4
    Swap intermediate i:0 and j:0
    Swap intermediate i:1 and j:1
    Swap intermediate i:2 and j:2
    Swap intermediate i:3 and j:3
    Swap (i + 1):4 and j:4
    [0, 1, 2, 2] 5 []
    **********Working within p:0 and r:3
    Swap intermediate i:0 and j:0
    Swap intermediate i:1 and j:1
    Swap intermediate i:2 and j:2
    Swap (i + 1):3 and j:3
    [0, 1, 2] 2 []
    **********Working within p:0 and r:2
    Swap intermediate i:0 and j:0
    Swap intermediate i:1 and j:1
    Swap (i + 1):2 and j:2
    [0, 1] 2 []
    **********Working within p:0 and r:1
    Swap intermediate i:0 and j:0
    Swap (i + 1):1 and j:1
    [0] 1 []



```python
A
```




    [0, 1, 2, 2, 5, 6, 13, 13]


