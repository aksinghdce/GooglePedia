
# Reverse Linked List


```python
class Node(object):
    # Node of the list
    def __init__(self, int_data):
        self.data = int_data
        self.next = None
    def getData(self):
        return self.data
    def setData(self, int_data):
        self.data = int_data
    def setNext(self, next_):
        self.next = next_
    def getNext(self):
        return self.next
```


```python
class LinkedList(object):
    #head_ is a node
    def __init__(self):
        self.head = None
        self.count = 0
    def setHead(self, node_):
        self.head = node_
        self.count = self.count + 1
    #at_ is the position after this new elements position
    def insert(self, at_, node_):
        if at_ == None:
            return
        if at_ == self.head:
            node_.setNext(at_)
            self.head = node_
            self.count = self.count + 1
        else:
            curr = self.head
            prev = None
            while curr != at_:
                prev = curr
                curr = curr.getNext()
            prev.setNext(node_)
            node_.setNext(curr)
            self.count += 1
    def getHead(self):
        return self.head
    def display(self):
        curr = self.head
        while curr != None:
            print curr.getData(), self.count
            curr = curr.getNext()
    def reverse(self):
        if self.head == None:
            return
        last = self.head
        first = self.head.getNext()
        last.setNext(None)
        next_ = first
        while next_ != None:
            next_ = first.getNext()
            first.setNext(last)
            last = first
            first = next_
        self.head = last
    def reverse_recursive(self, non_reversed_, reversed_=None):
        if non_reversed_ == None:
            self.head = reversed_
            return
        first = non_reversed_
        next_ = first.getNext()
        first.setNext(reversed_)
        reversed_ = first
        first = next_
        self.reverse_recursive(first, reversed_)
        
```


```python
node_ = Node(0)
```


```python
list_ = LinkedList()
```


```python

list_.setHead(node_)
```


```python
node__ = Node(1)
```


```python
list_.insert(list_.getHead(), node__)
```


```python
node___ = Node(2)
```


```python
list_.insert(list_.getHead(), node___)
```


```python
list_.display()
```

    2 3
    1 3
    0 3



```python
list_.reverse()
```


```python
list_.display()
```

    0 3
    1 3
    2 3



```python
list_.reverse_recursive(list_.getHead())
```


```python
list_.display()
```

    2 3
    1 3
    0 3

