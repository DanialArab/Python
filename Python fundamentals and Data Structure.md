# Python Fundamentals and Data Structure

Here is the summary of my notes from the following courses:

+ <a href="https://codewithmosh.com/p/python-programming-course-beginners">Complete Python Mastery</a>
+ <a href="https://www.udemy.com/course/data-structures-algorithms-python/">Python Data Structures & Algorithms + LEETCODE Exercises</a>

1. [Data Structures & Algorithms](#1)
    1. [Data Structures: Stacks](#2)
    2. [Data Structures: Trees ](#3)
       1. [Binary search tree (BST)](#4)
    3. [Algorithms](#5)
       1. [Algorithms: Tree Traversal]
           1. [Breadth First Search (BFS)]()
           2. [Depth First Search]()
               1. [PreOrder]
               2. [PostOrder]
               3. [InOrder]


<a name="1"></a>
### Introduction 

<a name="2"></a>
#### What is a Database? 


### References: 
+ Fundamentals --> Back-end Development –->  (Mosh Coding School - Mosh Hamedani)
+ Data Structures & Algorithms – Python (Udemy course by Scott Barrett)

## Data Structures & Algorithms 

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
