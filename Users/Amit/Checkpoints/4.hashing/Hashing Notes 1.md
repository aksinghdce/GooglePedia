
# Algorithms and Data Structures: Hashing

## Worst case complexity of hashing is O(n). But, on an average it gives O(1).

Direct Addressing: One unique location for every possible key.

## Load Factor:

Number of items stored in a hash table / size of the table

This tells whether the hash function is distributing the keys evenly in the table or not. How? well, the load factor tells the average size of chains that would be built in the table as a result of chaining. Now, if actual size of a chain corresponding to a certain key goes far beyond the load factor, then we would know that the hash function is not distributing the keys evenly.

## Collision resolution techniques:

1. Separate Chaining
2. Open Addressing or Closed Hashing. Collision resolution technique is called "probing" in this method.
    1. Linear Probing: Rehash : rehash(key) = (n+1)%tablesize. Interval between probes is fixed at 1. Problem of Clustering is seen.
    2. Quadratic Probing: Rehash: **$$rehash(key) = (n+k^2) \bmod(tablesize)$$**. 
    Intervals between probes increases proportionally to the hash value. Problem of secondary clustering is seen.
3. Double Hashing
    1. Interval between probes is computed by another hash function.
    2. h2(key) != 0. h2 != h1


Hashing is useful if the data is static and has unique keys.

If the problem domain needs more search operations than insert operations.

# Bloom Filter

A probabilistic data structure which was designed to check whether an element is present in a set with memory and time efficiency.

It tells whether the element is definitely not there in the set or might be there in the set.
