# Exercise 1.5: Object-Oriented Programming in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Python and Object-Oriented Programming](#python-and-object-oriented-programming)
4. [Building Your Own Classes](#building-your-own-classes)
5. [Defining Data Attributes](#defining-data-attributes)
6. [Defining Procedural Attributes (Class Methods)](#defining-procedural-attributes-class-methods)
7. [Polymorphism](#polymorphism)
8. [Inheritance and Hierarchies](#inheritance-and-hierarchies)
9. [Class Variables](#class-variables)
10. [Task Steps](#task-steps)
11. [Learning Journal](#learning-journal)
12. [Screenshots](#screenshots)
13. [Summary](#summary)

## Introduction

This exercise delves into the fundamental concepts of Object-Oriented Programming (OOP) in Python, presenting a crucial advancement in the Python programming curriculum. It focuses on imparting a thorough understanding of OOP principles, essential for structuring sophisticated and robust Python applications. The content is tailored to introduce the constructs of classes and objects, encapsulation, and the use of modular code designs. Mastery of these concepts is imperative for the development of efficient and maintainable software solutions, marking a pivotal step towards proficiency in advanced Python programming.

## Learning Goals

- Understand and apply object-oriented programming concepts in Python.
- Learn to define custom classes with data and procedural attributes.
- Master key OOP principles like polymorphism, inheritance, and class variables.

## Python and Object-Oriented Programming

- **Overview of OOP in Python:** Object-Oriented Programming, or OOP, is a way of writing programs that are organized around "objects" rather than "actions." In Python, this means writing code that combines both data and the functions that operate on that data into one unit, called a class. A class can be thought of as a blueprint for creating objects (instances of the class). This approach differs from procedural programming, where data and functions are separate. Python's OOP approach is particularly useful for managing complex programs, as it helps keep code organized and reusable.

- **Understanding Objects and Classes:** A class in Python is like a template that defines the nature of an object. For example, consider a class `Dog`. This class might include data like `name`, `age`, and `breed`, and functions (known as methods) like `bark` or `walk`. An object is an instance of a class. If we create an object `my_dog` from the class `Dog`, `my_dog` will have its own `name`, `age`, and `breed`. We can make many objects from the same class, each with its own specific data. Using classes and objects helps in organizing code, especially in complex programs, by grouping related data and functions.

### Example

```python
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!"

# Creating an object of the class Dog
my_dog = Dog("Buddy", 3, "Golden Retriever")

# Accessing the object's attributes and method
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Buddy says woof!
```

This example demonstrates the creation of a `Dog` class and the instantiation of an object `my_dog` from this class. The object `my_dog` has its own attributes (`name`, `age`, `breed`) and can perform actions defined in the class (like `bark`).

## Building Your Own Classes

Creating your own classes in Python is like defining a new type of object. This is handy when you need a specific kind of object that isn't already built into Python. A class is like a blueprint: it defines what attributes (data) and methods (functions) the objects created from this class will have.

### Key Elements of a Class

1. **Class Name:** This is the name of your class. In Python, class names typically follow the CamelCase naming convention, where each word starts with a capital letter and there's no space between words. For example, `MyClass` is a valid class name, but `my_class` or `myClass` are not.

2. **Inheritance:** Classes can inherit properties and methods from other classes. You'll often see the word `object` in class definitions, which means your class is inheriting from Python's base `object` class. This is a way to create a new class based on the properties of an existing class.

3. **Attributes and Methods:** These are the data and functions that belong to your class. Attributes hold information about the object, while methods define what the object can do.

#### Example: Creating a Date Class

Let's say you want to create a class to handle dates. You'd start by defining the class and its attributes (like day, month, and year) and methods (like a method to print the date).

```python
class Date:
    # Initializer method with attributes
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # Method to display the date
    def display_date(self):
        return f"{self.day}-{self.month}-{self.year}"

# Creating an object of the Date class
my_date = Date(15, 4, 2021)

# Using the method of the Date class
print(my_date.display_date())  # Output: 15-4-2021
```

In this example, `Date` is a class with three attributes (`day`, `month`, and `year`). The `__init__` method initializes these attributes. The `display_date` method is used to print the date in a formatted string. `my_date` is an instance (object) of the `Date` class, and it uses the `display_date` method to display the date.

## Defining Data Attributes

In Python, when building a class, defining data attributes is a way to specify what information each object of that class should hold. This is typically done using the `__init__()` method, which is known as the initializer or constructor. It sets up the object when it is created from the class.

### Using the `__init__()` Method

The `__init__()` method is special in Python. It gets called automatically when you create a new object from a class. Inside this method, you define the attributes you want your objects to have and set their initial values.

#### Example: Building a `Book` Class

Consider a class called `Book`. Each book should have a title, an author, and a number of pages. Here's how you could define this class:

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

# Creating an object of the Book class
my_book = Book("1984", "George Orwell", 328)

# Accessing the attributes of the object
print(f"Book: {my_book.title}, Author: {my_book.author}, Pages: {my_book.pages}")
```

In this example, the `Book` class has three attributes: `title`, `author`, and `pages`. When creating `my_book`, an instance of `Book`, you provide these details. The `__init__()` method then assigns these details to the object's attributes (`self.title`, `self.author`, and `self.pages`).

### Modifiying Object Attributes

After creating an object, you can modify its attributes using dot notation:

```python
# Modifying attributes of my_book
my_book.pages = 350
print(f"Updated Page Count: {my_book.pages}")
```

This changes the `pages` attribute of `my_book` to 350. Such flexibility allows objects to hold and update data specific to them.

By defining a class with an `__init__()` method and setting attributes, you create a template for objects that hold specific pieces of information. Each object created from the class can then have its own unique data, defined when the object is created and modifiable later on. This approach is a cornerstone of organizing data in object-oriented programming in Python.

## Defining Procedural Attributes (Class Methods)

In Python classes, procedural attributes, or class methods, are functions that define the behavior and capabilities of class objects. These methods often manipulate or interact with the object's data attributes.

### Getter and Setter Methods

Getter and setter methods are common in class design. They provide a controlled way of accessing and modifying an object's attributes.

- **Getter Methods:** These methods allow you to retrieve or "get" the value of an object's attribute.
- **Setter Methods:** These methods enable you to change or "set" the value of an object's attribute.

#### Example: Creating a `Vehicle` Class with Getter and Setter

Let's define a `Vehicle` class with attributes like `make`, `model`, and `year`, along with getter and setter methods for these attributes.

```python
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def set_make(self, make):
        self.make = make

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_year(self):
        return self.year

    def set_year(self, year):
        self.year = year

# Creating an instance of Vehicle
my_vehicle = Vehicle("Toyota", "Corolla", 2010)

# Output: Retrieving values using getter methods
print(f"Make: {my_vehicle.get_make()}, Model: {my_vehicle.get_model()}, Year: {my_vehicle.get_year()}")

# Modifying the vehicle's year
my_vehicle.set_year(2015)

# Output: After modification
print(f"Updated Year: {my_vehicle.get_year()}")
```

In this example, the `Vehicle` class has methods to get and set the make, model, and year of a vehicle. Initially, we create a `Vehicle` object `my_vehicle` and then use getter methods to retrieve its attributes. We also use a setter method to change its year.

### Defining Custom Methods

You can also define custom methods for specific functionalities. For instance, let's add a method to check if the vehicle is vintage (older than 25 years).

```python
import datetime

class Vehicle:
    # ... (previous code)

    def is_vintage(self):
        current_year = datetime.datetime.now().year
        return current_year - self.year > 25

# Checking if the vehicle is vintage
print(f"Is Vintage: {my_vehicle.is_vintage()}")
```

In this custom method, `is_vintage`, we calculate if the vehicle's age exceeds 25 years based on the current year.

Class methods, including getters, setters, and custom methods, are essential for encapsulating the logic of a class and safely interacting with its data. They offer a structured and maintainable way to manage objects in Python programming.

## Polymorphism

Polymorphism is a concept in Object-Oriented Programming (OOP) where the same function or method name can be used for different types. This allows methods to do different things based on the object they are called on, even if they share the same name.

### Understanding Polymorphism with Examples

1. **Different Classes with Same Method Names:**
Let's consider two different classes, `Bird` and `Fish`, both with a method named `move`. However, the implementation of `move` is different for each class to represent their respective modes of movement.

```python
class Bird:
    def move(self):
        return "I fly."

class Fish:
    def move(self):
        return "I swim."

# Creating objects
sparrow = Bird()
goldfish = Fish()

# Output: Calling the same method on different objects
print(sparrow.move())  # Output: I fly.
print(goldfish.move())  # Output: I swim.
```

In this example, both `Bird` and `Fish` have a method named `move`, but they perform differently according to their class definition. This is a basic example of polymorphism.

2. **Using a Method Directly from a Class with `self:`**
It's also possible to call a method directly from a class, but you have to pass an instance of the class as an argument. This approach is less common but can be useful in certain scenarios.

```python
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_date(self):
        return f"{self.day}/{self.month}/{self.year}"

# Creating an instance
some_date = Date(15, 6, 2022)

# Calling the method directly from the class
print(Date.get_date(some_date))  # Output: 15/6/2022
```

Here, the `get_date` method is called directly from the `Date` class, passing the `some_date` object as an argument.

3. **Method to Interact Between Multiple Objects:**
Methods can be designed to interact with multiple objects of the same class. For instance, consider a `ShoppingList` class that allows merging two shopping lists into one.

```python
class ShoppingList:
    def __init__(self, list_name):
        self.list_name = list_name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def merge_lists(self, other_list):
        merged_items = self.items + other_list.items
        return ShoppingList("Merged List").add_items(merged_items)

# Creating two shopping lists
fruits_list = ShoppingList("Fruits")
fruits_list.add_item("Apples")
fruits_list.add_item("Bananas")

veggies_list = ShoppingList("Vegetables")
veggies_list.add_item("Carrots")
veggies_list.add_item("Spinach")

# Merging the two lists
combined_list = fruits_list.merge_lists(veggies_list)

# Output: Displaying combined list items
print(combined_list.items)  # Output: ['Apples', 'Bananas', 'Carrots', 'Spinach']
```

In this case, the `merge_lists` method takes another object of the `ShoppingList` class and merges its items with the current list.

Polymorphism allows methods with the same name to perform differently based on the object they are associated with. It enhances flexibility in code and enables more dynamic and versatile programming practices.

## Operator Overloading in Python

Operator overloading allows custom classes in Python to interact with built-in operators such as `+`, `-`, `*`, etc. This means you can define how operators should work with your class objects.

### Understanding Operator Overloading with Examples

1. **Basics of Operator Overloading:**
By default, operators like `+` and `-` work with built-in data types (e.g., numbers, strings). However, they do not automatically work with custom class objects. To enable this functionality, you must explicitly define how these operators should behave with your class objects. This is done using special methods with double underscores, like `__add__` for `+` and `__sub__` for `-`.

2. **Example: Overloading the + Operator in a Custom Class:**
Let's create a `Vector` class and define how the `+` operator should work when adding two `Vector` objects.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Creating two Vector objects
v1 = Vector(2, 4)
v2 = Vector(3, 1)

# Using the overloaded + operator
result = v1 + v2
print(result)  # Output: Vector(5, 5)
```

In this example, the `__add__` method is defined to add two `Vector` objects. When `v1 + v2` is executed, it calls `v1.__add__(v2)`, resulting in a new `Vector` object with combined x and y values.

3. **Overloading Other Operators:**
Similarly, you can overload other operators like `-`, `*`, etc. For instance, to define subtraction for the `Vector` class:

```python
class Vector:
    # ... (previous code)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

# Using the overloaded - operator
result = v1 - v2
print(result)  # Output: Vector(-1, 3)
```

Here, `__sub__` is defined to subtract two `Vector` objects, and `v1 - v2` calls `v1.__sub__(v2)`.

Operator overloading is a powerful feature in Python that allows custom classes to interact with built-in operators. By defining special methods like `__add__`, `__sub__`, etc., you can specify how operators should behave with your class objects, making them more intuitive and easier to use.

## String Representation of an Object in Python

In Python's object-oriented programming, the string representation of an object is crucial for providing clear and understandable output when objects are printed. This representation is managed by the `__str__` method in class definitions.

### Using `__str__` for Readable Output

- **Purpose of `__str__`:** The `__str__` method in a class defines how an instance of that class will be printed or converted to a string. Without it, the `print()` function outputs a default and less informative representation like `<__main__.Object at 0x000001E6A7AAE790>`.

- **Defining `__str__` Method:** This method is intended to return a string that ideally represents the object in a user-friendly format.

#### Example: `Height` Class with String Representation

Consider a `Height` class that stores a person's height. By implementing `__str__`, we ensure that whenever an instance of `Height` is printed, it presents the height in a readable format.

```python
class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

# Creating and printing an instance of Height
adam_height = Height(5, 10)
print(adam_height)  # Output: 5 feet, 10 inches
```

### Operator Overloading for Enhanced Functionality

Additionally, Python allows for operator overloading, enabling objects to interact with operators like `+` or `-`. For instance, we can define how two `Height` objects are added together:

```python
class Height:
    # ... (existing __init__ and __str__)

    def __add__(self, other):
        total_inches = (self.feet * 12 + self.inches) + (other.feet * 12 + other.inches)
        new_feet = total_inches // 12
        new_inches = total_inches % 12
        return Height(new_feet, new_inches)

# Example of using the overloaded + operator
height1 = Height(5, 10)
height2 = Height(4, 2)
total_height = height1 + height2
print("Total height:", total_height)  # Output: Total height: 10 feet, 0 inches
```

In the `__add__` method, we handle the addition of two `Height` objects, converting their heights to inches, summing them up, and then converting back to feet and inches.

The `__str__` method plays a vital role in defining how objects are represented as strings, particularly when printed. Coupled with operator overloading like `__add__`, it allows for a more intuitive and rich interaction with class instances, making custom classes in Python both versatile and user-friendly.

## Inheritance and Hierarchies

Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class to inherit properties and methods from another class. This mechanism promotes code reuse and establishes a hierarchy between classes.

### Basics of Inheritance

- **Parent and Child Classes:** The class whose properties are inherited is known as the parent (or base) class, and the class that inherits these properties is called the child (or subclass) class.
- **Single Inheritance:** When a child class inherits from one parent class, it's known as single inheritance.
- **Multi-level Inheritance:** When a subclass becomes a parent for another subclass, it creates multi-level inheritance.

#### Example: Creating a Basic Inheritance Structure

Let's illustrate inheritance with an example. Consider a simple class `Animal` (as the parent class) and a subclass `Dog`.

```python
class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print("Some generic animal sound")

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, species, name):
        super().__init__(species)  # Call to the parent class's constructor
        self.name = name

    def make_sound(self):  # Overriding the method from Animal
        print("Woof!")

# Using the classes
generic_animal = Animal("Generic Animal")
generic_animal.make_sound()  # Output: Some generic animal sound

buddy = Dog("Canine", "Buddy")
buddy.make_sound()  # Output: Woof!
```

In this example, `Dog` inherits from `Animal`. It has its own constructor (`__init__`) but also calls the constructor of `Animal` using `super().__init__(species)`. The `make_sound` method is overridden in `Dog` to provide a specific implementation.

### Building a Hierarchy with Inheritance

Inheritance allows for the creation of a class hierarchy, where subclasses can inherit from a parent class and then become parent classes for further subclasses.

#### Example: Extending the Animal Hierarchy

Expanding on the previous example, let's add another class `Cat` that also inherits from `Animal`.

```python
class Cat(Animal):  # Cat inherits from Animal
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def make_sound(self):
        print("Meow")

# Creating a Cat instance
whiskers = Cat("Feline", "Whiskers")
whiskers.make_sound()  # Output: Meow
```

Here, both `Dog` and `Cat` are subclasses of `Animal` and have unique implementations of `make_sound`.

### Overriding Methods and Using `super()`

In inheritance, child classes can override methods of the parent class to provide specific behavior. They can also use `super()` to call methods from the parent class.

#### Example: Human Class Inheriting from Animal

Let's create a `Human` class that inherits from `Animal` and introduces additional attributes and methods.

```python
class Human(Animal):
    def __init__(self, name, age):
        super().__init__("Human")
        self.name = name
        self.age = age

    def speak(self, message):
        print(f"{self.name} says: {message}")

# Creating a Human instance
alice = Human("Alice", 30)
alice.speak("Hello, world!")  # Output: Alice says: Hello, world!
```

In this `Human` class, we define a new method `speak` and override the `__init__` method while still calling the `__init__` of `Animal` using `super()`.

Inheritance is a powerful feature in OOP that enhances code organization and reuse. It allows classes to inherit properties and behaviors from other classes, creating a structured and hierarchical codebase. This mechanism simplifies code maintenance and scalability in software development.

## Class Variables

Class variables in Python are an essential aspect of object-oriented programming (OOP). They provide a way for data to be shared across all instances of a class, unlike instance variables that are unique to each object.

### Understanding Class Variables

- **Shared Among Instances:** Class variables are shared across all instances of a class. Any change made to a class variable affects all instances of that class.
- **Defining Class Variables:** These variables are declared within the class but outside of any methods. Unlike instance variables, they are not prefixed with `self`.

#### Example: Implementing Class Variables

Consider a class `Car` with a class variable `total_cars` to keep track of how many `Car` objects have been created.

```python
class Car:
    total_cars = 0  # Class variable

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1  # Increment the class variable

# Creating Car instances
car1 = Car("Toyota", "Corolla")
car2 = Car("Ford", "Mustang")

# Accessing the class variable
print("Total cars created:", Car.total_cars)  # Output: Total cars created: 2
```

In this example, `total_cars` is incremented each time a new `Car` object is created. This variable is shared among all `Car` instances.

### Modifying Class Variables

Changes to class variables are reflected across all instances. This makes them useful for representing properties that should be common to all objects of that class.

```python
# Changing the class variable
Car.total_cars = 5

# The change is reflected in all instances
print("Total cars now:", car1.total_cars)  # Output: Total cars now: 5
```

### Practical Application: Unique Identifiers

A use case for class variables is assigning unique identifiers to each instance of a class.

```python
class Car:
    id_counter = 0  # Class variable for unique ID

    def __init__(self, make, model):
        self.id = Car.id_counter
        self.make = make
        self.model = model
        Car.id_counter += 1

# Creating Car instances
car_a = Car("Honda", "Civic")
car_b = Car("Mazda", "3")

# Each car has a unique ID
print("Car A ID:", car_a.id)  # Output: Car A ID: 0
print("Car B ID:", car_b.id)  # Output: Car B ID: 1
```

Here, `id_counter` is used to give each `Car` object a unique `id`. When a new car is created, `id_counter` is incremented, ensuring each car has a different identifier.

Class variables in Python are a powerful tool in OOP, allowing shared data across all instances of a class. They are particularly useful for keeping track of state or properties that are common to all objects of that class, such as counters or configuration settings. Understanding and utilizing class variables effectively can lead to more organized and efficient code structures.

## Task Steps

### Building the `Recipe` Class

**Purpose:** To define a class structure for recipes, encapsulating related data and methods.

**Code:**

```python
class Recipe:
    all_ingredients = set() # Class variable to store all unique ingredients

    def __init__(self, name, cooking_time):
        self.name = name
        self.ingredients = []
        self.cooking_time = cooking_time
        self.difficulty = None

    # Additional methods...
```

### Implementing Recipes

**Purpose:** Create instances of the `Recipe` class to represent various recipes.

**Code:**

```python
# Creating recipe instances and adding ingredients
tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)
```

### Searching Recipes

**Purpose:** Implement a method to search for recipes based on specific ingredients.

**Code:**

```python
def recipe_search(recipes, search_term):
    for recipe in recipes:
        if recipe.search_ingredient(search_term):
            print(recipe)

# Creating a list of recipes
recipes_list = [tea, coffee, cake, banana_smoothie]

# Searching for recipes containing specific ingredients
print("Recipes with Water:")
recipe_search(recipes_list, "Water")

print("Recipes with Sugar:")
recipe_search(recipes_list, "Sugar")

print("Recipes with Bananas:")
recipe_search(recipes_list, "Bananas")
```

### Final Implementation

**Purpose:** Combine all components to create a comprehensive recipe application using OOP.

**Code:**

```python
class Recipe:
    all_ingredients = set() # Class variable to store all unique ingredients across all recipes

    def __init__(self, name, cooking_time):
        self.name = name # Name of the recipe
        self.ingredients = [] # List to store ingredients of this recipe
        self.cooking_time = cooking_time # Cooking time in minutes
        self.difficulty = None # Difficulty level, calculated based on ingredients and cooking time

    def add_ingredients(self, *args):
        # Adds ingredients to the recipe and updates overall ingredient list
        for ingredient in args:
            self.ingredients.append(ingredient)
            self.update_all_ingredients(ingredient)
        self.calculate_difficulty() # Recalculate difficulty after adding new ingredients

    def calculate_difficulty(self):
        # Determines the difficulty of the recipe based on number of ingredients and cooking time
        num_ingredients = len(self.ingredients)
        if self.cooking_time < 10:
            self.difficulty = "Easy" if num_ingredients < 4 else "Medium"
        else:
            self.difficulty = "Intermediate" if num_ingredients < 4 else "Hard"

    def get_name(self):
        # Returns the name of the recipe
        return self.name
    
    def set_name(self, name):
        # Sets a new name for the recipe
        self.name = name

    def get_cooking_time(self):
        # Returns the cooking time of the recipe
        return self.cooking_time
    
    def set_cooking_time(self, cooking_time):
        # Sets a new cooking time and recalculates difficulty
        self.cooking_time = cooking_time
        self.calculate_difficulty()

    def get_ingredients(self):
        # Returns the list of ingredients for the recipe
        return self.ingredients

    def get_difficulty(self):
        # Returns the difficulty level, calculates it first if not already set
        if self.difficulty is None:
            self.calculate_difficulty()
        return self.difficulty

    def search_ingredient(self, ingredient):
        # Checks if an ingredient is in the recipe
        return ingredient in self.ingredients
    
    def update_all_ingredients(self, ingredient):
        # Updates the class variable with new ingredients
        Recipe.all_ingredients.add(ingredient)

    def __str__(self):
        # String representation of the recipe
        return f"Recipe: {self.name}\nCooking Time: {self.cooking_time} mins\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.difficulty}\n"
    
def recipe_search(recipes, search_term):
    # Searches for a given ingredient in a list of recipes
    for recipe in recipes:
        if recipe.search_ingredient(search_term):
            print(recipe)


# Main code
            
# Creating recipe instances and adding ingredients
print("--------------------------------------------------")
print("# Creating recipe instances and adding ingredients")  
print("--------------------------------------------------\n")        

tea = Recipe("Tea", 5)
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
print(tea)

coffee = Recipe("Coffee", 5)
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
print(coffee)

cake = Recipe("Cake", 50)
cake.add_ingredients("Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk")
print(cake)

banana_smoothie = Recipe("Banana Smoothie", 5)
banana_smoothie.add_ingredients("Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes")
print(banana_smoothie)


# Creating a list of recipes and searching for an ingredient
recipes_list = [tea, coffee, cake, banana_smoothie]


# Searching for recipes containing specific ingredients
print("-------------------------------------------------------")
print("# Searching for recipes containing specific ingredients")
print("-------------------------------------------------------")

print("---------------------")
print("Recipes with Water:")
print("---------------------")
recipe_search(recipes_list, "Water")

print("---------------------")
print("Recipes with Sugar:")
print("---------------------")
recipe_search(recipes_list, "Sugar")

print("---------------------")
print("Recipes with Bananas:")
print("---------------------")
recipe_search(recipes_list, "Bananas")
```

**Output:**

Image of the Command Line Interface for Part 1 of `%run recipe_oop.py`:

![CMD output of recipe_oop.py - Part 1](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.5/images/Task_Part_1.png)

Image of the Command Line Interface for Part 2 of `%run recipe_oop.py`:

![CMD output of recipe_oop.py - Part 2](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement1/Exercise1.5/images/Task_Part_2.png)

## Learning Journal

- The learning journal included reflects on the experience and learning outcomes from this exercise.

## Screenshots

- Two screenshots demonstrating the command-line interface process are included in the repository, named `Task_Part_1.png` and `Task_Part_2.png`.

## Summary

This exercise focuses on the application of object-oriented programming in Python, emphasizing the creation and manipulation of classes and objects. The knowledge and skills acquired here are fundamental for advanced Python programming and real-world applications.
