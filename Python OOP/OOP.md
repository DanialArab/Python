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
