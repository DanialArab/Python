1. [Zip Function](#1)
2. [Two Pointers](#2)
3. [Private helper function](#3)
4. [Types of String Literals](#4)
5. [XOR](#5)
6. [sort vs sorted](#6)
7. [Errors](#7)
8. [ Naming Conventions](#8)
9. [Dynamic Typing](#9)
10. [Type Casting](#10)
11. [Parameter vs. argument](#11)
12. [Type Hints](#12)
13. [Scope](#13)
14. [Global vs local scope](#14)
15. [Default argument](#15)
16. [If statement scope](#16)



<a name="1"></a>
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

<a name="2"></a>
## Two Pointers

In programming, "two pointers" refers to a technique where you use two references or indices to traverse or manipulate elements in a data structure. These pointers are typically used to track different positions within the data structure simultaneously.

The concept of two pointers is commonly used in algorithms and data structures, especially when dealing with arrays, linked lists, and strings. By maintaining two pointers, you can perform operations efficiently by iterating or comparing elements in a coordinated manner.

Here are a few common scenarios where two pointers are used:

+ Two-pointer technique: In this technique, you use two pointers that start at different ends of an array or list and move towards each other until they meet or cross paths. This approach is often used to search for pairs or patterns in a sorted or partially sorted array or list. It can help optimize the time complexity by avoiding unnecessary comparisons.

+ Sliding window technique: This technique involves maintaining a window or a subarray within a larger array by using two pointers. The window is defined by the two pointers, and it can be moved or expanded as needed. This technique is useful for solving problems that involve finding subarrays, substring problems, or optimizing algorithms by reducing redundant computations.

+ Fast and slow pointers: In some scenarios, you might need to traverse a linked list or an array at different speeds. You can use a fast pointer that moves faster than a slow pointer to perform operations such as cycle detection, finding middle elements, or partitioning.

These are just a few examples of how two pointers can be used in programming. The technique is versatile and can be adapted to various problem-solving situations to optimize algorithms and improve efficiency.

<a name="3"></a>
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


<a name="4"></a>
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

<a name="5"></a>
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

<a name="6"></a>
## sort vs sorted

#### sorted() is a function

You can pass any iterable (like str, list, tuple, dict keys, etc.) to it.

It creates and returns a new sorted list, without changing the input.

Example:

        s = "hello"
        print(sorted(s))   # ['e', 'h', 'l', 'l', 'o']
        print(s)           # "hello" (unchanged)

#### .sort() is a list method

It only works on lists (not strings, tuples, etc.).

It sorts the list in place and returns None.

Example:

        lst = [3, 1, 2]
        print(lst.sort())   # None
        print(lst)          # [1, 2, 3]

#### Why you can pass str to sorted() but not use .sort()

A str is an iterable of characters, so sorted("cat") works and gives ['a', 'c', 't'].

But strings don’t have a .sort() method — because strings are immutable in Python.
(You can’t rearrange the characters of a string in place.)

That’s why this fails:

        "cat".sort()   # ❌ AttributeError: 'str' object has no attribute 'sort'


Rule of thumb:
- Use .sort() when you already have a list you want to modify.
- Use sorted() when you want a new sorted list from any iterable (string, list, tuple, etc.).
- The insert() method for Python lists, along with other in-place modifying list methods like append(), extend(), sort(), and reverse(), returns None.

<a name="7"></a>
## Errors

- Syntax errors occur when the code is not written correctly according to the rules of the programming language. It's not so different from a spelling or grammar error in a human language, except that computers are much less forgiving.

Sometimes you may get helpful error messages which help you identify the problem. Other times, the error message may not be as clear.

There are many types of programming errors such as syntax errors, runtime errors, and logical errors. Syntax errors are easier to fix, because they usually point out which line the error is on.

- A runtime error is an error that occurs while the program is running. That means the syntax of the program itself is fine. It is usually caused by something that the programmer did not anticipate. Runtime errors can be difficult to debug because they may not always occur consistently. For example, if we programmed a calculator and the user tries to divide by zero, we will get a runtime error.

- A logical error is an error that occurs when the program runs without crashing or producing an error, but the output is not what the programmer intended. This is commonly known as a bug. Logical errors can be difficult to find because as programmers we have to identify which lines of code are causing the incorrect output. There are various techniques to debug logical errors, but in large programs, it can still be very challenging.


<a name="8"></a>
## Naming Conventions

More than having good variable names, it's important to follow naming conventions. These are rules that help us write code that is easy to read and understand.

There are several different naming conventions such as:

- Camel Case: The first letter of each word is capitalized except for the first word. For example, myVariableName.
- Snake Case: Words are separated by underscores. For example, my_variable_name.
- Pascal Case: The first letter of each word is capitalized. For example, MyVariableName.

In Python, we typically use snake case. This means we use underscores (_) to separate words in variable names.

<a name="9"></a>
## Dynamic Typing

In Python a single variable's type can change throughout the code. This is called dynamic typing. For example, the following code will run without any errors:

        variable = 10         # int type
        variable = "Hello"    # str type
        variable = [1, 2, 3]  # list type
        
Not all languages support dynamic typing. In some languages, a variable's type must be explicitly declared and cannot be changed. This is called static typing. For example, in Java, the following code will cause an error:

        int variable = 10;
        variable = "Hello";  // Error: incompatible types

#### Is dynamic typing a good idea?

Dynamic typing should generally be avoided when possible. This means you should avoid changing a variable's type throughout your code. If you do, you may not know what type a variable is at any given time, which can lead to bugs and make your code harder to understand.

Static typing is employed by many languages on purpose. It can help catch errors early, make code easier to read, and improve performance.

Each typing system has it's own advantages and disadvantages. Dynamic typing is flexible, but can be error-prone. Static typing is safer, but can be inflexible.

<a name="10"></a>
## Type Casting

A variable in Python can be converted to a different type using type casting. For example, the following code will run without any errors:

        variable = 10.9
        print(int(variable))
        This code will output:
        
        10
        
The variable variable is a floating-point number. The int() function converts it to an integer. The output is the integer part of the floating-point number, aka rounding the number down.

#### Type Errors

Even though variable types can change, there are still rules about what types of variables can be used together. For example, the following code will cause an error:

        message = "Hello"
        message = int(message)
        
We can't convert a string to an integer, unless the string is a number. This code will cause a ValueError.

<a name="11"></a>
## Parameter vs. argument

What is the difference between a parameter and an argument?

        def greet(name):
            msg = "Hello, " + name
            print(msg)
        
        greet("Alice")  # This will print "Hello, Alice"

A parameter is a variable in a function definition. When a function is called, the arguments are the data you pass into the function's parameters. In the example above, the parameter is name and the argument is "Alice".

If we next call the function by passing in "Bob" as the argument, the parameter is still name, but the argument is now "Bob".

<a name="12"></a>
## Type Hints

In Python, you can add type hints to your functions to indicate what type of data the function expects to receive and return. This is not required, but it can be helpful for other developers who are reading your code.

        def add(x: int, y: int) -> int:
            return x + y

To add a type hint for a parameter, you add a colon after the parameter name and then the type of data you expect. To add a return type, you add a right arrow (->) after the closing parenthesis and then the type of data you expect to return (before the colon).

**Type hints don't change how the function works, for example, we could still pass a couple of strings to the add function above and it would still work.**

What if we had a function that did not return anything? The return type would be None.

        def greet(name: str) -> None:
            print("Hello, " + name)

What if we explicitly return None?

Whether we don't return anything from a function, or explicitly return None, or even have an empty return statement, **the return value will be None in all cases.**

<a name="13"></a>
## Scope

Consider the following code:

        n = 10
        print(n)         # Output: 10
        
        def print_number(n):
            print(n)
        
        print_number(11) # Output: 11

        print(n)         # Output: 10
        
First n is assigned the value of 10 and printed.
Next we call the function print_number and pass in the value 11. The name of the parameter for this function is also n. But this does not cause an error in Python.
After the function call is complete, the value of the original n is printed and it's still 10.
This can be explained by the concept of scope in programming.

In programming, **the scope refers to the visibility or accessibility of variables within different parts of the code.** The value 11 passed into the print_number() function, is only accessible within the function. The function has its own scope, and the variable n inside the function is a different variable than the one outside the function. This is why the value of the original n is still 10 after the function call.


<a name="14"></a>
## Global vs Local Scope

Here are a few more examples illustrating scope in Python:

        def declare_variable() -> None:
            inside_function_only = 10
            return
        
        declare_variable()
        print(inside_function_only) # This will raise a NameError
        
In the code above, the variable inside_function_only is declared inside the function declare_variable. This variable has a local scope and is only accessible within the function. Attempting to access it outside the function will result in a **NameError.**

        n = 10
        
        def print_global_variable() -> None:
            print(n)
        
        print_global_variable() # This will print 10
        
In the code above, the variable n is declared outside the function print_global_variable. This variable has a global scope, since it's not within a function, and can be accessed from anywhere in the program, including inside functions.

Note: We saw earlier, that **if the function has a parameter with the same name as a global variable, the function will use the local variable instead of the global variable.**

**Global Scope:**

- Variables declared outside of any function have a global scope.
- They can be accessed from anywhere in the program, including inside functions.

**Local Scope:**

- Variables declared within a function have a local scope.
- They can only be accessed within the function in which they are defined.
- Local variables are created when the function is called and destroyed when the function exits.

<a name="15"></a>
## Default Arguments

You can specify default values for parameters in a function definition.

        def greet(name="world"):
            print("Hello, " + name + "!")
        
        greet()       # This will print "Hello, world!"
        greet("Bob")  # This will print "Hello, Bob!"
        
In the above code, we have given the parameter name a default value of "world". If we call the function without any arguments, the default value will be used. If we call the function with an argument, that argument will be used instead.

We can also have multiple parameters with default values. **But the order of the parameters matters! If you have a parameter with a default value, all parameters after it must also have default values.**

        # This is valid
        def greet(greeting="Hello", name="world"):
            print(greeting + ", " + name + "!")
        
        # This is valid
        def greet(greeting, name="world"):
            print(greeting + ", " + name + "!")
        
        # This is NOT valid
        def greet(greeting="Hello", name):
            print(greeting + ", " + name + "!")

<a name="16"></a>
## If Statement Scope

Unlike functions, **if statements do not create a new scope**. This means that variables defined inside an if statement are accessible outside of the if statement. Here's an example:

        if True:
            message = "Hello"
        
        print(message)  # This will print "Hello"

They can also update variables that were defined outside of the if statement. Here's an example:

        balance = -100
        
        if balance < 0:
            balance = 0
        
        print(balance)  # This will print 0

Within functions, if statements have the same scope as the function. This means that variables defined inside an if statement are accessible within that function, but not outside of it. Here's an example:

        def is_balance_low(balance: int):
            if balance <= 100:
                message = "Warning: Low balance."
            print(message)
        
        is_balance_low(50)  # This will print "Warning: Low balance."
        print(message)  # This will cause an error
