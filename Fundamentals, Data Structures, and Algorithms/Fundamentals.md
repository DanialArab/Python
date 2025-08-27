+ <a href="https://codewithmosh.com/p/python-programming-course-beginners">Complete Python Mastery</a>

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

## Private helper function 

A private helper method in Python is a method intended to be used only inside the class,  not from outside code. It’s a way to organize code by breaking down complex functions into smaller reusable parts, but signaling to users of the class that this method is "internal" and not part of the public API. Python doesn’t enforce privacy strictly, but by convention:
- Methods or attributes prefixed with a single underscore _ are considered private or internal.
- This is just a naming convention to tell other developers: "Hey, don’t use this method directly unless you know what you’re doing.

        def _get_cleaned_subset(self, column_name, use_clean):
      
            if self.data is None:
                raise ValueError("Data not loaded. Use `load_data()` first.")
    
            if use_clean:
                idx = self.clean_data(column_name)
                print(f"Using cleaned data subset for column: {column_name}")
    
            else:
                print(f"Using raw data (no cleaning) for column: {column_name}")
                idx = self.data.index
    
            df_sub = self.data.loc[idx]
            values = df_sub[column_name].fillna('').tolist()
    
            ids = df_sub['Id'].tolist()
            names = df_sub['Name'].tolist()
    
            print(f"Data subset was prepared for embedding generation.")
            return df_sub, values, ids, names


Some points learned from https://www.youtube.com/watch?v=0K_eZGS5NsU:

- In Python, variables are dynamically typed
- arrays are called list in python
- custom sort like arr=['bbb', 'alice', 'jane'] then arr.sort(key=lambda x: len(x))
- from collections import deque 
- HashSet: mySet = set()
- HashMap or dict: myMap = {} 
- import heapq:   heaps are good for finding min and max of a set of values frequently , under the hood they are arrays 
- nested functions
- nonlocal value


## Types of String Literals

1. Single-quoted strings


        s = 'Hello'


2. Double-quoted strings:

        s = "World"


Single and double quotes are interchangeable; use whichever makes it easier to include quotes inside the string.

3. Triple-quoted strings (for multi-line strings or docstrings):

        s = '''This is
        a multi-line
        string'''


or

        s = """This is
        another multi-line
        string"""


4. Raw strings (ignore escape sequences like \n):

        s = r"C:\Users\Danial\Documents"
        print(s)  # prints C:\Users\Danial\Documents


5. f-strings (formatted string literals, Python 3.6+):

        name = "Alice"
        age = 25
        s = f"My name is {name} and I am {age} years old."
        print(s)  # My name is Alice and I am 25 years old.


6. Byte strings (prefix b, used for binary data):

        b = b"Hello"

Escape Sequences

String literals can include special characters using a backslash \:

        s = "Line1\nLine2\tTabbed"
        print(s)


Output:

        Line1
        Line2    Tabbed


In short, a string literal is just how you write a string directly in your Python code.

## XOR

- XOR cancels duplicates: x ^ x = 0.
- XOR with 0 does nothing: 0 ^ x = x.
- So after XOR-ing all numbers, the number that appears only once is left.

136. Single Number - Leetcode

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

        - class Solution:
            def singleNumber(self, nums: List[int]) -> int:
        
                res = 0 
                for n in nums:
                    res ^= n
                    
                return res 


sorted() is a function

You can pass any iterable (like str, list, tuple, dict keys, etc.) to it.

It creates and returns a new sorted list, without changing the input.

Example:

s = "hello"
print(sorted(s))   # ['e', 'h', 'l', 'l', 'o']
print(s)           # "hello" (unchanged)

2. .sort() is a list method

It only works on lists (not strings, tuples, etc.).

It sorts the list in place and returns None.

Example:

lst = [3, 1, 2]
print(lst.sort())   # None
print(lst)          # [1, 2, 3]

3. Why you can pass str to sorted() but not use .sort()

A str is an iterable of characters, so sorted("cat") works and gives ['a', 'c', 't'].

But strings don’t have a .sort() method — because strings are immutable in Python.
(You can’t rearrange the characters of a string in place.)

That’s why this fails:

"cat".sort()   # ❌ AttributeError: 'str' object has no attribute 'sort'


✅ Rule of thumb:

Use .sort() when you already have a list you want to modify.

Use sorted() when you want a new sorted list from any iterable (string, list, tuple, etc.).

The insert() method for Python lists, along with other in-place modifying list methods like append(), extend(), sort(), and reverse(), returns None.

## Errors

- Syntax errors occur when the code is not written correctly according to the rules of the programming language. It's not so different from a spelling or grammar error in a human language, except that computers are much less forgiving.

Sometimes you may get helpful error messages which help you identify the problem. Other times, the error message may not be as clear.

There are many types of programming errors such as syntax errors, runtime errors, and logical errors. Syntax errors are easier to fix, because they usually point out which line the error is on.

- A runtime error is an error that occurs while the program is running. That means the syntax of the program itself is fine. It is usually caused by something that the programmer did not anticipate. Runtime errors can be difficult to debug because they may not always occur consistently. For example, if we programmed a calculator and the user tries to divide by zero, we will get a runtime error.

- A logical error is an error that occurs when the program runs without crashing or producing an error, but the output is not what the programmer intended. This is commonly known as a bug. Logical errors can be difficult to find because as programmers we have to identify which lines of code are causing the incorrect output. There are various techniques to debug logical errors, but in large programs, it can still be very challenging.


