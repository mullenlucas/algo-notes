# LinkedList

[Linked Lists for Technical Interviews - Full Course - YouTube](https://www.youtube.com/watch?v=Hj_rA0dhr2I)

#### High level view:

A linked list is a type of data structure. It organizes data across many nodes.

**Node**: a container for some data, visualized as circles where you can put some data inside.

Taking a simple list `[A,B,C,D]`, we can make it a linked-list by linking them together, adressing forward to the next value:

{A} -> {B} -> {C} -> {D}

The term used is saying `A's next is B`

In other terms, it is a bunch of nodes linked together

The last node is named `Tail` and its pointer points to nothing (`null`)

The first node is named `Head` 

`Head [○,○] -> [○,○] -> [○,○] -> [○,○] -> [○,○] Tail`

A linked-list is an ordered data structure, where every node's pointer points to the next node

##### How is the linked-list different from an array?

![](C:\Users\zeals\AppData\Roaming\marktext\images\2023-07-29-17-50-05-image.png)

An array must be stored contiguously in memory, meaning all the elements of the array are going to be stored next to each other in the computer's memory. On the other hand, in a linked list the contiguous values are stored in different spaces of the computer's memory.

Inserting "q" at position 2:

- Array: to make this possible, it would need to first find the value of index 2, move the forward elements one step to the right, and in the index space insert the value "q". By doing this one-by-one, it becomes a very costly operation => `O(n) insertion time`

- Linked list: to do this, it need to create a new node in the linked list. For that, to insert `q` at pointer 2 it needs to modify the pointer to which the "b" (position 1) node points to, and then `q`'s pointer shall point to node `c` (position 2). This way the logical order of nodes is changed. `Insertion has constant O(1) time`

```python
list = [1,2,3,4,10,20,30,40,50]
```

The linked list allows the manipulation of values in the inner indexes of the linked-list. Otherwise, using the `insert()` indexing funciton, it takes order(n) time, otherwise in at the ends it has order(1) time.

The linked-list traverse this limitation because of the structure it is composed of:

### Simple linked-list

`Head [○,○] -> [○,○] -> [○,○] -> [○,○] -> [○,○] Tail`

The simple linked list 
