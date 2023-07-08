# Python Fundamentals and Data Structure

Here is the summary of my notes from the following courses:

+ <a href="https://codewithmosh.com/p/python-programming-course-beginners">Complete Python Mastery</a>
+ <a href="https://www.udemy.com/course/data-structures-algorithms-python/">Python Data Structures & Algorithms + LEETCODE Exercises</a>

1. [Data Structures & Algorithms](#1)
    1. [Time and Space Complexities ](#2)
       1. [Overview](#3)
       2. [Big O: Intro ](#4)
           1. [Time complexity](#5)
           2. [Space complexity](#6)
       3. [Terminologies](#7)
           1. [Omega](#8)
           2. [Theta](#9)
           3. [Omicron](#10)
       4. [Big O](#11)
           1. [Big O: O(n) (or proportional)](#12)
           2. [Big O: Drop Constants](#13)
           3. [Big O: O (n ^2)](#14)
           4. [Big O: Drop Non-Dominants](#15)
           5. [Big O: O(1) (or constant)](#16)
           6. [Big O: O(log n)](#17)
           7. [Big O: Different Terms for Inputs](#18)
           8. [Big O: Lists](#19)
           9. [Big O: Wrap Up](#20)
    2. [Pointers](#21)
    3. [Data Structures](#22)
        1. [Singly Linked List](#23)
           1. [Intro](#24)
           2. [Big O](#25)
           3. [Implementation](#26)
        2. [Doubly Linked List](#27)
        3. [Stacks](#)
        4. [Queues]()
        5. [Trees ](#3)
            . [Binary search tree (BST)](#4)
                [Algorithms: Tree Traversal]
       . [Breadth First Search (BFS)]()
       . [Depth First Search]()
           1. [PreOrder]
           2. [PostOrder]
           3. [InOrder]
        6. [Hash Table](#5)
        7. [Graphs]()
   4. [Algorithms](#)
       1. [Recursion](#)
          1. [Intro](#)
          2. [Call stack](#)
          3. [Factorial](#)
       3. [Basic Sorts]
       4. [Tree Traversal]
 


<a name="1"></a>
## Data Structures & Algorithms 

<a name="2"></a>
### Time and Space Complexities 

<a name="3"></a>
#### Overview

You may get asked in the interview that what would be the best data structure or algorithm for this situation? What data structure or algorithm you would use for a particular question like when the list is the best solution or when a linked list is the best one? In these cases what you are really asked about is on understanding Big O? 

<a name="4"></a>
#### Big O: Intro 

It is a huge topic when it comes to data structures and algos. It is a way of comparing, mathematically like how efficient they are compared to each other, two sets of code. 

<a name="5"></a>
##### Time complexity

It is not measured in time b/c otherwise it would be machine dependent. So it is measured in the number of operations needed to complete something. 

<a name="6"></a>
##### Space complexity 

It is about how much running a code takes memory, an indicator of memory usage. It should be traded off with time complexity meaning we have to consider both time and space complexities when comparing two sets of codes. For most of the parts in this course we are concerned about time complexities. 

<a name="7"></a>
#### Terminologies 

When dealing with time and space complexities we deal with Omega, Theta, and Omicron. 

<a name="8"></a>
##### Omega

The best-case scenario 

<a name="9"></a>
##### Theta

The average case scenario. 

<a name="10"></a>
##### Omicron

The worst-case scenario. 

When we are talking about big O we always talk about the worst case. 

<a name="11"></a>
#### Big O 

![](https://github.com/DanialArab/images/blob/main/Python/Big%20O.png)

Reference: <a href="https://www.bigocheatsheet.com/">Big O Cheat Sheet</a>

<a name="12"></a>
##### Big O: O(n) (or proportional) 

It is also called proportional b/c there is a **linear relationship between the number of operations with the input size n**. There is n number of operations/runs when we pass in number n.  Like:

        def print_function(n):
            for i in range(n):
                print(i)

        print_function(10)

        0
        1
        2
        3
        4
        5
        6
        7
        8
        9

<a name="13"></a>
##### Big O: Drop Constants 

There are a few ways through which we can simplify Big O notation. One of them is drop constants. Like:

        def print_function(n):
            for i in range(n):
                print(i)
        
            for j in range(n):
                print(j)
        
        print_function(10)
        output:
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9
        0
        1
        2
        3
        4
        5
        6
        7
        8
        9


The above code ran n + n or 2n times. However, the Big O is simplified from O(2n) to O(n). it does not matter if there was O(100n) we simplify it to O(n). 

<a name="14"></a>
##### Big O: O (n ^2)

The below code runs n * n times or n^2 leading to have O(n^2):

        def print_function(n):
            for i in range(n):
                for j in range(n):
                    print(i, j)
        
        print_function(10)

also the below code runs in n * n * n times, and you might think that our big O is O(n^3), but we simplify it as O(n^2).

        def print_function(n):
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        print(i, j, k)

        print_function(10)

Again, it does not matter if it is O(n^10) or etc. We simplify it as O(n^2), which is less efficient in terms of time complexity compared to O(n). 

<a name="15"></a>
##### Big O: Drop Non-Dominants

We simplify the O(n^2 + n) as O(n^2) in the following code:

        def print_function(n):
            for i in range(n):
                for j in range(n):
                    print(i, j)
        
            for k in range(n):
                print(k)
        
        print_function(10)

<a name="16"></a>
##### Big O: O(1) (or constant)

O(1) is also called constant time meaning that as n increases the number of operations remains constant. It is the most efficient Big O. so any time you can make it Big O(1) that would be the optimal solution. 

        def add(n):
            return n + n 
        
        print(add(10))

or 

        def add(n):
            return n + n + n
        
        print(add(10))

in the above codes, the number of operations is independent of n like if n is 1 or 1000000 the number of operations is the same and equal to 1. In the first code since we have one operation the big O is O(1), and we also simplify it in the second code as O(1).

<a name="17"></a>
##### Big O: O(log n) 

To find an item in a sorted list we can first cut the list to a half and continue with the half which includes the desired number we continue doing this until finding the number. Let’s say if I have 8 items in my list I need to repeat this three times like 2 to the power of 3 is 8 or log of 2 of 8 (log of 8 with the base of 2) is 3. In this case the number of operations or big O is O(log n). 

This is very efficient/flat as shown in the above graph. These are the ones we see mostly in the course (I mean O(n^2), O(n), O(log n), and O (1)) but in some sorting algorithms we have O (n log n ) we see a couple of those like merge sort and quick sort in this course. O (n log n) is the most efficient that you can make in a sorting algorithm if you want to sort various types of data like string (if you only want to sort some numbers you can get more efficient than that though). 

<a name="18"></a>
##### Big O: Different Terms for Inputs

Big O (a + b) and Big O (a * b) are the Big Os for the following, respectively:

        def print_function(a, b):
            for i in range(a):
                print(i)
        
            for j in range(b):
                print(j)

and also:

        def print_function(a, b):
            for i in range(a):
                for j in range(b):
                    print(i, j) 

<a name="19"></a>
##### Big O: Lists

It is very common to compare the Big O of other data structures against that of list, which is a built-in data structure. Appending and popping, of course, the last item in a list I mean, of an item to/from a list is of O(1) (no reindexing required). However, inserting an item into a list at a particular index or popping an item at a particular index other than the last one requires re-indexing and so we have O(n). One may argue that the big O would be O(1/2 n) if the item is in the middle of the list but there are two issues: one is that the constant ½ can be dropped by the simplification of a drop of constants and the second is that Big O is all about the worst-case scenario, not the average case scenario. also to search an item by value in a list is of O(n), while the searching by an index is of O(1). 

**Takeaway** Adding or removing from the end of a list is of O(1) but adding to or removing from the other end is of O (n). in the middle the big O is also O(n). 

<a name="20"></a>
##### Big O: Wrap Up

Some terminologies:

O(n^2) = loop within a loop

O(n) = proportional 

O(log n) = divide and conquer

O(1) = constant time 

Great site: <a href="https://www.bigocheatsheet.com/">Big O Cheat Sheet</a>

<a name="21"></a>
#### Pointers

Every data structure we create would be through defining classes. 

Integers are **immutable** objects in Python. When num1 = 11 and num2 = num1, the value 11 is assigned to both num1 and num2. Since integers are immutable, when we update num2 to 22, a new memory location is allocated for num2 with the updated value, while num1 remains unchanged with the value 11. But dictionaries are **mutable objects** in Python. When dict2 = dict1, both dict1 and dict2 refer to the same dictionary object. Therefore, when we update the value associated with the key "value" in dict2 to 22, it reflects the same change in dict1 because they are pointing to the same object. This is because dictionaries are mutable, and changes made to one reference of the object will be reflected in all other references.

In summary, when working with immutable objects like integers, assigning one variable to another creates a new copy with the same value. However, with mutable objects like dictionaries and lists, assigning one variable to another creates a new reference to the same object.

<a name="22"></a>
#### Data Structures

<a name="23"></a>
##### Singly Linked List

<a name="24"></a>
###### Intro

+ A linked list does not have an index unlike a list
+ A list is a contiguous place in memory meaning the list’s items are right next to each other in memory (this is why we can access the list’s items through indexing) but in a linked list all the nodes are spread all over the place.
+ In a linked list we have a variable called head which points to the first node, we also have a tail pointing to the last node, each node points to the next node all the way towards the end where the last node points to None. 

<a name="25"></a>
###### Big O

+ Adding a node to the end of a linked list, appending I mean, is of O(1) but removing a node from the end of a linked list is O(n) b/c I need to start from the head node to change the pointer at the tail.
+ Adding a node to the beginning of a linked list is of O(1) and also removing the node from the beginning is of O(1).
+ Adding a node in the middle of a linked list is of O(n) b/c I need to start from the head node to change the pointer, also removing a node from the middle of a linked list is of O(n).
+ Look up in a linked list either through the value or index is of O(n). The following is a good summary:

![](https://github.com/DanialArab/images/blob/main/Python/Linked%20List%20vs.%20List%20Big%20O.png)

<a name="26"></a>
###### Implementation 

        class Node:
            def __init__ (self, value):
                self.value = value
                self.next = None
        
        class Linked_List:
            def __init__(self, value):
                new_node = Node(value)
                self.head = new_node
                self.tail = new_node
                self.length = 1
        
            def print_list(self):
                temp = self.head
                while temp:
                    print (temp.value)
                    temp  = temp.next 
        
            def append(self, value):
                new_node = Node(value)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                self.length += 1
        
            def prepend(self, value):
                new_node = Node(value)
        
                if self.length == 0:
                    self.head = new_node
                    self.tail = new_node
        
                else:
                    new_node.next = self.head
                    self.head = new_node
                self.length += 1
                return True
        
            def pop(self):
                if self.length == 0:
                    return None
                temp = self.head
                pre = self.head 
        
                while temp.next:
                    pre = temp 
                    temp = temp.next 
        
                self.tail = pre 
                self.tail.next = None        
                self.length -= 1
                if self.length == 0:
                    self.head = None
                    self.tail = None 
                
                return temp
        
            def pop_first(self):
                if self.length == 0:
                    return None 
                
                temp = self.head
                self.head = self.head.next 
                temp.next = None
                self.length -= 1
        
                if self.length == 0:
                    self.tail = None
        
                return temp 
        
            def get(self, index):
                if index < 0 or index >= self.length:
                    return None
                
                temp = self.head 
                for _ in range(index):
                    temp = temp.next 
                return temp 
            
            def set_value (self, index, value):
                
                temp = self.get(index)
                if temp:
                    temp.value = value 
                    return True 
                return False 
            
            def insert (self, index, value):
                if index < 0 or index > self.length:
                    return False 
                if index == 0:
                    return self.prepend(value)
                if index == self.length:
                    return self.append(value)
                
                new_node = Node (value)
                temp = self.get(index - 1)
                new_node.next = temp.next 
                temp.next = new_node
                self.length += 1 
                return True 
        
            def remove (self, index):
                if index < 0 or index >= self.length:
                    return None
                if index == 0:
                    return self.pop_first()
                if index == self.length - 1:
                    return self.pop()
                
        
                pre = self.get(index - 1)
                temp = pre.next
                pre.next = temp.next 
                temp.next = None
                self.length -= 1
        
                return temp 
            
            def reverse(self):
        
                temp = self.head
                self.head = self.tail
                self.tail = temp 
        
                after = temp.next 
                before = None
                
                for _ in range(self.length):
                    after = temp.next 
                    temp.next = before
                    before = temp 
                    temp = after 



<a name="27"></a>
##### Doubly Linked List 

HERE


### Data Structures: Stacks 

#### Intro - Stack 

+ LIFO
+ Like a tennis ball can 
+ An example is our browser history like when we visited some websites we can access the last one only and after pushing back button we can access the next one.
+ There are a couple of common ways to implement a stack: one is to use a list (which is the simplest way), we can also use a linked list to implement a stack 
+ For something to be a stack you just have to **add and remove from the same end** so if I use a list there is one end that I want to use for adding and removing. If I want to use a list to implement a stack I want to make sure that I am adding and removing from the end not the beginning to make sure that I have O (1) and not O(n) (which is the case for adding and removing to/from the beginning). 
+ If I want o use a linked list to implement a stack, I want to make sure that the same end to/from which I add or remove is the first node and not the last one (again to have the O(1) rather than O(n)) (adding/removing an item to/from the begging of a linked list is O(1) but adding an item to the end of a linked list is of O(1) while removing an item from the end of a linked list is O(n)). 
+ In stack we have **pop and push** corresponding to pop and prepend 
+ In stack we have top (instead of head) and bottom instead of tail, but since in stack to be implemented through a linked list we are adding or removing from the top we really don’t need to keep track of bottom. 

Constructor 

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class Stack:
        def __init__(self, value):
            new_node = Node(value)
            self.top = new_node
            self.height = 1

        def printer(self):
            temp = self.top
            while temp:
                print(temp.value)
                temp = temp.next

    my_stack = Stack(4)
    my_stack.printer()

output:

    4
Push

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class Stack:
        def __init__(self, value):
            new_node = Node(value)
            self.top = new_node
            self.height = 1

        def push(self, value):
            new_node = Node(value)
            if self.height == 0:
                self.top = new_node
            else:
                new_node.next = self.top
                self.top = new_node
            self.height += 1
            return True

        def printer(self):
            temp = self.top
            while temp:
                print(temp.value)
                temp = temp.next

    my_stack = Stack(2)
    my_stack.push(1)
    my_stack.printer()

output:

    1
    2

Pop 

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    class Stack:
        def __init__(self, value):
            new_node = Node(value)
            self.top = new_node
            self.height = 1

        def push(self, value):
            new_node = Node(value)
            if self.height == 0:
                self.top = new_node
            else:
                new_node.next = self.top
                self.top = new_node
            self.height += 1
            return True

        def pop(self):  # pop is actually pop first b/c in stack implemented by LL i add/remove from the first node
            if self.height == 0:
                return None
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value

        def printer(self):
            temp = self.top
            while temp:
                print(temp.value)
                temp = temp.next

    my_stack = Stack(7)
    my_stack.push(23)
    my_stack.push(3)
    my_stack.push(11)
    my_stack.printer()
    print("\n")
    print(my_stack.pop(), "\n")
    my_stack.printer()

output:

    11
    3
    23
    7

    11 

    3
    23
    7


### Data Structures: Trees 

#### Intro and terminology 

+ We have already seen a tree in this course: linked list. A linked list is a tree that does not fork. 
+ In a binary tree we have left and right values so if each node can only point to two other nodes it is a binary tree
+ But trees don’t have to be a binary tree, in this course we deal with binary trees though 
+ Some terminologies:
    + Full: in a full tree every node either points to ZERO nodes or TWO nodes.
    + Perfect: in a perfect tree any level on the tree that has any nodes is completely filled all the way across 
    + Complete: in a complete tree we are filling the tree from left to right with no gaps 
+ Every node can only have one parent 
+ The child nodes which share a parent node are called siblings 
+ Child nodes can also be parent nodes 
+ A node that does not have any children is called leaf 

#### Binary search tree (BST)

The nodes in a binary tree should be laid out in a particular way to be called a binary search tree: if the value of the nodes to be added to the tree is greater than the parent node it will be positioned on the right and if it is less than that it will be placed in the left. To add a new node we always start the comparison with the node at the very top. 

**If you take any node in a binary search tree all the nodes below it to the right are greater than that node and everything on the left is going to be less than.**


##### BST: Big O 
The total number of nodes in a BST can be calculated with **2^n -1** where n is the level of the tree, we can approximate it with 2^n to get the total number of nodes in a BST. 
The steps we need to take to add/remove a node to/from the desired level in a BST is equal to the level of that node in a tree. This means that all of these have **O(log n)**. Remember this is achieved by **divide and conquer**. In terms of time complexity a perfect tree gives us the best perfect scenario which is measured as Omega. The worst case is that when we have a tree growing like a straight line which never forks (a linked list actually) in this case the time complexity is O(n) so technically a big o of a BST is O(n). So if we assume that we don’t have a worst case possible scenario, i.e., the BST not to be a linked list, we treat it as if the big o is O(log n) and not O(n) data structure. (so in conclusion the big O of a BST is O(n) but if we assume that we can exclude the worst case scenario, which is a linked list, we can treat it as O(log n) data structure). So for the following we treat it as if O(log n):

+ Lookup()
+ Insert()
+ Remove()

Interview question: we need to add data to a data structure very quickly and the retrieval speed is not very important b/c we don’t need to retrieve things very often what we could have is burst of data coming in and we want to make sure nothing is dropped and so the main priority is to add the data as quickly as possible. Would you choose BST or a linked list? 
Re:
Linked list is the best data structure b/c appending to a linked list is O(1), you see you can justify through big O concepts. 

##### BST: Constructor 
We don’t keep track of length in a BST. 

    class Node:
        def __init__ (self, value):
            self.value = value 
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__ (self, value):
            new_node = Node(value)
            self.root = new_node

We don’t have to make the first node at the time of creating the BST, I mean what we have done yet is to create the first node at the same time as creating the data structure like linked list, stack, etc. but we don’t have to it we can alternatively create the first node using insert method like the following where we create an empty tree at the time of running the constructor: 

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

    my_tree = BinarySearchTree()
    print(my_tree.root)

output:

    None

##### BST: Insert -- Intro 

**Just remember we don’t have duplicates in BST.** 

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            new_node = Node(value)
            if self.root is None:
                self.root = new_node
                return True  
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True 
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

    my_tree = BinarySearchTree()
    my_tree.insert(2)
    my_tree.insert(1)
    my_tree.insert(3)
    print((my_tree.root.value))
    print((my_tree.root.left.value))
    print((my_tree.root.right.value))

output:

    2
    1
    3

##### BST: Contains

With contains method we just want to see if a tree contains a particular value. 

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            new_node = Node(value)
            if self.root is None:
                self.root = new_node
                return True
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

        def contains(self, value):
            temp = self.root
            while temp:
                if value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
                else:
                    return True
            return False

    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.contains(27))
    print(my_tree.contains(17))

the output is the same as above.

    True
    False


##### BST: Minimum Value 

This method finds and returns the node with the minimum value in a tree or a subtree. So we write this method like it can be also applied in any subtree. 

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            new_node = Node(value)
            if self.root is None:
                self.root = new_node
                return True
            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

        def contains(self, value):
            temp = self.root
            while temp:
                if value < temp.value:
                    temp = temp.left
                elif value > temp.value:
                    temp = temp.right
                else:
                    return True
            return False

        def min_value_node(slef, current_node):
            while current_node.left:
                current_node = current_node.left
            return current_node.value

    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)

    print(my_tree.min_value_node(my_tree.root))
    print(my_tree.min_value_node(my_tree.root.right))

output:

    18
    52

Quiz:
1-	Adding an item to a Binary Search Tree is O(log n): False: Omega (best case) and Theta (average case) are both (log n). However, worst case is O(n) and Big O measures worst case.
2-	Binary Search Trees always have a better Big O than Linked Lists: False: An insert into a Binary Search Tree is typically (log n). Appending an item onto the end of a Linked List is O(1).


### Algorithms: Tree Traversal 

#### Intro

Tree traversal is when we are going to visit every node in the tree and we want to take the values and put them in a list then will return that list. 
Tree traversal is more complicated compared to doing something like with a linked list b/c in a linked list it is just linear so to traverse it we just start at the beginning and go through the list but with the tree there are multiple ways to visit each node one approach is breadth first search another way is depth first search. We look at different ways of DFS in the followings. 

#### Breadth First Search (BFS)

##### Intro 

We start at the top of the tree then we do the second row and then the third row and so on and so forth. We will create two lists: queue and results, results is the one that will be returned with all the nodes’ values in it. The queue is the one where we include the entire node meaning its value and its left and right. But in the results we are only storing the values and not the entire node. The loop only runs as long as we have items in the queue list like as long as the queue is empty it means that we have visited every item in the tree and the only thing left to do is to return the results list.  

##### Code 

The BFS is a method in our binary search tree we defined previously: 

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            new_node = Node(value)

            if self.root is None:
                self.root = new_node
                return True

            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

        def BFS(self):
            current_node = self.root
            queue = []
            results = []
            queue.append(current_node)

            while len(queue) > 0:
                current_node = queue.pop(0)
                results.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            return results

    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(my_tree.BFS())

output:

    [47, 21, 76, 18, 27, 52, 82]

#### Depth First Search HERE
Breadth First Search (BFS)
There are three types of depth first search: preorder, postorder, and inorder.

##### PreOrder 

###### Intro 

The order by which we add the items to the list is we start at the top then we keep moving to the left until we reach to point which is as far as we can go to the left then we go up and go right until we reach to the point that we looked at everything to the left of the top node then we go to the right and then we go to the left and then right …. 

###### Code 
Again the DFS preorder is a method in our BinarySearchTree class. Inside the method we have a recursive function, we have not seen such a thing before:

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            new_node = Node(value)

            if self.root is None:
                self.root = new_node
                return True

            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

        def BFS(self):
            current_node = self.root
            queue = []
            results = []

            queue.append(current_node)

            while len(queue) > 0:
                current_node = queue.pop(0)
                results.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            return results

        def dfs_pre_order(self):
            results = []

            def traverse(current_node):
                results.append(current_node.value)
                if current_node.left:
                    traverse(current_node.left)
                if current_node.right:
                    traverse(current_node.right)

            traverse(self.root)
            return results

    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(my_tree.dfs_pre_order())

output:

    [47, 21, 18, 27, 76, 52, 82]

##### PostOrder 

###### Intro 

Just like the other tree traversal we start at the top what is different here is that we are just going to visit the self.root node we are not going to write that value to the results list yet, then we are going to go to the left then visit that node and then we go to the left again until there is no node to the left and right only then finally we write the value of the last node, which does not have any left or right, to the results list so the order is that we look left then right if there is nothing on the left and right we write the node’s value to the results list. Then we come back up and go to right … the last node which will be written to the results list is the self.root node. 

###### Code

The method for the dfs_post_order is exactly the same as of dfs_pre_order but we append at the end:

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            new_node = Node(value)

            if self.root is None:
                self.root = new_node
                return True

            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

        def BFS(self):
            current_node = self.root
            queue = []
            results = []

            queue.append(current_node)

            while len(queue) > 0:
                current_node = queue.pop(0)
                results.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            return results

        def dfs_pre_order(self):
            results = []

            def traverse(current_node):
                results.append(current_node.value)
                if current_node.left:
                    traverse(current_node.left)
                if current_node.right:
                    traverse(current_node.right)

            traverse(self.root)
            return results

        def dfs_post_order(self):
            results = []

            def traverse(current_node):
                if current_node.left:
                    traverse(current_node.left)
                if current_node.right:
                    traverse(current_node.right)
                results.append(current_node.value)
            traverse(self.root)
            return results

    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(my_tree.dfs_post_order())

output:

    [18, 27, 21, 52, 82, 76, 47]


##### InOrder 

###### Intro

We start at the top node, we go to the left, then again go to the left until there is nothing to the left then we write that last node to the results list then we go to the right and so on and so forth. In this case we write the lowest value first to the results list then the second lowest value and all the way we add the nodes’ values in numerical order to the results list. 

###### Code

Again here the method is pretty similar to that of preorder and postorder but we append the value after going to the left and before going to the right:

    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    class BinarySearchTree:
        def __init__(self):
            self.root = None

        def insert(self, value):
            new_node = Node(value)

            if self.root is None:
                self.root = new_node
                return True

            temp = self.root
            while True:
                if new_node.value == temp.value:
                    return False
                if new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True
                    temp = temp.right

        def BFS(self):
            current_node = self.root
            queue = []
            results = []

            queue.append(current_node)

            while len(queue) > 0:
                current_node = queue.pop(0)
                results.append(current_node.value)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            return results

        def dfs_pre_order(self):
            results = []

            def traverse(current_node):
                results.append(current_node.value)
                if current_node.left:
                    traverse(current_node.left)
                if current_node.right:
                    traverse(current_node.right)

            traverse(self.root)
            return results

        def dfs_post_order(self):
            results = []

            def traverse(current_node):
                if current_node.left:
                    traverse(current_node.left)
                if current_node.right:
                    traverse(current_node.right)
                results.append(current_node.value)
            traverse(self.root)
            return results

        def dfs_in_order(self):
            results = []

            def traverse(current_node):
                if current_node.left:
                    traverse(current_node.left)
                results.append(current_node.value)
                if current_node.right:
                    traverse(current_node.right)
            traverse(self.root)
            return results

    my_tree = BinarySearchTree()
    my_tree.insert(47)
    my_tree.insert(21)
    my_tree.insert(76)
    my_tree.insert(18)
    my_tree.insert(27)
    my_tree.insert(52)
    my_tree.insert(82)
    print(my_tree.dfs_in_order())

output:

    [18, 21, 27, 47, 52, 76, 82]


<a name=""></a>
##### Recursion

<a name=""></a>
###### Intro 

**Recursion is a function that calls itself until it does not**. The example is opening a gift box through running a gift_box function, which returns either a ball or a smaller gift box and we run the function again … 

Points:

+ The process of opening each new box, in our example, is the same. In a general term, the process of whatever we do with recursion has to be the same 
+ Each time we open a box, we make the problem smaller 
+ You have to have a return in your recursive function to make sure that at some point the recursive function finally does not call itself. 
+ When we open the box and it contains the ball this is what we call our base case this is when we are going to stop opening boxes or the function will stop calling itself, so the base case is when we stop calling the recursive function. This is very important to have the if statement for the base case b/c otherwise the function gets called again and again … which is called stack overflow so I do need to have a base case where this will at some point stop calling itself. 
+ The statement of the base case has to be true at some point to prevent infinite looping through creating a stack overflow. So if you get a stack overflow in a recursive function this is one of the places to go troubleshoot 
+ Also if you have a print statement instead of a return statement, if the condition in the if statement is met there would be a print but b/c there is no return statement to cause us to stop running the code we will end up having a stack overflow. So it is very important o have a return statement in your code. 
+ If the recursive function needs to call itself again, this is called a recursive case

<a name=""></a>
###### Call Stack

We start taking a look at the call stack with the function that is not recursive to make sure we can understand it and then we look at how recursive functions go on the call stack. 

What we learned in the data structure section on stack also applies here. So whatever function is at the top of the call stack is the only one that can run once that function is done running and you remove it then the next function can run and so on and so forth. 

        def funcThree():
            print("Three")
        
        def funcTwo():
            funcThree()
            print("Two")
        
        def funcOne():
            funcTwo()
            print("One")
        
        funcOne()
        
        
        output:
        Three
        Two
        One

<a name=""></a>
###### Factorial 

In any course aimed to teach recursion, the factorial is used. 
Some reminders:

+ In a recursive function, I need to do the same thing over and over
+ The problem needs to be getting smaller
 
Factorial function properly demonstrates these two and so that is why it is used most often to teach recursion. 

        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n-1)
        
        print(factorial(4))
        
        output:
        24





## Zip Function

If we have two lists and we want to combine them as a list of tuples let’s say, here we cannot use map function or list comprehension because they both work with a single list and so here we need built-in zip function, which returns a zip object which is also iterable and can be converted to a list like:

    list1 = [1, 2, 3]
    list2 = [10, 20, 30]

    print(list(zip(list1, list2)))


the output would be:

    [(1, 10), (2, 20), (3, 30)]

Something cool would be:

    list1 = [1, 2, 3]
    list2 = [10, 20, 30]

    print(list(zip("abc", list1, list2)))


the output would be:

    [('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]

## Two Pointers

In programming, "two pointers" refers to a technique where you use two references or indices to traverse or manipulate elements in a data structure. These pointers are typically used to track different positions within the data structure simultaneously.

The concept of two pointers is commonly used in algorithms and data structures, especially when dealing with arrays, linked lists, and strings. By maintaining two pointers, you can perform operations efficiently by iterating or comparing elements in a coordinated manner.

Here are a few common scenarios where two pointers are used:

+ Two-pointer technique: In this technique, you use two pointers that start at different ends of an array or list and move towards each other until they meet or cross paths. This approach is often used to search for pairs or patterns in a sorted or partially sorted array or list. It can help optimize the time complexity by avoiding unnecessary comparisons.

+ Sliding window technique: This technique involves maintaining a window or a subarray within a larger array by using two pointers. The window is defined by the two pointers, and it can be moved or expanded as needed. This technique is useful for solving problems that involve finding subarrays, substring problems, or optimizing algorithms by reducing redundant computations.

+ Fast and slow pointers: In some scenarios, you might need to traverse a linked list or an array at different speeds. You can use a fast pointer that moves faster than a slow pointer to perform operations such as cycle detection, finding middle elements, or partitioning.

These are just a few examples of how two pointers can be used in programming. The technique is versatile and can be adapted to various problem-solving situations to optimize algorithms and improve efficiency.
