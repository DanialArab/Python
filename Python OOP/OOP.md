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
   1. [Public Attribute and Method](#12)
   2. [What is Encapsulation?](#13)
   3. [Protected Attribute and Method](#14)
   4. [Private Attribute and Method](#15)
   5. [Getter and Setter Methods](#16)
   6. [Property and Setter Decorator](#17)
      1. [Why use @property and @setter?](#18)
   7. [How to access properties](#19)
4. [Class attributes](#20)
   1. [Class Attributes](#21)
   2. [Class vs Instance Attributes](#22)
   3. [Class Methods](#23)
   4. [Static Methods](#24)
   
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

<a name="12"></a>
## Public Attribute and Method

In Python, public attributes or methods can be accessed and modified directly from outside the class. **By default, all attributes and methods in Python are public.**

      class SuperHero:
          def __init__(self, name: str, power_level: int):
              self.name = name                # public attribute
              self.power_level = power_level  # public attribute
          
          # Public method
          def display_power_level(self) -> None:
              print(f"{self.name} has a power level of {self.power_level}")
              
When an attribute or method is public, we can:

- Access it directly using dot notation
- Modify the attribute from outside the class
- Call the method from outside the class

Let's see public attributes in action:

      # Creating a superhero
      spider_man = SuperHero("Spider-Man", 85)
      
      # Accessing public attributes/methods
      print(spider_man.name)
      spider_man.display_power_level()
      
      # Modifying public attributes
      spider_man.power_level = 90
      
Public attributes are suitable when:

- The attribute doesn't need validation
- Direct access won't compromise the object's integrity
- You want to keep the code simple and straightforward

Don't worry about the above for now, we will cover validation and integrity later.

Hints
- Remember to initialize attributes in the init method
- Use descriptive names for your attributes
- Public attributes can be accessed using dot notation
- Use the print function to display the attributes

<a name="13"></a>
## What is Encapsulation?

**Encapsulation is the concept of wrapping data and methods that work on the data within one unit, called a class**. In addition, it restricts access to some of the object's components.

**The purpose is to hide the internal details of an object and only expose the necessary parts of the object to the outside world.**

A real world analogy is a car. The car is a complex system with many moving parts. However, as a driver, you don't need to know how the car works internally. You only need to know how to operate the car.

Key Points About Public Attributes
- Public attributes are accessible from anywhere in the code
- They're defined without any special naming convention
- They offer direct access to object properties
- They're suitable for simple, straightforward data storage
- No special methods are needed to access or modify them


<a name="14"></a>
## Protected Attribute and Method

**In Python, protected attributes and methods are class members that should not be accessed directly from outside the class. However, they can be accessed within the class and in child classes (see below for more on child classes).**

Protected attributes are denoted by prefixing the attribute/method name with a **single underscore _.**

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

Unlike other languages, Python doesn't enforce access control for protected attributes. We can still access them directly, but it's not recommended. Using an underscore prefix is a **convention to signal to other developers that these attributes shouldn't be accessed directly from outside.**

Below is the recommended way to access protected attributes and methods:

      spider_man = SuperHero("Spider-Man", 85)
      
      print(spider_man._name)      # Allowed but discouraged
      print(spider_man.get_name()) # Recommended
      
      spider_man._some_protected_method() # Allowed but discouraged
      spider_man.some_public_method()     # Recommended
      
- To access protected attributes, use the public methods.
- To access protected methods, use the public methods.

Hints
- Use underscore prefix for protected attributes during initialization
- Remember you can access protected attributes within the class.
- Remember protected attributes are still accessible but shouldn't be accessed directly

What's a child class?

A child class is a class that inherits attributes and methods from another class (called the parent class). We'll cover inheritance in detail in upcoming lessons, but for now, just know that **protected members are not accessible outside of a class or its child classes.**

Remember
- Python doesn't enforce protection through technical restrictions, protected attributes (prefixed with _) act as a convention - similar to a yellow traffic light. They warn other developers: You can access this, but you probably shouldn't


<a name="15"></a>
## Private Attribute and Method

Private attributes and methods are class members that should not be accessed from outside the class. They are denoted by prefixing the attribute/method name with double underscores (__).

**Unlike protected attributes, they are not accessible from child classes.** We will learn about child classes in the inheritance chapter.

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

- It should not be directly accessed using normal dot notation from outside the class.
- It's meant to be used only within the class itself.
- It provides the **strongest form of information hiding in Python.**

Hints
- Use double underscores (__) for private attributes
- Remember private attributes can only be accessed within the class

Key Points About Private Attributes
- Private attributes are denoted by double underscores (__)
- They should be accessed only through public methods
- They're ideal for sensitive information e.g passwords

Summary
- Public (no underscore): Accessible everywhere - Protected (single underscore `_` ): Should only be accessed within class and subclasses - Private (double underscore `__` ): Should only be accessed within the defining class
- Remember though, Python follows the **we're all consenting adults philosophy** - these are conventions rather than strict rules. Private/protected attributes can still be accessed, but doing so is strongly discouraged.

<a name="16"></a>
## Getter and Setter Methods

Remember our SuperHero class? We used a private attribute __power_level and accessed it through a method:

      class SuperHero:
          def __init__(self, name: str, power_level: int):
              self.__name = name                # private attribute
              self.__power_level = power_level  # private attribute
          
          # method to get power_level
          def get_power_level(self) -> int:      
              return self.__power_level

This method get_power_level() is what we call a getter - it's a method that **returns (gets) the value of a private/protected attribute.**

**Similarly, a setter is a method that sets (changes) the value of a private or protected attribute.**

Let's add a setter method to our SuperHero class with validation:

      def set_power_level(self, new_level: int) -> None:  # method to set power_level
          if 0 <= new_level <= 100:          # validation
              self.__power_level = new_level
          else:
              print("Power level must be between 0 and 100!")

The above method not only sets the value of the private attribute, but **also validates the value**. We specically check if the new value is in between 0 and 100 using 0 <= new_level <= 100 in the if statement. If the value is not in the range, we print an error message in the else block.

**This ensures we never set an invalid value for the power level. This is another reason we prefer using methods to access and modify private attributes.**

Alternatively, we could have raised an error using raise ValueError("Power level must be between 0 and 100!") instead of printing an error message.
      
         Example Usage
         hero.set_power_level(90)   # Changes to 90
         hero.set_power_level(150)  # Error: Power level must be between 0 and 100!


Best Practices
- Always use the name get_ <attribute> for getter methods
- Always use the name set_<attribute> for setter methods


<a name="17"></a>
##  Property and Setter Decorator

Python provides a more idiomatic way to use getters and setters using the @property and @setter decorators.

      class Hero:
          def __init__(self, name: str):
              self.__name = name    # private attribute
      
          # Getter
          @property
          def name(self) -> str:
              return self.__name
              
          # Setter
          @name.setter
          def name(self, new_name: str) -> None:
              if new_name != "":             
                  self.__name = new_name
              else:            
                  print("Name cannot be empty!")
                  
In the above code, we have defined two methods with the same name as attribute name. But these are two different methods. We **use @property to define a getter method and @name.setter to define a setter method.** We also added validation logic in the setter method to prevent setting the name to an empty string.

      hero = Hero("Batman")
      
      # Getting name
      print(hero.name)        # this calls the getter method not the attribute
      # Setting name
      hero.name = "Superman"  # this calls the setter method not the attribute
      hero.name = ""         # Error: Name cannot be empty!
      
In the above code, we created an instance of the Hero class and accessed and modified the name attribute. But internally, accessing the name attribute calls the getter method name and modifying the name attribute calls the setter method name.

**Notice that the field name is __name but the method names for the getter and setter are still name.**

<a name="18"></a>
### Why use @property and @setter?
- Makes code look cleaner
- Feels more natural (like using attributes)
- Still gives us control (validation, etc.)

Hints
- Use @property for the getter
- Use @balance.setter for the setter
- Remember to keep the name of the attribute the same for both the getter and setter methods

Some hints:

- Use the __ prefix to make the attributes private
- Use the getter and setter methods to access the private attributes
- Use the get keyword to implement the getter methods
- Use the set keyword to implement the setter methods
- You can't print the private attributes directly use the getter methods to access them

Some hints:
- Use the __ prefix to make the attributes private
- Use @property to create getter properties
- Use @property_name.setter to create setter properties
- The validation logic stays the same as in the original getter/setter methods

<a name="19"></a>
## How to access properties 

The key point is that in Python, **properties are accessed like attributes, not like methods.**

Let’s break it down:

1. Without @property

Normally, if you wrote a getter method like:

      def get_name(self):
          return self.__name


then you would call it with parentheses:

      hero.get_name()


and to set, you’d need a separate setter method, e.g., set_name("Superman").

2. With @property

The @property decorator **transforms a method into something that acts like an attribute, even though it’s really calling a method under the hood.**

So this:

      @property
      def name(self):
          return self.__name


lets you write:

      hero.name  # instead of hero.name()


And with the setter:

      @name.setter
      def name(self, new_name: str):
          ...


you can write:

      hero.name = "Superman"   # instead of hero.set_name("Superman")

3. Why not hero.name() = "Superman"?

Because hero.name() means “call the getter function”, which returns the current string. Strings are immutable, so "Superman" can’t be assigned to the return value.

hero.name = "Superman" works because the property system intercepts assignment and calls the setter method.

So the magic of @property is:

- hero.name → calls the getter method.
- hero.name = "Superman" → calls the setter method.

You never use () unless you defined it as a normal method.


<a name="20"></a>
# Class Attributes

<a name="21"></a>
## Class Attributes
 
When assembling the Avengers to fight Thanos, certain information needs to be shared across all heroes. For instance, Nick Fury needs to track how many heroes we have ready for battle. This is where class attributes come in.

class Superhero:
    hero_count = 0      # Class attribute
    
    def __init__(self, name: str, power: str):
        self.name = name      # Instance attribute
        self.power = power    # Instance attribute
        Superhero.hero_count += 1
In the above code, hero_count is a class attribute, where as name and power are instance attributes.

In this case, hero_count belongs to the entire superhero class - not to individual heroes. This attribute is shared by all instances of the class. Unlike instance attributes, we don't use the self keyword to access class attributes.

Class attributes must be declared outside the __init__ method and without the self keyword.

iron_man = Superhero("Iron Man", "repulsor beams")
thor = Superhero("Thor", "lightning")

print(f"Heroes ready to face Thanos: {Superhero.hero_count}")  # This should print 2
In the above code, we created two instances of the Superhero class, iron_man and thor. We then accessed the class attribute hero_count using the class name Superhero.hero_count.

Notice that we access class attributes using the class name, not the instance name. This is because class attributes are shared by all instances of the class. Class attributes can be updated outside the class as well.

Note: We can also access the class attribute using the instance of the class iron_man.hero_count but it's not recommended. That's because the class attribute belongs to the class, not to the instance.
Challenge
You are given code for class SmartDevice. Modify it to track the total and active devices in your house:

Add two class attributes:
total_devices: Track total number of devices created, initialized to 0
active_devices: Track number of devices currently turned on, initialized to 0
Implement these methods:
turn_on(): Increase active devices by 1
turn_off(): Decrease active devices by 1
Note:

total_devices increases in __init__ (already done for you)
Methods should only update active_devices count
Expected Output

Total Devices: 2
Active Devices: 1

Hints
Use className.attributeName = value to update the class attribute

<a name="22"></a>
## Class vs Instance Attributes

The below example shows a BankAccount class with class and instance attributes.

class BankAccount:
    total_accounts = 0    # Class attribute: Shared by ALL accounts
    total_balance = 0     # Class attribute: Tracks bank's total money
    
    def __init__(self, name: str, balance: float):
        self.name = name        # Instance: Each account has unique owner
        self.balance = balance  # Instance: Each account has unique balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance
We use class attributes to track bank-wide information that is shared by all accounts, such as the total number of accounts and the total balance of all accounts.
We use instance attributes to track information that is unique to each account, such as the account number and the balance of the account.
Challenge
Your task is to implement a BankAccount class that effectively uses both class and instance attributes.

The attributes you need to track are:

The total number of accounts in bank total_accounts
The bank's total balance total_balance
The individual account owner names name
The individual account balances balance
You tasks are:

Decide which attributes should be class vs instance attributes and add them at their appropriate places
Implement the BankAccount class
Create two accounts, "Alice" and "Bob" with balances 1000 and 2000 respectively
Print the information using the following format:
print(f"Alice's balance: <Alice's balance>")
print(f"Bob's balance: <Bob's balance>")
print(f"Total Accounts: <Total Accounts>")
print(f"Total Balance: <Total Balance>")
Expected Output
Alice's balance: $1000
Bob's balance: $2000
Total Accounts: 2
Total Balance: $3000

Hints
Think: Does the attribute need to be shared across ALL accounts?
Class attributes are defined outside __init__
Instance attributes are defined inside __init__
Remember to update class attributes when creating new accounts


<a name="23"></a>
## Class Methods
 
So far the methods we have used were all related to the instance of the class. For example, we used use_power method which was used by a single superhero.

Sometimes we need special methods that work with the entire class rather than individual instances. For example, we may want to upgrade the training level of all heroes at once. Let's see how we can do that using class methods.

class Superhero:
    training_level = 1  # Class attribute
    
    def __init__(self, name: str, power: str):
        self.name = name         # Instance attribute
        self.power = power       # Instance attribute
        
    @classmethod
    def upgrade_training(cls) -> None:
        cls.training_level += 1
        print(f"All heroes now at training level {cls.training_level}")
In the above Superhero class, the upgrade_training method is a class method.

It uses @classmethod decorator to define the class method
It uses cls as the first parameter instead of self
It upgrades the training_level (a class attribute) by 1
cls is used to access the class attribute instead of the class name Superhero
The below code shows how the recommended way to call the class method:

Superhero.upgrade_training()     # Recommend way to use class method
print(Superhero.training_level)  # 2
The below code shows how the class method can be called using an instance of the class, which is not recommended:

iron_man = Superhero("Iron Man", "Flying")
iron_man.upgrade_training()     # Works but not recommended
print(iron_man.training_level)  # 2
Important: Class methods are similar to class attributes. They are shared by all instances of the class. This also means that they do not have access to instance attributes, which is why we don't use self in class methods. Class methods can be defined with additional parameters, after the cls parameter.

Challenge
Given the code for Library class, implement the following two class methods to manage book lending.

lend_books that takes number as an argument and subtracts it from books_available
return_books that takes number as an argument and adds it to books_available
Expected Output

Initial status: 100 books available
After lending: 70 books available
After return: 80 books available

Hint
Always pass cls as the first parameter to the class method
Use cls.books_available to access the class attribute
Use cls.books_available -= number to decrease the number of books available
Use cls.books_available += number to increase the number of books available


<a name="24"></a>
## Static Methods 
So far we've seen instance methods (using self) and class methods (using cls).

There are also static methods which are similar to class methods but they don't have access to self or cls. They do not have access to instance attributes, but they can still access class attributes using the class name.

They are just regular functions that live inside a class for organizational purposes.

class Superhero:
    def __init__(self, name: str, power: str):
        if not self.is_valid_power(power):
            raise ValueError(f"Invalid power: {power}")
        self.name = name        # Instance attribute
        self.power = power      # Instance attribute
    
    @staticmethod
    def is_valid_power(power: str) -> bool:
        valid_powers = ['Flying', 'Strength', 'Speed', 'Intelligence']
        for valid_power in valid_powers: # Iterate over each valid power and check if the power matches
            if power == valid_power:
                return True
        return False
In the above code, we defined a class Superhero with a static method is_valid_power. We call this method using the self parameter within the __init__ method for validation before creating the hero.

Alternatively, we could have defined this method outside the class, but this method would never be needed outside the class. Thus, it's best to define it inside the class for organizational purposes.

Below is an example of how this class can be used. Notice that we can also call the static method using the class name.

print(Superhero.is_valid_power('Flying'))         # True
print(Superhero.is_valid_power('Mind Reading'))   # False

iron_man = Superhero("Iron Man", "Flying")        # Works

mind_reader = Superhero("Hero", "Mind Reading")   # Raises ValueError
Challenge
Complete the CurrencyConverter class to convert between currencies using static methods. You are already given the rates class attribute which you can use to convert between currencies. Your tasks is to:

Implement the static method to_usd that takes an amount and a currency code as arguments and converts the amount to USD and returns the converted amount.
Expected Output
100 EUR = 120.0 USD
100 JPY = 1.0 USD

Hints
Use @staticmethod decorator to define the static methods
Use the rates dictionary to convert between currencies
You don't need to pass self or cls as the first parameter in static methods
Use the CurrencyConverter.rates to access the rates class attribute in the static methods

Implement Power Calculation System
Suppose we are developing a game where we need to calculate the effective power level of a hero when creating it. You are given the Hero class and its __init__ method. Your tasks are:

1. Add a static method calculate_effective_power that takes two parameters:
base_power: The hero's base power level (integer)
attributes: A dictionary containing the hero's attributes (strength, speed, intelligence)
The method should:

Calculate the attribute_bonus by averaging all attribute values. Use sum(attributes.values()) / len(attributes) to calculate the average
Calculate effective power using the formula: base_power * (1 + attribute_bonus)
Round the final result to one decimal place. Use round(number, 1) to round to one decimal place
Return the calculated effective power
Expected Output:

Base Power: 8
Attributes: {'strength': 7, 'speed': 6, 'intelligence': 8}
Effective Power: 64.0

Base Power: 6
Attributes: {'strength': 4, 'speed': 5, 'intelligence': 6}
Effective Power: 36.0

Hints
Use the @staticmethod decorator to define the static method
Don't pass self or cls as a parameter to the static method


