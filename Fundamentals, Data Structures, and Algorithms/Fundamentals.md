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
17. [Truthy and falsy](#17)
18. [Control Flow](#18)
19. [Strings are Immutable](#19)
20. [Set](#20)
21. [Dictionaries](#21)
22. [Reading Stdin](#22)


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

What is the scope of a while loop?

The scope of a while loop is the same as an if statement, so just like if statements, loops do not create their own scope. All variables declared within the while loop are accessible outside of the loop. Loops share the same scope as the function they are in. Or the global scope if they are not in a function.

<a name="17"></a>
## Truthy and Falsy

In Python it's possible to use non-boolean values to execute conditional statements.

        msg = ""
        if msg:
            print("Message is not empty.") # This will not be printed
        
        msg = "Hello, World!"
        if msg:
            print("Message is not empty.") # This will be printed

This is because Python has the concept of truthy and falsy values. **A value is considered truthy if it evaluates to True in a boolean context. A value is considered falsy if it evaluates to False in a boolean context.** The condition in an if statement is considered a boolean context.

A value is falsy if it is:

        False (boolean)
        None (NoneType)
        0 (integer)
        0.0 (float)
        "" (empty string)
        [] (empty list)
        Most other empty collections (e.g. empty tuple, empty set, empty dictionary)

A value is truthy if it is:

        True (boolean)
        All integers other than 0
        All floats other than 0.0
        All strings other than ""
        All collections with at least one element
        This means that the following two if statements are equivalent:

        x = 10
        
        if x:
            print("x is not zero")
        
        if x != 0:
            print("x is not zero")

As a beginner, it may be fine for you to prefer the second form, as it is more explicit. But be aware that the first form is more idiomatic in Python (more common and the intended way to use Python).

What other boolean contexts are there?

Besides the condition in an if statement, there are other contexts where a value is evaluated as a boolean. For example, when using the logical operators and, or, and not, the values are evaluated as booleans.

The boolean context is also used in loops, which we will cover soon.

<a name="18"></a>
## Control Flow

Python provides control statements to alter the execution of loops.

- break: Exits the loop immediately.
- continue: Skips the remaining code inside the loop for the current iteration and moves to the next iteration.
- pass: Acts as a placeholder and does nothing. We cannot have empty loops, so we use pass to avoid errors. It can also be used in conditional statements and functions.

Here's an example demonstrating pass:

        for i in range(1, 8):
            pass
        
        if True:
            pass
        
        def unfinsished_function():
            pass
None of the above code will actually do anything, but it also won't cause an error.

Here's an example demonstrating the break and continue control statements:

        for i in range(1, 8):
            if i == 3:
                continue  
            elif i == 6 :
                break  
            print(i)
The output would be:

        1
        2
        4
        5
Notice that the output is missing some numbers?

Thats because when i was equal to 3 the if statements block of code executed **causing the loop to continue to the next iteration of the loop, before reaching the print(i) line.**

When number was equal to 6 the loop exited, because the break statement executed.

For the numbers where neither condition executed, the print(i) line was reached.

Control flow statements are commonly used, but they are not usually required. They are generally used to make code more readable.

<a name="19"></a>
## Strings are Immutable

It's important to know that whenever you slice a string, you are not modifying the underlying string. Instead, you are creating a new string with the sliced characters. This is because strings are immutable in Python, which means they cannot be changed after they are created.

        message = "I will never change."
        
        message[0] = "X" # This will cause an error

In the above code, we try to reassign just the first character of the string. This will cause a TypeError because strings are immutable. We cannot change individual characters, we can only reassign the entire string.

If we wanted to create a new string with the second character removed, we can accomplish this by slicing and concatenation.


        message = "I will never change."
        
        before_second = message[:1] # "I"
        after_second = message[2:]  # "will never change."

        new_message = before_second + after_second
Above, we removed the second character from the string (which was the space " "), and concatenated the two parts together to create a new string.

<a name="20"></a>
## Intro to Sets
In Python, a set is very similar to a list, but with a few key differences.

- A set is unordered, meaning the elements are not stored in a specific order. **If order is important, you should use a list.**
- A set can only contain unique elements. If you try to add a duplicate element to a set, it will be ignored.

Here is an example:
        
        my_set = {1, 2, 3}
        
        print(my_set)  # Output: {1, 2, 3}
        
        my_set = {3, 2, 1}
        
        print(my_set)  # Output: {1, 2, 3}

As you can see, a set can be created using curly braces {} with elements separated by commas. When printing a set, the elements sometimes appear in sorted order, **but this is not guaranteed**. A set makes no gurantees about the order of the elements stored.

        my_set = set()
        
        my_set.add(1)
        my_set.add(2)
        my_set.add(1)
        
        print(my_set)  # Output: {1, 2}

Above we declared an empty set with set(). We then added the elements 1 and 2 to the set. When we tried to add 1 again, it was ignored because it was already in the set. This is because sets can not contain duplicate elements.

Just like with lists, we can loop over elements within a set using for loops. **The difference is that we can't access elements by index because sets are unordered.** The order that we loop over a set is not guaranteed.

        my_set = {1, 2, 3}
        
        for element in my_set:
            print(element)

We can also convert a list into a set by passing the list into the set() function. We can then convert the set back into a list by passing it into the list() function. **This is an easy way to remove duplicates from a list.**

        my_list = [1, 2, 3, 4, 5, 1, 2, 5]
        
        my_set = set(my_list)
        
        print(my_set)  # Output: {1, 2, 3, 4, 5}
        
        my_list_no_duplicates = list(my_set)
        
Just like with lists, we can also use the in keyword to check if an element is present in a set.

        my_set = {"Cat", "Dog", "Mouse"}
        
        contains_cat = "Cat" in my_set   # True
        contains_lion = "Lion" in my_set # False

Why can't we declare an empty set with curly braces?

If we used empty curly braces {}, it would not have declared a set. That's because Python uses curly braces to declare an empty dictionary. A dictionary is a data structure that stores key-value pairs. We will learn more about dictionaries soon.

<a name="21"></a>
## Dictionaries

### Dict Operations

Dictionaries can't contain duplicate keys, just like sets.

        my_dict = {"a": 1, "b": 2, "c": 3}
        
        print(my_dict["a"]) # Output: 1
        
        my_dict["a"] = 4
        
        print(my_dict["a"]) # Output: 4

**As shown above, if we assign the same key a new value, the old value is overwritten.**

The values within a dictionary can be of any type, including lists, sets, and even other dictionaries.

        my_dict = {"a": [1, 2, 3], "b": {4, 5, 6}, "c": {"x": 7, "y": 8, "z": 9}}
        
        print(my_dict["a"]) # Output: [1, 2, 3]
        print(my_dict["b"]) # Output: {4, 5, 6}
        print(my_dict["c"]) # Output: {"x": 7, "y": 8, "z": 9}

The keys within a dictionary must be unique, but the values can be duplicated.

        my_dict = {"a": 1, "b": 1, "c": 1} # this is valid
        To check if a dictionary contains a key, you can use the in keyword.
        
        my_dict = {"a": 1, "b": 2, "c": 3}
        
        print("a" in my_dict) # Output: True
        print("d" in my_dict) # Output: False

Are key-value pairs in a dict ordered?

In Python 3.7 and later, dictionaries are ordered by the order in which they were inserted. This means that the order of key-value pairs in a dictionary is preserved.

### Dict Remove
You can remove an item from a dictionary using the pop() function. This function takes a key as an argument and removes the key-value pair from the dictionary. If the key doesn't exist, it will raise a KeyError.

        my_dict = {"a": 1, "b": 2, "c": 3}
        
        my_dict.pop("a")
        
        print(my_dict) # Output: {"b": 2, "c": 3}
        
        my_dict.pop("d") # Raises KeyError

**If you don't want to worry about handling the KeyError, you can use the second argument of the pop() function. This argument is the default value that will be returned if the key doesn't exist.**

        my_dict = {"a": 1, "b": 2, "c": 3}
        
        value = my_dict.pop("d", 0) # Returns 0, no error occurs
        
You can also use the **del keyword to remove a key-value pair from a dictionary**. This is a bit more concise than using the pop() function.

        my_dict = {"a": 1, "b": 2, "c": 3}
        
        del my_dict["a"]


<a name="22"></a>
## Reading Stdin

So far we have only printed output to the console, but what if we want to take input from the console?

In Python, the input() function is used to read input to the program while the program is running. This input comes from a stream of data called **standard input or stdin**. This can either mean the data a user types in manually into the terminal (console) or input that is supplied to the program before it is run.

In this course, we will be directly supplying input to your program to simulate user input.

        user_input = input("Enter some text: ") 
        
        print(user_input) # This will print the input to the console

In the above code, input() will print the string "Enter some text: " to the console and read one line of input from stdin. The input will be in the form of a string and will be stored in the variable user_input.

When input() prints text, the following print statement will be **on the same line as the prompt.** So if the input was "some text" in the above example, the output would be:

        Enter some text: some text


#### Why doesn't input print on a different line?

There is a special character in programming called the newline character \n. This character is used to move the cursor to the next line, similar to how you would press the Enter key on your keyboard.

Even though it's called the "newline" character, it's actually two characters: a backslash \ and the letter n. When you see \n in a string, it tells Python to move to the next line.

By default, Python adds a newline character to the end of the string when it calls print() to the console.

The input() function does not do this. It prints to the console without a newline character, so the next print statement will be on the same line.

