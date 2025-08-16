Python OOP from https://neetcode.io/

1. [Classes and Objects ](#1)
   1. [Intro to Classes](#2)
   2. [ What is the self argument?](#3)
   3. [What are Objects?](#4)
   4. [The importance of parameter order](#5)
   5. [Object Attributes](#6)
   6. [Object Methods](#7)
   7. [Self Parameter](#8)
   8. [Init Method](#9)
   9. [Docstrings](#10)
2. [Encapsulation](#11)
   
<a name="1"></a>
# Classes and Objects 

<a name="2"></a>
## Intro to Classes

Imagine you're a game developer creating a superhero game. You start by defining individual heroes:

    hero_1_name = "Iron Man"
    hero_1_power = "repulsor beams"
    hero_1_health = 100
    hero_1_speed = 80

    hero_2_name = "Spider Man"
    hero_2_power = "web slinging"
    hero_2_health = 90
    hero_2_speed = 95
    
This approach has a few problems:

- Repetition: You have to define each hero individually.
- Messy code: It's hard to keep track of all the hero attributes and their values.
- Scalability: What if you need to create 50 different heroes? Your code would become unmanageable very quickly.

Classes

A class is a blueprint for creating objects. Here's the basic syntax for defining a class in Python:

   class SuperHero:
       def __init__(self, name: str, power: str, health: int, speed: int):
           self.name = name
           self.power = power
           self.health = health
           self.speed = speed

In Python, a class is defined with the keyword word class followed by the name of the class and a colon. The __init__ method is a special method that belongs to the class. It creates **an object** and **initializes it's attributes.**

Notice that the __init__ method has an argument self. This is required. The **self variable allows us to add attributes to our object**. It also prevents name conflicts, since name and self.name are different variables.

<a name="3"></a>
## What is the self argument?

In Python, self represents the instance of the class. It's used to access variables and methods associated with the class. When you create an object from a class, Python automatically passes the object as the first argument to the __init__ method. You can name this argument anything you like, but self is the convention.

How to name classes in Python?
Class names in Python use PascalCase convention, meaning each word starts with a capital letter and there are no underscores between words (e.g., SuperHero, IronMan, SpiderMan).


<a name="4"></a>
## What are Objects?

An object is an instance of a class. It's a specific item created using the blueprint defined by the class.

We can create an object by calling the class and passing in the required arguments.

      # Creating superhero objects
      
      iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
      spider_man = SuperHero("Spider Man", "web slinging", 90, 95)
      
When we write iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80), we're telling Python:

- Create a new object variable called iron_man
- Use the SuperHero class to create it
- Set its name attribute to "Iron Man"
- Set its power attribute to "repulsor beams"
- Set its health attribute to 100
- Set its speed attribute to 80

<a name="5"></a>
## The importance of parameter order

When creating a new superhero object, the order of values must match the __init__ method:

      def __init__(self, name, power, health, speed)
      Example:
      
      Correct order
      correct_hero = SuperHero("Captain America", "super strength", 110, 85)
      Incorrect order
      incorrect_hero = SuperHero(100, "Hulk", 75, "gamma radiation")

In the incorrect example, the order of attributes is mismatched. Be careful, **Python won't give us any errors for this incorrect order**, which means we need to be careful when creating our objects!

<a name="6"></a>
## Object Attributes

Attributes are the **properties that define or belong to an object**. In our superhero example, we have the following attributes for a superhero: name, power, health, and speed.

Accessing Attributes

To access an object's attributes, we use **dot notation**: object_name.attribute_name. Let's create a superhero and access its attributes:

      class SuperHero:
          def __init__(self, name: str, power: str, health: int, speed: int):
              self.name = name
              self.power = power
              self.health = health
              self.speed = speed
      
      iron_man = SuperHero("Iron Man", "repulsor beams", 100, 80)
      
      print(iron_man.name)    # Iron Man
      print(iron_man.power)   # repulsor beams
      
Modifying Attributes

We can also modify an attribute's value using the same dot notation:

      iron_man.health = 90
      iron_man.power = "advanced repulsor technology"
      
      print(iron_man.health)  # 90
      print(iron_man.power)   # advanced repulsor technology

Attribute Types

While Python won't give us any errors when changing the data type of an attribute, we should avoid doing so to avoid unexpected behavior.

      iron_man.name = 42       # Allowed but bad practice
      iron_man.health = "full" # Allowed but bad practice

<a name="7"></a>
## Object Methods

Methods are functions that belong to a class or object. They define the behavior of the class or object.

Defining methods in a class

Let's update our SuperHero class to include two methods, use_power() and take_damage(amount):

      class SuperHero:
          def __init__(self, name, power, health, speed):
              self.name = name
              self.power = power
              self.health = health
              self.speed = speed
          
          def use_power(self):
              print(f"{self.name} uses {self.power}!")
          
          def take_damage(self, amount):
              self.health -= amount
              print(f"{self.name} takes {amount} damage. Health is now {self.health}.")

We can create an object of the SuperHero class and call the methods on it:

      iron_man = SuperHero("Iron Man", "super strength", 100, 90)
      
      iron_man.use_power()     # Output: Iron Man uses super strength!
      iron_man.take_damage(20) # Output: Iron Man takes 20 damage. Health is now 80.

Let's break down what's happening in this code:

The use_power() method:
- Takes no parameters (except self, which we'll explain in a future lesson).
- Prints a message saying the superhero is using their power.

The take_damage(amount) method:
- Takes a parameter amount and subtracts it from the object's health.
- Prints a message about the damage taken and the object's new health.

Methods are called on an object using dot notation, like iron_man.use_power(). If a method takes parameters, they are passed in the same way as function arguments e.g. iron_man.take_damage(20).

Method vs Function

Methods are just functions that are defined inside a class. A function defined outside of a class is not a method.

<a name="8"></a>
## Self Parameter

When we create a superhero or call a method, how does Python know which superhero we're talking about? This is where self comes in!

**self is how Python refers to the specific object being created or acted upon.** It allows each superhero to have their own set of attributes and use their own powers.

In some other languages, this is used instead of self.

Let's look at our SuperHero class again:

      class SuperHero:
          def __init__(self, name, power, health, speed):
              self.name = name
              self.power = power
              self.health = health
              self.speed = speed
      
          def use_power(self):
              print(f"{self.name} uses {self.power}!")

Notice how self is the first parameter in all our methods, including __init__. This is a Python convention and is required for methods to work.

How self works in method calls

To better understand how self works, it can be helpful to think of it this way:

spider_man = SuperHero("Spider-Man", "web-slinging", 100, 90)

      spider_man.use_power() # SuperHero.use_power(spider_man)

self inside use_power() refers to spider_man

<a name="9"></a>
## Init Method

The __init__ method we've been using is a special method in Python classes, also known as a constructor. Its job is to initialize the attributes of a new object when it's created.

The __init__ method is technically not a constructor in Python, but it's often referred to as one. The __new__ method is the actual constructor in Python.

      class SuperHero:
          def __init__(self, name, power):
              self.name = name
              self.power = power

The __init__ method is automatically called when we create a new object from our class. It sets up the initial state of the object.

In the above code, __init__ is responsible for setting the initial values for name and power for each new superhero we create.

      # Creating a superhero
      iron_man = SuperHero("Iron Man", "repulsor beams")

Above we created a SuperHero object called iron_man which calls the __init__ method. Logically, this is equivalent to SuperHero.__init__(iron_man, "Iron Man", "repulsor beams")

- We don't need to explicitly pass anything for the self parameter because Python handles this automatically.
- self inside __init__ refers to the new iron_man object
- The other parameters are passed to the __init__ method to initialize the attributes of the object
- After this process, iron_man is a fully initialized SuperHero object with all its attributes set.

Key Points About self and __init__
- The init method is automatically called when creating a new object.
- self is always the first parameter in method definitions, including init.
- When creating objects or calling methods, we don't explicitly provide self - Python handles this automatically.
- Inside init, self refers to the newly created object.
- Use init to set initial values for the object's attributes.

Attributes outside of __init__

- Attributes outside of __init__ are instance attributes. - Within methods, instance attributes are accessed using the self keyword. - Instance attributes are unique to each instance of a class. - Instance attributes are defined outside of any methods in the class, but can also be defined inside the __init__ method using the self keyword.

<a name="10"></a>
## Docstrings

Docstrings are **string literals** that describe functions, methods, classes, or modules. They serve as documentation for our code.

Let's see an example:

      class SuperHero:
          """
          A class to represent a superhero.
      
          Attributes:
              name (str): The superhero's name
              health (int): The superhero's health points
          """
      
          def __init__(self, name: str, health: int) -> None:
              """Initialize a new SuperHero instance."""
              self.name = name
              self.health = health
      
          def take_damage(self, amount: int) -> None:
              """
              Reduce the superhero's health by the given amount.
      
              Args:
                  amount (int): The amount of damage to inflict
              """
              self.health -= amount
              print(f"{self.name} takes {amount} damage.")
              
We have three docstrings in this class:

- The class docstring describes the class and its attributes.
- The __init__ method docstring describes the method and its parameters.
- The take_damage method docstring describes the method and its parameters.

Writing Docstrings

For both classes and methods:

- Use triple quotes (""") to enclose the docstring
- Place the docstring immediately after the class or method definition
- Follow a consistent style (e.g., Google-style)

For classes:

- Describe the purpose of the class
- List and explain attributes

For methods:

- Use a one-line description for simple methods
- For complex methods:
   - Describe what the method does
   - List and explain parameters (Args:)
   - Describe the return value (Returns:)
   - Mention any exceptions raised (Raises:)

Using Docstrings
      # Print the class docstring
      print(SuperHero.__doc__)

Get help on the whole class (includes docstrings of class and methods)

      help(SuperHero)

Print a method's docstring 
      print(SuperHero.take_damage.__doc__)

By adding docstrings, you make your code more understandable for future users, including yourself.

<a name="11"></a>
# Encapsulation

Public Attribute and Method
In Python, public attributes or methods can be accessed and modified directly from outside the class. By default, all attributes and methods in Python are public.

class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.name = name                # public attribute
        self.power_level = power_level  # public attribute
    
    # Public method
    def display_power_level(self) -> None:
        print(f"{self.name} has a power level of {self.power_level}")
When an attribute or method is public, we can:

Access it directly using dot notation
Modify the attribute from outside the class
Call the method from outside the class
Let's see public attributes in action:

# Creating a superhero
spider_man = SuperHero("Spider-Man", 85)

# Accessing public attributes/methods
print(spider_man.name)
spider_man.display_power_level()

# Modifying public attributes
spider_man.power_level = 90
Public attributes are suitable when:

The attribute doesn't need validation
Direct access won't compromise the object's integrity
You want to keep the code simple and straightforward
Don't worry about the above for now, we will cover validation and integrity later.

Challenge
You are given starter code for a simple shop system where items are displayed with their names and prices. Your tasks are:

Add public attributes for name and price
Access the attributes of the chips object and display them. Use this format: Item: [name] - Price: $[price] for printing.
class StoreItem:
    def __init__(self):
        pass  # Add: name, price

chips = StoreItem("Chips", 1.99)
Expected Output

Chips
1.99

Hints
Remember to initialize attributes in the init method
Use descriptive names for your attributes
Public attributes can be accessed using dot notation
Use the print function to display the attributes

What is Encapsulation?
Encapsulation is the concept of wrapping data and methods that work on the data within one unit, called a class. In addition, it restricts access to some of the object's components.
The purpose is to hide the internal details of an object and only expose the necessary parts of the object to the outside world.
A real world analogy is a car. The car is a complex system with many moving parts. However, as a driver, you don't need to know how the car works internally. You only need to know how to operate the car.

Key Points About Public Attributes
Public attributes are accessible from anywhere in the code
They're defined without any special naming convention
They offer direct access to object properties
They're suitable for simple, straightforward data storage
No special methods are needed to access or modify them


Protected Attribute and Method
In Python, protected attributes and methods are class members that should not be accessed directly from outside the class. However, they can be accessed within the class and in child classes (see below for more on child classes).

Protected attributes are denoted by prefixing the attribute/method name with a single underscore _.

class SuperHero:
    def __init__(self, name: str, power_level: int):
        self._name = name                # protected attribute
        self._power_level = power_level  # protected attribute
        
    def get_name(self) -> str: # public method
        return self._name

    def _some_protected_method(self) -> None: # protected method
        pass

    def some_public_method(self) -> None:
        self._some_protected_method() 
Unlike other languages, Python doesn't enforce access control for protected attributes. We can still access them directly, but it's not recommended. Using an underscore prefix is a convention to signal to other developers that these attributes shouldn't be accessed directly from outside.
Below is the recommended way to access protected attributes and methods:

spider_man = SuperHero("Spider-Man", 85)

print(spider_man._name)      # Allowed but discouraged
print(spider_man.get_name()) # Recommended

spider_man._some_protected_method() # Allowed but discouraged
spider_man.some_public_method()     # Recommended
To access protected attributes, use the public methods.
To access protected methods, use the public methods.
Challenge
You are given code for a simple banking system. Your task is to:

Initialize two attributes, "title" a public attribute and "_balance" a protected attribute
Use a public method display_balance to display the balance.
Expected Output

Balance: $1000

Hints
Use underscore prefix for protected attributes during initialization
Remember you can access protected attributes within the class.
Remember protected attributes are still accessible but shouldn't be accessed directly

What's a child class?
A child class is a class that inherits attributes and methods from another class (called the parent class). We'll cover inheritance in detail in upcoming lessons, but for now, just know that protected members are not accessible outside of a class or its child classes.

Remember
Python doesn't enforce protection through technical restrictions, protected attributes (prefixed with _) act as a convention - similar to a yellow traffic light. They warn other developers: You can access this, but you probably shouldn't


Private Attribute and Method
Private attributes and methods are class members that should not be accessed from outside the class. They are denoted by prefixing the attribute/method name with double underscores (__).

Unlike protected attributes, they are not accessible from child classes. We will learn about child classes in the inheritance chapter.

class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name                # private attribute
        self.__power_level = power_level  # private attribute
    
    # private method
    def __secret_power(self) -> str:        
        return f"Using {self.__name}'s secret power!"
        
    # public method to access private method
    def use_power(self) -> str:             
        return self.__secret_power()
    
    # public method to access private attribute
    def get_power_level(self) -> int: 
        return self.__power_level
In the above code, the __name and __power_level attributes are private, meaning they cannot be accessed directly from outside the class. The same goes for the __secret_power method. Though we can access them using the public methods get_power_level and use_power.

When an attribute/method is private:

It should not be directly accessed using normal dot notation from outside the class.
It's meant to be used only within the class itself.
It provides the strongest form of information hiding in Python.
Challenge
You are given the code for the PasswordManager class. Your task is to:

Add a private attribute for storing the password, which should be a string initialized in the constructor.
Implement a public method verify_password that takes an input password and returns True if it matches the stored password, otherwise return False.
Expected Output

True
False

Hints
Use double underscores (__) for private attributes
Remember private attributes can only be accessed within the class

Key Points About Private Attributes
Private attributes are denoted by double underscores (__)
They should be accessed only through public methods
They're ideal for sensitive information e.g passwords

Summary
- Public (no underscore): Accessible everywhere - Protected (single underscore `_` ): Should only be accessed within class and subclasses - Private (double underscore `__` ): Should only be accessed within the defining class
Remember though, Python follows the we're all consenting adults philosophy - these are conventions rather than strict rules. Private/protected attributes can still be accessed, but doing so is strongly discouraged.

Getter and Setter Methods
Solved 
Remember our SuperHero class? We used a private attribute __power_level and accessed it through a method:

class SuperHero:
    def __init__(self, name: str, power_level: int):
        self.__name = name                # private attribute
        self.__power_level = power_level  # private attribute
    
    # method to get power_level
    def get_power_level(self) -> int:      
        return self.__power_level
This method get_power_level() is what we call a getter - it's a method that returns (gets) the value of a private/protected attribute.

Similarly, a setter is a method that sets (changes) the value of a private or protected attribute.

Let's add a setter method to our SuperHero class with validation:

def set_power_level(self, new_level: int) -> None:  # method to set power_level
    if 0 <= new_level <= 100:          # validation
        self.__power_level = new_level
    else:
        print("Power level must be between 0 and 100!")
The above method not only sets the value of the private attribute, but also validates the value. We specically check if the new value is in between 0 and 100 using 0 <= new_level <= 100 in the if statement. If the value is not in the range, we print an error message in the else block.

This ensures we never set an invalid value for the power level. This is another reason we prefer using methods to access and modify private attributes.

Alternatively, we could have raised an error using raise ValueError("Power level must be between 0 and 100!") instead of printing an error message.
Example Usage
hero.set_power_level(90)   # Changes to 90
hero.set_power_level(150)  # Error: Power level must be between 0 and 100!
Challenge
You are given a BankAccount class. Your task is to:

Add a private attribute named __balance which is initialized in the constructor. It should store an integer value.
Add a getter method for balance named get_balance() -> int that returns the balance.
Add a setter method for balance named set_balance(new_balance: int) -> None that sets the value of balance if it is non-negative. If the balance is negative print Cannot set negative balance! and do not update the balance.
Expected Output

1000
Cannot set negative balance!
1000
100
0

Hints
Use double underscore for private balance
Getter just returns the private balance
Setter should check if new balance >= 0

Best Practices
Always use the name get_
<
attribute
>
 for getter methods
Always use the name set_
<
attribute
>
 for setter methods
