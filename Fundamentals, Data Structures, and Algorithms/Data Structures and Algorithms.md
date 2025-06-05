# Python Data Structures and Algorithms 

1. [Time and Space Complexities ](#1)
   1. [Overview](#2)
   2. [Big O: Intro ](#3)
       1. [Time complexity](#4)
       2. [Space complexity](#5)
   3. [Terminologies](#6)
       1. [Omega](#7)
       2. [Theta](#8)
       3. [Omicron](#9)
   4. [Big O](#10)
       1. [Big O: O(n) (or proportional)](#11)
       2. [Big O: Drop Constants](#12)
       3. [Big O: O (n ^2)](#13)
       4. [Big O: Drop Non-Dominants](#14)
       5. [Big O: O(1) (or constant)](#15)
       6. [Big O: O(log n)](#16)
       7. [Big O: Different Terms for Inputs](#17)
       8. [Big O: Lists](#18)
       9. [Big O: Wrap Up](#19)
2. [Pointers](#20)
3. [Data Structures](#21)
   1. [Singly Linked List](#22)
      1. [Intro](#23)
      2. [Big O](#24)
      3. [Implementation](#25)
   2. [Doubly Linked List](#26)
      1. [Implementation](#27)
   3. [Stacks](#28)
      1. [Intro](#29)
      2. [Implementation](#30)
   4. [Queues](#31)
      1. [Intro](#32)
      2. [Implementation](#33)
   5. [Trees ](#34)
      1. [Intro and terminology](#35)
      2. [Binary search tree (BST)](#36)
          1. [BST: Big O](#37)
          2. [Constructor](#38)
          3. [Insert](#39)
          4. [Contains](#40)
          5. [Minimum value](#41)
   6. [Hash Table](#42)
      1. [Intro ](#43)
      2. [Collisions ](#44)
      3. [Implementation](#45)
      4. [Big O](#46)
      5. [Interview Question](#47)
   7. [Graphs](#48)
        1. [Intro](#49)
        2. [Adjacency Matrix](#50)
        3. [Adjacency List](#51)
        4. [Big O](#52)
        5. [Implementation](#53)
   8. [Heaps](#54)
      1. [Intro](#55)
      2. 
4. [Algorithms](#54)
   1. [Recursion](#55)
      1. [Intro](#56)
      2. [Call stack](#57)
      3. [Factorial](#58)
   2. [Basic Sorts](#59)
      1. [Bubble sort](#60)
         1. [Intro](#61)
         2. [Implementation](#62)
      2. [Selection sort](#63)
         1. [Intro](#64)
         2. [Implementation](#65)
      3.  [Insertion sort](#66)
         1. [Intro](#67)
         2. [Implementation](#68)
         3. [Big O](#69)
   3. [Merge Sort](#70)
      1. [Overview](#71)
      2. [Intro](#72)
      3. [Implementation](#73)
      4. [Merge Sort: Intro](#74)
      5. [Merge Sort: Implementation](#75)
      6. [Bog O](#76)
   4. [Quick Sort](#77)
      1. [Quick Sort: Intro](#78)
      2. [Pivot: Intro](#79)
      3. [Pivot: Implementation](#80)
      4. [Quick Sort: Implementation](#81)
      5. [Big O](#82)
   5. [Tree Traversal](#83)
      1. [Intro](#84)
      2. [Breadth First Search (BFS)](#85)
         1. [Intro](#86)
         2. [Implementation](#87)
      4. [Depth First Search](#88)
         1. [PreOrder](#89)
            1. [Intro](#90)
            2. [Implementation](#91)
         3. [PostOrder](#92)
            1. [Intro](#93)
            2. [Implementation](#94)
         5. [InOrder](#95)
            1. [Intro](#96)
            2. [Implementation](#97)
5. [Reference](#98)
   
<a name="1"></a>
### Time and Space Complexities 

<a name="2"></a>
#### Overview

You may get asked in the interview that what would be the best data structure or algorithm for this situation? What data structure or algorithm you would use for a particular question like when the list is the best solution or when a linked list is the best one? In these cases what you are really asked about is on understanding Big O? 

<a name="3"></a>
#### Big O: Intro 

It is a huge topic when it comes to data structures and algos. It is a way of comparing, mathematically like how efficient they are compared to each other, two sets of code. 

<a name="4"></a>
##### Time complexity

It is not measured in time b/c otherwise it would be machine dependent. So it is measured in the number of operations needed to complete something. 

<a name="5"></a>
##### Space complexity 

It is about how much running a code takes memory, an indicator of memory usage. It should be traded off with time complexity meaning we have to consider both time and space complexities when comparing two sets of codes. For most of the parts in this course we are concerned about time complexities. 

<a name="6"></a>
#### Terminologies 

When dealing with time and space complexities we deal with Omega, Theta, and Omicron. 

<a name="7"></a>
##### Omega

The best-case scenario 

<a name="8"></a>
##### Theta

The average case scenario. 

<a name="9"></a>
##### Omicron

The worst-case scenario. 

When we are talking about big O we always talk about the worst case. 

<a name="10"></a>
#### Big O 

![](https://github.com/DanialArab/images/blob/main/Python/Big%20O.png)

Reference: <a href="https://www.bigocheatsheet.com/">Big O Cheat Sheet</a>

<a name="11"></a>
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

<a name="12"></a>
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

<a name="13"></a>
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

<a name="14"></a>
##### Big O: Drop Non-Dominants

We simplify the O(n^2 + n) as O(n^2) in the following code:

        def print_function(n):
            for i in range(n):
                for j in range(n):
                    print(i, j)
        
            for k in range(n):
                print(k)
        
        print_function(10)

<a name="15"></a>
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

<a name="16"></a>
##### Big O: O(log n) 

To find an item in a sorted list we can first cut the list to a half and continue with the half which includes the desired number we continue doing this until finding the number. Let’s say if I have 8 items in my list I need to repeat this three times like 2 to the power of 3 is 8 or log of 2 of 8 (log of 8 with the base of 2) is 3. In this case the number of operations or big O is O(log n). 

This is very efficient/flat as shown in the above graph. These are the ones we see mostly in the course (I mean O(n^2), O(n), O(log n), and O (1)) but in some sorting algorithms we have O (n log n ) we see a couple of those like merge sort and quick sort in this course. O (n log n) is the most efficient that you can make in a sorting algorithm if you want to sort various types of data like string (if you only want to sort some numbers you can get more efficient than that though). 

<a name="17"></a>
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

<a name="18"></a>
##### Big O: Lists

It is very common to compare the Big O of other data structures against that of a list, which is a built-in data structure. Appending and popping, of course, the last item in a list I mean, of an item to/from a list is of O(1) (no reindexing required). However, inserting an item into a list at a particular index or popping an item at a particular index other than the last one requires re-indexing and so we have O(n) (n is the number of items in the list). One may argue that the big O would be O(1/2 n) if the item is in the middle of the list but there are two issues: one is that the constant ½ can be dropped by the simplification of a drop of constants and the second is that Big O is all about the worst-case scenario, not the average case scenario. also to search an item by value in a list is of O(n), while the searching by an index is of O(1). 

**Takeaway** Adding or removing from the end of a list is of O(1) but adding to or removing from the other end is of O (n). in the middle the big O is also O(n). 

<a name="19"></a>
##### Big O: Wrap Up

Some terminologies:

O(n^2) = loop within a loop

O(n) = proportional 

O(log n) = divide and conquer

O(1) = constant time 

Great site: <a href="https://www.bigocheatsheet.com/">Big O Cheat Sheet</a>

<a name="20"></a>
#### Pointers

Every data structure we create would be through defining classes. 

Integers are **immutable** objects in Python. When num1 = 11 and num2 = num1, the value 11 is assigned to both num1 and num2. Since integers are immutable, when we update num2 to 22, a new memory location is allocated for num2 with the updated value, while num1 remains unchanged with the value 11. 

      num1 = 1
      num2 = num1
      
      print (f"num1: {num1}")
      print (f"num2: {num2}")
      print (f"num1 points to: {id(num1)}")
      print (f"num2 points to: {id(num2)}")
      num2 = 22
      print (f"num2: {num2}")
      print (f"num1 points to: {id(num1)}")
      print (f"num2 points to: {id(num2)}")

which returns:

      num1: 1
      num2: 1
      num1 points to: 140730016437032
      num2 points to: 140730016437032
      num2: 22
      num1 points to: 140730016437032
      num2 points to: 140730016437704

But dictionaries are **mutable objects** in Python. When dict2 = dict1, both dict1 and dict2 refer to the same dictionary object. Therefore, when we update the value associated with the key "value" in dict2 to 22, it reflects the same change in dict1 because they are pointing to the same object. This is because dictionaries are mutable, and changes made to one reference of the object will be reflected in all other references.

      dic1 = {}
      dic1['value'] = 1
      print (f'dic1: {dic1}')
      
      dic2 = {}
      dic2 = dic1
      print (f'dic2: {dic2}')
      
      print (f"dic1 points to : {id(dic1)}")
      print (f"dic2 points to : {id(dic2)}")
      
      dic2['value'] = 3
      
      print (f'dic1: {dic1}')
      
      print (f'dic2: {dic2}')
      
      print (f"dic1 points to : {id(dic1)}")
      print (f"dic2 points to : {id(dic2)}")

which returns:

      dic1: {'value': 1}
      dic2: {'value': 1}
      dic1 points to : 2828749573440
      dic2 points to : 2828749573440
      dic1: {'value': 3}
      dic2: {'value': 3}
      dic1 points to : 2828749573440
      dic2 points to : 2828749573440

In summary, when working with immutable objects like integers, assigning one variable to another creates a new copy with the same value. However, with mutable objects like dictionaries and lists, assigning one variable to another creates a new reference to the same object.

<a name="21"></a>
#### Data Structures

<a name="22"></a>
##### Singly Linked List

<a name="23"></a>
###### Intro

+ A linked list does not have an index unlike a list
+ A list is a contiguous place in memory meaning the list’s items are right next to each other in memory (this is why we can access the list’s items through indexing) but in a linked list all the nodes are spread all over the place.
+ In a linked list we have a variable called head which points to the first node, we also have a tail pointing to the last node, each node points to the next node all the way towards the end where the last node points to None. 

<a name="24"></a>
###### Big O

+ Adding a node to the end of a linked list, appending I mean, is of O(1) but removing a node from the end of a linked list is O(n) b/c I need to start from the head node to change the pointer at the tail.
+ Adding a node to the beginning of a linked list is of O(1) and also removing the node from the beginning is of O(1).
+ Adding a node in the middle of a linked list is of O(n) b/c I need to start from the head node to change the pointer, also removing a node from the middle of a linked list is of O(n).
+ Look up in a linked list either through the value or index is of O(n). The following is a good summary:

![](https://github.com/DanialArab/images/blob/main/Python/Linked%20List%20vs.%20List%20Big%20O.png)

<a name="25"></a>
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



<a name="26"></a>
##### Doubly Linked List 

<a name="27"></a>
###### Implementation 

      class Node:
          def __init__(self, value):
              self.value = value
              self.next = None
              self.prev = None
      
      class DoublyLinkedList:
          def __init__(self, value):
              new_node = Node(value)
              self.head = new_node
              self.tail = new_node
              self.length = 1
      
          def append(self, value):
              new_node = Node(value)
              if self.head is None:
                  self.head = new_node
                  self.tail = new_node
              else:
                  self.tail.next = new_node
                  new_node.prev = self.tail
                  self.tail = new_node
              self.length += 1
              return True
      
          def pop(self):
              if self.length == 0:
                  return None
              temp = self.tail
              if self.length == 1:
                  self.head = None
                  self.tail = None
              else:
                  self.teil = self.tail.prev
                  self.tail.next = None
                  temp.prev = None
              self.length -= 1
              return temp
      
          def prepend(self, value):
              new_node = Node(value)
              if self.length == 0:
                  self.head = new_node
                  self.tail = new_node
              else:
                  new_node.next = self.head
                  self.head.prev = new_node
                  self.head = new_node
      
              self.length += 1
              return True
      
          def pop_first(self):
              if self.length == 0:
                  return None
              temp = self.head
              if self.length == 1:
                  self.head = None
                  self.tail = None
              else:
                  self.head = self.head.next
                  self.head.prev = None
                  temp.next = None
              self.length -= 1
              return temp.value
      
          def get(self, index):
              if index < 0 or index >= self.length:
                  return None
              temp = self.head
              if index < self.length/2:
                  for _ in range(index):
                      temp = temp.next
              else:
                  temp = self.tail
                  for _ in range(self.length - 1, index, -1):
                      temp = temp.prev
              return temp
      
          def set_value(self, index, value):
              temp = self.get(index)
              if temp:
                  temp.value = value
                  return True
              return False
      
          def insert(self, index, value):
              if index < 0 or index > self.length:
                  return False
              if index == 0:
                  return self.prepend(value)
      
              if index == self.length:
                  return self.append(value)
      
              new_node = Node(value)
              before = self.get(index-1)
              after = before.next
      
              before.next = new_node
              after.prev = new_node
              new_node.prev = before
              new_node.next = after
      
              self.length += 1
              return True
      
          def remove(self, index):
              if index < 0 or index >= self.length:
                  return None
              if index == 0:
                  return self.pop_first()
              if index == self.length - 1:
                  return self.pop()
              temp = self.get(index)
      
              before = temp.prev
              after = temp.next
      
              before.next = after
              temp.next = None
              after.prev = before
              temp.prev = None
              self.length -= 1
              return temp.value
      
          def printer(self):
              temp = self.head
              while temp:
                  print(temp.value)
                  temp = temp.next
      
      my_DLL = DoublyLinkedList(0)
      my_DLL.append(1)
      my_DLL.append(2)
      my_DLL.printer()
      print("\n")
      print(my_DLL.remove(1))
      print("\n")
      my_DLL.printer()
      
      output:
      0
      1
      2
      
      1
      
      0
      2

<a name="28"></a>
##### Stacks 

<a name="29"></a>
###### Intro  

+ LIFO
+ Like a tennis ball can 
+ An example is our browser history like when we visited some websites we can access the last one only and after pushing back button we can access the next one.
+ There are a couple of common ways to implement a stack: one is to use a list (which is the simplest way), we can also use a linked list to implement a stack 
+ For something to be a stack you just have to **add and remove from the same end** so if I use a list there is one end that I want to use for adding and removing. If I want to use a list to implement a stack I want to make sure that I am adding and removing from the end not the beginning to make sure that I have O (1) and not O(n) (which is the case for adding and removing to/from the beginning). 
+ If I want o use a linked list to implement a stack, I want to make sure that the same end to/from which I add or remove is the first node and not the last one (again to have the O(1) rather than O(n)) (adding/removing an item to/from the begging of a linked list is O(1) but adding an item to the end of a linked list is of O(1) while removing an item from the end of a linked list is O(n)). 
+ In stack we have **pop and push** corresponding to pop and prepend 
+ In stack we have top (instead of head) and bottom instead of tail, but since in stack to be implemented through a linked list we are adding or removing from the top we really don’t need to keep track of bottom. 

<a name="30"></a>
###### Implementation  

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


<a name="31"></a>
##### Queues

<a name="32"></a>
###### Intro  

+ FIFO
+ We have the terms enqueue  and dequeue to add and remove from the queue respectively
+ We can use list and linked list to implement a queue. Queue is FIFO so for something to be a queue we add on one end and remove from the other end so if we want to use a list to implement a queue we have O(1) on one end and O(n) on the other end (b/c we have O(1) for adding or removing from the end of a list and O(n) for adding or removing from the beginning of a list).
+ If we use a linked list to implement a queue: we have O(1) for adding to the end of a linked list and O(1) for removing from the beginning of a linked list so I do NOT want to dequeue from the end of a linked list. So I want to enqueue to the end of a linked list and dequeue from the beginning of a linked list to make sure that we have O(1) for both adding and removing an item to/from a queue.
+ In queue we keep track of both head and tail, which are called first and last here. 

<a name="33"></a>
###### Implementation  

      class Node:
          def __init__(self, value):
              self.value = value
              self.next = None
      
      class Queue:
          def __init__(self, value):
              new_node = Node(value)
              self.first = new_node
              self.last = new_node
              self.length = 1
      
          def enqueue(self, value):
              new_node = Node(value)
              if self.length == 0:
                  self.first = new_node
                  self.last = new_node
              else:
                  self.last.next = new_node
                  self.last = new_node
              self.length += 1
      
          def dequeue(self):
              if self.length == 0:
                  return None
              temp = self.first
              if self.length == 1:
                  self.first = None
                  self.last = None
              else:
                  self.first = self.first.next
                  temp.next = None
              self.length -= 1
              return temp.value
      
          def printer(self):
              temp = self.first
              while temp:
                  print(temp.value)
                  temp = temp.next
      
      my_q = Queue(1)
      my_q.enqueue(2)
      my_q.enqueue(3)
      print(my_q.dequeue())
      print(my_q.dequeue())
      print(my_q.dequeue())
      print(my_q.dequeue())
      
      
      output:
      1
      2
      3
      None


<a name="34"></a>
##### Trees

<a name="35"></a>
###### Intro and terminology 

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


![](https://github.com/DanialArab/images/blob/main/Python/BT_types.png)

reference: https://medium.com/data-science/5-types-of-binary-tree-with-cool-illustrations-9b335c430254

<a name="36"></a>
###### Binary search tree (BST)

The nodes in a binary tree should be laid out in a particular way to be called a binary search tree: if the value of the nodes to be added to the tree is greater than the parent node it will be positioned on the right and if it is less than that it will be placed in the left. To add a new node we always start the comparison with the node at the very top. 

**If you take any node in a binary search tree all the nodes below it to the right are greater than that node and everything on the left is going to be less than.**

<a name="37"></a>
###### BST: Big O 
The total number of nodes in a BST can be calculated with **(2^n) -1** where n is the level of the tree, we can approximate it with 2^n to get the total number of nodes in a BST. 
The steps we need to take to add/remove a node to/from the desired level in a BST is equal to the level of that node in a tree. This means that all of these have **O(log n)**. Remember this is achieved by **divide and conquer**. In terms of time complexity a perfect tree gives us the best perfect scenario which is measured as Omega. The worst case is that when we have a tree growing like a straight line which never forks (a linked list actually) in this case the time complexity is O(n) so technically a big o of a BST is O(n). So if we assume that we don’t have a worst case possible scenario, i.e., the BST not to be a linked list, we treat it as if the big o is O(log n) and not O(n) data structure. (so in conclusion the big O of a BST is O(n) but if we assume that we can exclude the worst case scenario, which is a linked list, we can treat it as O(log n) data structure). So for the following we treat it as if O(log n):

+ Lookup()
+ Insert()
+ Remove()

Interview question: we need to add data to a data structure very quickly and the retrieval speed is not very important b/c we don’t need to retrieve things very often what we could have is burst of data coming in and we want to make sure nothing is dropped and so the main priority is to add the data as quickly as possible. Would you choose BST or a linked list? 
Re:
Linked list is the best data structure b/c appending to a linked list is O(1), you see you can justify through big O concepts. 

<a name="38"></a>
###### BST: Constructor 
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

<a name="39"></a>
###### BST: Insert 

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

<a name="40"></a>
###### BST: Contains

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

<a name="41"></a>
###### BST: Minimum Value 

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

<a name="42"></a>
##### Hash Table

<a name="43"></a>
###### Intro 

+ Dictionaries are the built-in hash tables. 
+ The way that hash tables work is like we have a hash function/method which performs a hash on the key so we take that key and then run it through the hash and in addition to getting the key-value pair back we also get an address, where we store that key-value pair. 
+ Hash function/method has two characteristics:
    + It is one way
    + It is deterministic meaning for a particular hash function every time that we put the specific key in it we expect to get the same address back.
      
So the hash function embodies these two characteristics. As said, we have dictionaries as the Python built-in hash tables but we are going to create our own: we create our own address space by creating a list then we create methods.

<a name="44"></a>
######  HT: Collisions 

A collision happens when you put a key-value pair at an address where there was already a key-value pair. These two key-value pairs are put in another list at that specific address. This technique of dealing with collisions where you just put them at the same address is called **separate chaining**. Another way to deal with collisions is that you go down until you find an empty address and then you put the key-value pair there. This technique is called **linear probing** which is a form of **open addressing**. This makes it so that you don’t have more than one key-value pair at any address. In this course, we do separate chaining. Another way of doing separate chaining is instead of having lists that are all stored at that address in our list of address space is we can have a linked list at those addresses. But in this course, we use a list of lists to have various key-value pairs at the same address. 

<a name="45"></a>
###### Implementation 

The point is that you always want to have a prime number of addresses in your address space. The reason for this is that having a prime number addresses increases the amount of randomness for how the key-value pairs will be distributed through the hash table so it reduces your collisions. 

The only thing that the constructor of a hash table does is to build the empty lists of address space. 

        class HashTable:
            def __init__(self, size=7):
                self.data_map = [None] * size

In addition, we want to create our hash method like:

Point: the hash method takes a key to determine the address where we store the key-value pair. The hash method returns a value between zero and size – 1 (to make this happen I have % len(self.data_map) below), which is our address to store the key-value pair in the hash table.  

        class HshTable:
            def __init__(self, size=7):
                self.data_map = [None] * size
        
            def __hash(self, key):
                my_hash = 0
                for letter in key:
                    my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
                return my_hash
        
            def ptinter(self):
                for i, val in enumerate(self.data_map):
                    print(f"{i}: {val}")
        
        my_hash_table = HshTable()
        my_hash_table.ptinter()
        
        output:
        0: None
        1: None
        2: None
        3: None
        4: None
        5: None
        6: None

the __hash method above is a **Python private method.**

Private methods in Python are methods that are **intended for internal use within a class**. They are **not meant to be accessed directly from outside the class**. Python does not enforce true privacy like some other languages, but it uses a convention of name mangling to indicate private methods.

###### How to define a private method

A private method is defined by **prefixing the method name with double underscores __.** For example: 

      class MyClass:
          def __private_method(self):
              print("This is a private method.")

###### How to call a private method

Private methods are intended to be called **from within the class itself.**


      class MyClass:
          def __private_method(self):
              print("This is a private method.")
          
          def public_method(self):
              self.__private_method() # Calling private method from inside the class
      
      obj = MyClass()
      obj.public_method() # Output: This is a private method.

###### Name Mangling

Python uses name mangling to make private methods less accessible from outside the class. When a method name starts with double underscores, the Python interpreter changes its name to **_ClassName__methodname**. This makes it **harder to accidentally access a private method from outside the class.**


      class MyClass:
          def __private_method(self):
              print("This is a private method.")
      
      obj = MyClass()

###### Trying to access the method directly will result in an AttributeError

      #obj.__private_method() # This would cause an error

###### However, we can access it using the mangled name

      obj._MyClass__private_method() # Output: This is a private method.

###### Purpose of private methods

Private methods are used to:

- **Encapsulate internal logic**: They hide implementation details from the outside world.
- **Prevent accidental overriding**: They reduce the risk of child classes unintentionally overriding methods that are not meant to be overridden.
- **Break down complex tasks**: They allow you to break down complex methods into smaller, more manageable parts.


Implementation of methods Set, Get, and Keys: 
  
      class HashTable:
          def __init__(self, size=7):
              self.data_map = [None]*size
      
          def __hash(self, key):
              my_hash = 0
              for letter in key:
                  my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
              return my_hash
      
          def set_item(self, key, value):
              index = self.__hash(key)
              if self.data_map[index] == None:
                  self.data_map[index] = []
              self.data_map[index].append([key, value])
      
          def get_item(self, key):
              index = self.__hash(key)
              if self.data_map[index] is not None:
                  for i in range(len(self.data_map[index])):
                      if self.data_map[index][i][0] == key:
                          return self.data_map[index][i][1]
                  return None

          # def get_item(self, key): # this is my version which found to be better by chatGPT:
          # Your Version is better unless you explicitly need the index for other purposes (e.g., modifying the list in-place or tracking position). It's: More Pythonic, Easier to               # read and maintain, less error-prone. So go with your Version for clarity and best practice.
          #     index = self.__hash(key)
          #     if self.data_map[index] is None:
          #         return None 
          #     for item in self.data_map[index]:
          #         if item [0] == key:
          #             return item[1]
          #     return None 


          def keys(self):
              all_keys = []
              for i in range(len(self.data_map)):
                  if self.data_map[i]:
                      for j in range(len(self.data_map[i])):
                          all_keys.append(self.data_map[i][j][0])
              return all_keys

          def printer(self):
              for i, val in enumerate(self.data_map):
                  print(f"{i} : {val}")
      
      my_t = HashTable()
      my_t.set_item("bolts", 1400)
      my_t.set_item("washers", 50)
      my_t.printer()

      print(my_t.get_item("bolts"))
      print(my_t.get_item("washers"))
      print(my_t.get_item("lumber"))
      print(my_t.keys())
      
      output:
      0 : None
      1 : None
      2 : None
      3 : None
      4 : [['bolts', 1400], ['washers', 50]]
      5 : None
      6 : None
      1400
      50
      None
      ['bolts', 'washers']

<a name="46"></a>
######  HT: Big O 

+ We use linked list instead of a nested list here since it is visually easier to look at
+ Since everything we do with a hash table involves using the hash method, the first thing we need to do is to figure out the big O of the hash method itself. So for a given key of a certain number of letters, it will always be the same number of operations to calculate the hash that means that the hash method itself is O(1)
+ Let’s look at setting an item, we run it through our hash method and let’s say that is going to be at the address of two we append that onto our linked list and appending that is also O(1)
+ Now let’s look at get items: again first we get the address through running our hash method which is O(1) and then it could be either only one operation to find the item or if the item would be in the end of a linked list the big O would be O(n) I mean the worst case would be that all the items being put in the same address and to find the desired item we need to iterate through all the items and so the big o would be O(n) but the assumption with the hash table is that the distribution is going to be more distributed even with the very primitive hash method that we created it gives us a very good distribution of items. The hash method that’s built into Python is going to be even more efficient at distributing all the items and also you are going to be dealing with a much larger address space, so collisions are going to be fairly rare so we treat hash tables which are implemented as dictionaries in Python as a O(1) and it is O(1) to place a key value pair or to look up something by key. Either way it is O(1). 

<a name="47"></a>
######  HT: Interview Question
A very common interview question:
We want to determine whether 2 lists have an item in common.
 Approach 1, which is the naïve approach: 
def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 6]
print(item_in_common(list1, list2))

This approach is of O(n^2) b/c of having nested for loops. This approach is inefficient! 
Approach 2, which is desired by the interviewer: 
def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True

    for j in list2:
        if j in my_dict:
            return True
    return False

list1 = [1, 3, 5]
list2 = [2, 4, 5]
print(item_in_common(list1, list2))

output:
True

The key here is that I avoided using a nested for loops but I have one loop after the other which makes the big o as O(2n) which is simplified as O(n). 

HT: Big O quiz
1-	Both Insert and Lookup by key in a Hash Table is O(1): True
2-	Since a Hash Table is O(1) for Insert and Lookup it is always better than a Binary Search Tree: False b/c Binary Search Trees are sorted which makes them better at searching for all values that fall within a range.
3-	Looking up a value in a Hash Table is O(1): False b/c Key lookup is O(1) but not value. 

<a name="48"></a>
##### Graphs 

<a name="49"></a>
###### Intro

We do have:
+ a vertex or node, the proper to say that is vertex, the plural would be vertices
+ between vertices we have edge or connection, the proper to say it is edge
+ hop: A hop is a step or traversal from one node (vertex) to another via an edge.
     - 1-hop means directly connected (A → B).
     - 2-hops means there's an intermediate node (A → B → C).
     - N-hops refers to paths that require N edge traversals.
      
+ there is no limit to how many other vertices that a vertex can connect to
+ two concepts here:
   + with graphs you may have weighted edges, you are not going to have it always, but you can have. You may use something like this in a maps app to address traffics for example. Another example would be with network routing protocols like it is better to have an extra hop and have two very fast links than one very slow link. Again the edges can be weighted or NOT weighted  
   + bi-directional (like you and your friend are friends on facebook) vs directional relationship (like you follow a celebrity on Instagram but he does not follow you back), in a graph where all the edges are bi-directional you will often see it like without arrows  so if there is no arrows in the edges it is assumed that it is bi-directional and it goes both ways 
   + so in summary the edges can be weighted or not and also they can be directional or bi-directional
+ we already saw a graph in the course: it was a tree, trees are a from of graphs but they have the limitations that each node can only point to two other nodes, also we mentioned we had seen a tree before: a linked list so linked list is a form of a tree which is a form of a graph and so a linked list is a form of a graph with the limitation that they can only point to one other node.

<a name="50"></a>
###### Adjacency Matrix

We have two ways to represent a graph:
+ adjacency matrix
+ adjacency list

the following is an example of an adjacency matrix: 

![](https://github.com/DanialArab/images/blob/main/Python/adjacency%20matrix.png)

The course mentioned each vertex cannot have an edge with itself and that’s why we always have a 45 degree line of zeros (I think this is n ot accurate like in the above image I took from internet it is like vertex D has an edge with itself!). 

In a bi-directional matrix we always have a mirror image on each side of the 45 degree line, if it is directional it would not be like that and we lose the symmetry. 
Also if our edges are weighted we also store these weights in the matrix like instead of having ones in the matrix, like in an above fig., we have the weights associated with each edge. 

<a name="51"></a>
###### Adjacency List

With an adjacency list we represent the graph as a dictionary where the keys are the vertex of interest and the values are a list of all the edges that the vertex in the key has with other vertices like for the above figure I have:
      {
      “A”: [“B”, “C”, “D”],
      …
      }
In our course, we use an adjacency list to represent our graphs. 

<a name="52"></a>
###### Big O

Space complexity of adjacency matrix vs. adjacency list: the huge difference between these two is that in a matrix each vertex has to also store all of the vertices it is not connected to. So from the space complexity standpoint, the adjacency matrix big o is the number of vertices squared i.e., O(|V|^2) while in the adjacency list the big o is the number of vertices plus the number of edges i.e., O (|V| + |E|) so let’s take a look at the big o of the common operations in a graph:
+ adding a vertex (just a vertex not connecting it to anything): for adjacency list is O(1) but for the adjacency matrix is O(|V|^2) b/c basically we need to rewrite the entire matrix. This is a huge difference between the adjacency list and matrix
+ adding an edge: in an adjacency list we append the edges to the lists pretty easy, in an adjacency matrix we change the numbers in the matrix from zero to one for the particular edge therefore adding an edge for both adjacency list and matrix is of O(1).
+ Removing an edge between two vertices: the big o of an adjacency matrix is O(1) b/c I just need to change the numbers one to zero, however, the big o of an adjacency list is O(|E|) b/c we have to iterate through the list of edges that is associated with each one of those vertices so big o is the number of edges that we have to go through. This is a win for matrix over the list
+ Remove the vertex: in a list we have to remove the vertex and also its appearance as edge in all the other edges which means we have to touch everything in the dictionary. In a matrix in order to remove a vertex we have to basically rewrite the entire matrix so the big o would be O(|V|^2) for the matrix and O(|V| + |E|) for the list. For the adjacency list if we have bi-directional connections there is an efficiency in how you can write your method that makes this more efficient
+ When we have a small graphs it is not a big deal to store all the zeros other than the ones in an adjacency matrix but imagine for much larger graphs like a billion items there would be billions of items in a horizontal axis and in the vertical axis  so representing a graph through an adjacency matrix is incredibly inefficient from the storage perspective whereas with the adjacency list we don’t have to store all those zeros so we use adjacency list in this course which is much simpler and much more efficient. 

<a name="53"></a>
###### Implementation

**Add Vertex**

Because our constructor in our class Graph is pretty simple Scott did not devote a separate part to it and included it here:

      class Graph:
          def __init__(self):
              self.adj_list = {}
      
          def add_vertex(self, vertex): 
              if vertex not in self.adj_list: # If not checking this and vertex already exists in self.adj_list, we will overwrite the existing adjacency list of that vertex — potentially deleting existing edges.
                  self.adj_list[vertex] = []
                  return True
              return False
      
          def printer(self):
              for key in self.adj_list:
                  print(f"{key} : {self.adj_list[key]}")
      
      my_graph = Graph()
      print(my_graph.add_vertex("A"))
      my_graph.printer()
      
      output:
      True
      A : []

**Add Edge**

      class Graph:
          def __init__(self):
              self.adj_list = {}
      
          def add_vertex(self, vertex):
              if vertex not in self.adj_list:
                  self.adj_list[vertex] = []
                  return True
              return False
      
          def add_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  self.adj_list[v1].append(v2)
                  self.adj_list[v2].append(v1)
                  return True
              return False

         def add_edge(self, v1, v2): # Prevents duplicate edges in an undirected graph.
              if v1 not in self.adj_list or v2 not in self.adj_list:
                  return False
              if v2 not in self.adj_list[v1]:
                  self.adj_list[v1].append(v2)
              if v1 not in self.adj_list[v2]:
                  self.adj_list[v2].append(v1)
              return True 
        
          def printer(self):
              for key in self.adj_list:
                  print(f"{key} : {self.adj_list[key]}")
      
      my_graph = Graph()
      
      my_graph.add_vertex(1)
      my_graph.add_vertex(2)
      
      my_graph.add_edge(1, 2)
      
      my_graph.printer()
      
      output:
      1 : [2]
      2 : [1]


**Remove Edge**

      class Graph:
          def __init__(self):
              self.adj_list = {}
      
          def add_vertex(self, vertex):
              if vertex not in self.adj_list:
                  self.adj_list[vertex] = []
                  return True
              return False
      
          def add_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  self.adj_list[v1].append(v2)
                  self.adj_list[v2].append(v1)
                  return True
              return False
      
          def remove_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  self.adj_list[v1].remove(v2)
                  self.adj_list[v2].remove(v1)
                  return True
              return False
      
          def printer(self):
              for key in self.adj_list:
                  print(f"{key} : {self.adj_list[key]}")
      
      my_graph = Graph()
      
      my_graph.add_vertex("A")
      my_graph.add_vertex("B")
      my_graph.add_vertex("C")
      
      my_graph.add_edge("A", "B")
      my_graph.add_edge("B", "C")
      my_graph.add_edge("C", "A")
      my_graph.printer()
      print("\n")
      my_graph.remove_edge("A", "B")
      my_graph.printer()
      
      output:
      A : ['B', 'C']
      B : ['A', 'C']
      C : ['B', 'A']
      
      A : ['C']
      B : ['C']
      C : ['B', 'A']

The issue is that our code as it is in the above does not address one of the edge cases which is when there is no edge/connection between the two vertices, my change to solve this:

      class Graph:
          def __init__(self):
              self.adj_list = {}
      
          def add_vertex(self, vertex):
              if vertex not in self.adj_list:
                  self.adj_list[vertex] = []
                  return True
              return False
      
          def add_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  self.adj_list[v1].append(v2)
                  self.adj_list[v2].append(v1)
                  return True
              return False
      
          def remove_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  if v2 in self.adj_list[v1] and v1 in self.adj_list[v2]:
                      self.adj_list[v1].remove(v2)
                      self.adj_list[v2].remove(v1)
                      return True
              return False
      
          def printer(self):
              for key in self.adj_list:
                  print(f"{key} : {self.adj_list[key]}")
      
      my_graph = Graph()
      
      my_graph.add_vertex("A")
      my_graph.add_vertex("B")
      my_graph.add_vertex("C")
      my_graph.add_vertex("D")
      
      my_graph.add_edge("A", "B")
      my_graph.add_edge("B", "C")
      my_graph.add_edge("C", "A")
      my_graph.printer()
      print("\n")
      my_graph.remove_edge("A", "D")
      my_graph.printer()
      
      output:
      A : ['B', 'C']
      B : ['A', 'C']
      C : ['B', 'A']
      D : []
      
      A : ['B', 'C']
      B : ['A', 'C']
      C : ['B', 'A']
      D : []

But the better approach to solve this issue is through using try block like what Scott did and I learned it, which is in the following:

      class Graph:
          def __init__(self):
              self.adj_list = {}
      
          def add_vertex(self, vertex):
              if vertex not in self.adj_list:
                  self.adj_list[vertex] = []
                  return True
              return False
      
          def add_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  self.adj_list[v1].append(v2)
                  self.adj_list[v2].append(v1)
                  return True
              return False
      
          def remove_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  try:
                      self.adj_list[v1].remove(v2)
                      self.adj_list[v2].remove(v1)
                  except ValueError:
                      pass
                  return True
              return False
      
          def printer(self):
              for key in self.adj_list:
                  print(f"{key} : {self.adj_list[key]}")
      
      my_graph = Graph()
      
      my_graph.add_vertex("A")
      my_graph.add_vertex("B")
      my_graph.add_vertex("C")
      my_graph.add_vertex("D")
      
      my_graph.add_edge("A", "B")
      my_graph.add_edge("B", "C")
      my_graph.add_edge("C", "A")
      my_graph.printer()
      print("\n")
      my_graph.remove_edge("A", "D")
      my_graph.printer()
      
      output:
      A : ['B', 'C']
      B : ['A', 'C']
      C : ['B', 'A']
      D : []
      
      A : ['B', 'C']
      B : ['A', 'C']
      C : ['B', 'A']
      D : []

**Remove Vertex**

Before removing a vertex we have to remove all the other edges that vertex has with other nodes and it is only then that we can remove the vertex. 
In the big o section, we already mentioned that there could be an efficiency that we could use in graphs that have bidirectional connections: we know that if vertex D has an edge with one vertex that vertex also has an edge with vertex D. we take advantage of this in our for loop: 

      class Graph:
          def __init__(self):
              self.adj_list = {}
      
          def add_vertex(self, vertex):
              if vertex not in self.adj_list:
                  self.adj_list[vertex] = []
                  return True
              return False
      
          def add_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  self.adj_list[v1].append(v2)
                  self.adj_list[v2].append(v1)
                  return True
              return False
      
          def remove_edge(self, v1, v2):
              if v1 in self.adj_list and v2 in self.adj_list:
                  try:
                      self.adj_list[v1].remove(v2)
                      self.adj_list[v2].remove(v1)
                  except ValueError:
                      pass
                  return True
              return False
      
          def remove_vertex(self, vertex):
              if vertex in self.adj_list:
                  for other_vertex in self.adj_list[vertex]:
                      self.adj_list[other_vertex].remove(vertex)
                  del self.adj_list[vertex]
                  return True
              return False
      
          def printer(self):
              for key in self.adj_list:
                  print(f"{key} : {self.adj_list[key]}")
      
      my_graph = Graph()
      
      my_graph.add_vertex("A")
      my_graph.add_vertex("B")
      my_graph.add_vertex("C")
      my_graph.add_vertex("D")
      
      my_graph.add_edge("A", "B")
      my_graph.add_edge("A", "C")
      my_graph.add_edge("A", "D")
      my_graph.add_edge("B", "D")
      my_graph.add_edge("C", "D")
      my_graph.printer()
      print("\n")
      my_graph.remove_vertex("D")
      my_graph.printer()
      
      output:
      A : ['B', 'C', 'D']
      B : ['A', 'D']
      C : ['A', 'D']
      D : ['A', 'B', 'C']
      
      A : ['B', 'C']
      B : ['A']
      C : ['A']

Quiz 
+ Graphs are the go-to data structure when you need to represent entities and the relationships between them: True. 


<a name="54"></a>
##### Heaps 



<a name="55"></a>
###### Intro 




<a name="54"></a>
### Algorithms

<a name="55"></a>
#### Recursion

<a name="56"></a>
##### Intro

**Recursion is a function that calls itself until it does not**. The example is opening a gift box through running a gift_box function, which returns either a ball or a smaller gift box and we run the function again … 

Points:

+ The process of opening each new box, in our example, is the same. In a general term, the process of whatever we do with recursion has to be the same 
+ Each time we open a box, we make the problem smaller 
+ You have to have a return in your recursive function to make sure that at some point the recursive function finally does not call itself. 
+ When we open the box and it contains the ball this is what we call our base case this is when we are going to stop opening boxes or the function will stop calling itself, so the base case is when we stop calling the recursive function. This is very important to have the if statement for the base case b/c otherwise the function gets called again and again … which is called stack overflow so I do need to have a base case where this will at some point stop calling itself. 
+ The statement of the base case has to be true at some point to prevent infinite looping through creating a stack overflow. So if you get a stack overflow in a recursive function this is one of the places to go troubleshoot 
+ Also if you have a print statement instead of a return statement, if the condition in the if statement is met there would be a print but b/c there is no return statement to cause us to stop running the code we will end up having a stack overflow. So it is very important o have a return statement in your code. 
+ If the recursive function needs to call itself again, this is called a recursive case

<a name="57"></a>
##### Call stack

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

<a name="58"></a>
##### Factorial

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

<a name="59"></a>
#### Basic Sorts

<a name="60"></a>
##### Bubble sort

<a name="61"></a>
###### Intro

We talk about the logic here and then code it next. We want to sort a list. What we do with bubble sort is we start with the first item in the list and we are going to compare it with the second item and if the first item is larger than the second item we are going to switch these then we take the second item and then compare it with the third item if switch is not required we just go to the third item and then compare it with the fourth one and so on and so forth. When we do this and make this comparison all the way up to reaching the last item in the list (meaning finishing the first round), now this last item is sorted, what we have done is we have bubbled up the largest item. In order to do that we have to do 5 comparisons if the list contains 6 items let’s say. Now I only have 5 items left to sort so in this round we only have 4 comparisons: we start back at the beginning and compare the first item to the second item etc. in this round the second largest item out of the list will be bubbled up or sorted. 

<a name="62"></a>
###### Implementation

      def bubble_sort(my_list):
          for i in range(len(my_list)-1, 0, -1):
              for j in range(i):
                  if my_list[j] > my_list[j+1]:
                      my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
                      # temp = my_list[j]
                      # my_list[j] = my_list[j+1]
                      # my_list[j+1] = temp
          return my_list
      
      my_list = [4, 2, 6, 5, 1, 3]
      print(bubble_sort(my_list))
      
      output:
      [1, 2, 3, 4, 5, 6]

Scott wrote the lines as commented above but mine is more concise! Bingo! But the best would be to define a swap function as I learned from Mosh. 

<a name="63"></a>
##### Selection sort

<a name="64"></a>
###### Intro

The difference between bubble sort and selection sort is that here we also need the indexes for the selection sort. Therefore with the selection sort we look at the first item and then we are going to keep track of the index where the minimum value is. The important thing to emphasize here is that we keep track of the index of the minimum value and not the actual minimum value: we are not storing a value but we are storing the index. At the end of the first round when we find the index of the minimum value we switch the minimum value at that index with the first item (at index zero I mean). Now we know that the value at the zero index is sorted then we are going to move to the next item 

<a name="65"></a>
###### Implementation
      
      def selection_sort(my_list):
          for i in range(len(my_list)-1):
              min_index = i
              for j in range(i+1, len(my_list)):
                  if my_list[j] < my_list[min_index]:
                      min_index = j
      
              if i != min_index:
                  swap(my_list, i, min_index)
          return my_list
      
      def swap(li, index1, index2):
          temp = li[index1]
          li[index1] = li[index2]
          li[index2] = temp
      
      print(selection_sort([4, 2, 6, 5, 1, 3]))
      
      output:
      [1, 2, 3, 4, 5, 6]

<a name="66"></a>
##### Insertion sort

<a name="67"></a>
###### Intro

With the insertion sort we always start with the second item in the list. Then we compare it with the previous item if it is less than the previous item we swap their spots. Then we go to the next item and we do the same thing we compare it with the previous item and so on and so forth. There is a case when we move the item to the beginning of the list then j would be -1 so we need to take care of it: 

<a name="68"></a>
###### Implementation

      def insertion_sort(my_list):
          for i in range(1, len(my_list)):
              temp = my_list[i]
              j = i - 1
      
              while temp < my_list[j] and j > -1:
                  my_list[j+1] = my_list[j]
                  my_list[j] = temp
                  j -= 1
      
          return my_list
      
      print(insertion_sort([2, 4, 44, 0, 3, 21, 1]))
      
      output:
      [0, 1, 2, 3, 4, 21, 44]

<a name="69"></a>
###### Big O

Obviously b/c we have a nested loop the big O is O(n^2) as the worst possible scenario. But our best possible scenario is when we have a sorted or almost sorted list, whose big o is O(n). 

**Quiz on Basic Sorts**

1-	Bubble, Selection, and Insertion Sort all have O(n) time complexity: False: b/c each of these three sorting algorithms have a loop within a loop so they are O(n^2).
2-	Bubble, Selection, and Insertion Sort have O(1) space complexity: True, b/c All three of these sort the list in place. That means that they do not create additional copies of the list. That means that the space complexity is O(1).
3-	Bubble, Selection, and Insertion Sort are all O(n) if you start with a sorted (or almost sorted) array: False, Only Insertion Sort is O(n) when you start with sorted (or almost sorted) data.

<a name="70"></a>
#### Merge Sort

<a name="71"></a>
##### Overview

The idea behind merge sort is that if you have two sorted lists it is very easy to combine these into a new sorted list. 
Let’s say if we have an unsorted list of 8 elements what merge sort is going to do is to first break it in half in sequential steps until we only have only one item in the broken lists, like in our example we have 8 separate lists with one item in each and a list with one item in it is by definition a sorted list. Now you can take each two of them and create a new list that is sorted we keep doing this until having 4 lists with 2 items in each we do this again to make 2 lists of 4 items and finally we can combine these two lists to make a sorted lists of 8 elements. This is a high level overview of a merge sort. 

<a name="72"></a>
##### Merge: Intro

Merge function is called a helper function meaning it does not do all of what is required for merge sort but instead it just does a portion of it. The portion that merge function does is it takes two sorted lists, they do need to be sorted, and takes values from these and puts them into a new combined list. How? We loop through each of these lists we will loop through the first one with a variable i and in the second list with a variable j then we just compare i and j and whichever one is lowest we add it to the new combined list. Then we do it again and again until one of the lists is empty once we have done that we have another loop that loops through whichever list that still has items and we will add these items to the combined list. 

<a name="73"></a>
##### Merge: Implementation

Tips: b/c you don’t know how many times you need to loop through you cannot use for loops and instead you need to use while loops. 

      def merge(list1, list2):
          combined = []
          i = 0
          j = 0
          while i < len(list1) and j < len(list2):
              if list1[i] < list2[j]:
                  combined.append(list1[i])
                  i += 1
              else:
                  combined.append(list2[j])
                  j += 1
          while i < len(list1):
              combined.append(list1[i])
              i += 1
      
          while j < len(list2):
              combined.append(list2[j])
              j += 1
      
          return combined
      
      list1 = [1, 2, 7, 8]
      list2 = [3, 4, 5, 6]
      print(merge(list1, list2))
      
      output:
      [1, 2, 3, 4, 5, 6, 7, 8]


<a name="74"></a>
##### Merge Sort: Intro 

Here we want to break the list down into halves and then we can use our merge helper function. We want to write a code to break the list in half. Here b/c the two characteristics of recursion apply (repeating the exact same thing over and over and also making a problem smaller in each step, both of which here are the case) we can use recursion. Also here our base class is happening when our list length would be one, where we want to stop calling our recursive function. At this point we want to use the merge helper function we created before to put the lists back together. So in summary we have three steps in merge sort:

1-	Breaks lists in half
2-	Base case, when len (the_list) is 1
3-	Uses merge () to put lists back together 

<a name="75"></a>
##### Merge Sort: Implementation 

Points:

Merge sort is different compared to the other sorting algorithms we have seen so far, b/c the other sorting algorithms sort the list in place i.e., the original list will be sorted when we are done. But with merge sort the original list stays the same and it returns a separate sorted list. 

      def merge(list1, list2):
          combined = []
          i = 0
          j = 0
          while i < len(list1) and j < len(list2):
              if list1[i] < list2[j]:
                  combined.append(list1[i])
                  i += 1
              else:
                  combined.append(list2[j])
                  j += 1
          while i < len(list1):
              combined.append(list1[i])
              i += 1
      
          while j < len(list2):
              combined.append(list2[j])
              j += 1
      
          return combined
      
      def merge_sort(my_list):
          if len(my_list) == 1:
              return my_list
          mid_index = int(len(my_list)/2)
          left = merge_sort(my_list[:mid_index])
          right = merge_sort(my_list[mid_index:])
      
          return merge(left, right)
      
      original_list = [3, 1, 4, 2]
      sorted_list = merge_sort(original_list)
      print("Original: ", original_list)
      print("Sorted: ", sorted_list)
      
      output:
      Original:  [3, 1, 4, 2]
      Sorted:  [1, 2, 3, 4]


<a name="76"></a>
##### Bog O

Space complexity here is O(n) b/c a list of n items need to be broken into n separate list to be stored in memory and so the big o of space complexity is O(n) but for the previous sorting algorithms we have seen yet the lists are sorted in place meaning we take the original list and we move things around inside of that list but merge sort is different b/c it creates new lists.
Time complexity: big o for breaking a list apart into separate lists with breaking lists in halves  sequentially is log n and then putting them back with merge function is O(n) so we have O(n log n) for merge sort. Reminder is that the other three sorting algorithms we already talked about, bubble, selection and insertion, are all of O(n^2) time complexity while merge sort is of (n log n), which is much more efficient. So n log n is the most efficient that you can make a sorting algorithm that is going to sort multiple types of data. There are certain efficiencies and sorting only numbers and there are some sorting algorithms that can run more efficient than this BUT you can only sort numbers with them. 

<a name="77"></a>
#### Quick Sort 

<a name="78"></a>
##### Quick Sort: Intro

We start with a pivot point that is to be going to the first item, at index 0 I mean, initially. Then we compare each of the items after the pivot point with the pivot point to see if they are less than or greater than that. So long as we reach to the item which is less than the pivot point we swap it with the first item which was greater than the pivot point. At the end of this round we have all the items that are greater than the pivot point are grouped together and also all the items that are less than that are grouped together. Then in the next step, we swap the pivot item with the last item in the less than group items. Two points:

1. The pivot item which is swapped with the last item in the less than group is now sorted.
2. And everything less than that item now is in its left side and everything greater than that item is now in its right side. 

Now we run quick sort again on both items (i.e., less than and greater than items).  We keep doing this until we have only one item left which means it is already sorted. Now we have a completely sorted list. 

<a name="79"></a>
##### Pivot: Intro

It is a helper function for the quick sort. Similar to the merge function that we already used as the helper function in the merge sort. 
What we do in the pivot function is to pick the pivot point and then having all the values less than the pivot value on one side of the pivot value and all the greater values on the other side. The pivot function does two things: rearrange the items in the list and also returns the swap index (not its value but its index). The reason that we return the swap index is that for the next time we want to run the quick sort function we want to run it on the side starting from beginning up to the item before the swap index, not including the swap index, on one side and also on the other side from the item after the swap index up to the end. That is why we need to return the index. 

<a name="80"></a>
##### Pivot: Implementation

      def swap(my_list, index1, index2):
          temp = my_list[index1]
          my_list[index1] = my_list[index2]
          my_list[index2] = temp
      
      def pivot(my_list, pivot_index, end_index):
          swap_index = pivot_index
          for i in range(pivot_index + 1, end_index+1):
              if my_list[i] < my_list[pivot_index]:
                  swap_index += 1
                  swap(my_list, index1=swap_index, index2=i)
          swap(my_list, pivot_index, swap_index)
          return swap_index
      
      my_list = [4, 6, 1, 7, 3, 2, 5]
      print(my_list)
      print(pivot(my_list, 0, 6))
      print(my_list) 
      
      output:
      [4, 6, 1, 7, 3, 2, 5]
      3
      [2, 1, 3, 4, 6, 7, 5]

Again be aware that the pivot function only returns the swap index. 

<a name="81"></a>
##### Quick Sort: Implementation

The quick sort function recursively runs pivot function on each side of the swap index. Be mindful of creating a base case to make sure that you can stop calling the function at some point in a recursion. 
I need to pass the leftmost and the rightmost indexes to the quick_sort function, which are zero and len(my_list) – 1 respectively. With the helper function I defined at the end we don’t need to pass these two and just need to pass the list to the quick sort function. Brilliant idea. 

      def swap(my_list, index1, index2):
          temp = my_list[index1]
          my_list[index1] = my_list[index2]
          my_list[index2] = temp
      
      def pivot(my_list, pivot_index, end_index):
          swap_index = pivot_index
          for i in range(pivot_index+1, end_index+1):
              if my_list[i] < my_list[pivot_index]:
                  swap_index += 1
                  swap(my_list, swap_index, i)
          swap(my_list, pivot_index, swap_index)
          return swap_index
      
      def quick_sort_helper(my_list, left, right):
          if left < right:
              pivot_index = pivot(my_list, left, right)
              quick_sort_helper(my_list, left, pivot_index-1)
              quick_sort_helper(my_list, pivot_index+1, right)
          return my_list
      
      def quick_sort(my_list):
          return quick_sort_helper(my_list, left=0, right=len(my_list)-1)
      
      my_list = [4, 6, 1, 7, 3, 2, 5]
      print(quick_sort(my_list))
      
      output:
      [1, 2, 3, 4, 5, 6, 7]

<a name="82"></a>
##### Big O

The first step is to run the pivot function where we have a for loop, which loops all the way through the list looking at each item, which is of O(n). But the recursive part of the quick sort function is O(log n) based on that the big o of quick sort is n log n like the merge sort BUT this is for the best case and average case and not for the worst case. The worst case is when we already have a sorted list in this case we only have item on the right of the pivot value and when running pivot function again the big o would be O(n) and not log n, and so the big o would be O(n^2). So the big o of quick sort is n squared and so long as you don’t have a sorted data you can count on the quick sort running on n log n but if you have a sorted data it might be better to use something like insertion sort which has generally O(n^2) but the best possible scenario for insertion sort is O(n). So you want to consider these things when looking at sorting algorithms big O. 

<a name="83"></a>
#### Tree Traversal

<a name="84"></a>
##### Intro 

Tree traversal is when we are going to visit every node in the tree and we want to take the values and put them in a list then will return that list. 
Tree traversal is more complicated compared to doing something like with a linked list b/c in a linked list it is just linear so to traverse it we just start at the beginning and go through the list but with the tree there are multiple ways to visit each node one approach is breadth first search another way is depth first search. We look at different ways of DFS in the followings. 

<a name="85"></a>
##### Breadth First Search (BFS)

<a name="86"></a>
###### Intro

We start at the top of the tree then we do the second row and then the third row and so on and so forth. We will create two lists: queue and results, results is the one that will be returned with all the nodes’ values in it. The queue is the one where we include the entire node meaning its value and its left and right. But in the results we are only storing the values and not the entire node. The loop only runs as long as we have items in the queue list like as long as the queue is empty it means that we have visited every item in the tree and the only thing left to do is to return the results list.  

<a name="87"></a>
###### Implementation

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

<a name="88"></a>
##### Depth First Search

There are three types of depth first search: preorder, postorder, and inorder.

<a name="89"></a>
###### PreOrder

<a name="90"></a>
###### Intro 

The order by which we add the items to the list is we start at the top then we keep moving to the left until we reach to point which is as far as we can go to the left then we go up and go right until we reach to the point that we looked at everything to the left of the top node then we go to the right and then we go to the left and then right …. 

<a name="91"></a>
###### Implementation  

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
    
<a name="92"></a>
###### PostOrder

<a name="93"></a>
###### Intro 

Just like the other tree traversal we start at the top what is different here is that we are just going to visit the self.root node we are not going to write that value to the results list yet, then we are going to go to the left then visit that node and then we go to the left again until there is no node to the left and right only then finally we write the value of the last node, which does not have any left or right, to the results list so the order is that we look left then right if there is nothing on the left and right we write the node’s value to the results list. Then we come back up and go to right … the last node which will be written to the results list is the self.root node. 

<a name="94"></a>
###### Implementation  

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
<a name="95"></a>
###### InOrder

<a name="96"></a>
###### Intro 

We start at the top node, we go to the left, then again go to the left until there is nothing to the left then we write that last node to the results list then we go to the right and so on and so forth. In this case we write the lowest value first to the results list then the second lowest value and all the way we add the nodes’ values in numerical order to the results list. 


<a name="97"></a>
###### Implementation  

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


<a name="98"></a>
### Reference:

+ <a href="https://www.udemy.com/course/data-structures-algorithms-python/">Python Data Structures & Algorithms + LEETCODE Exercises</a>
