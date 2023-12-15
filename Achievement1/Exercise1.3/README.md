# Exercise 1.3: Conditional Statements, Loops, and Functions in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Scripts in Python](#scripts-in-python)
4. [Core Operations in Python](#core-operations-in-python)
    - [Comparison Operators](#comparison-operators)
    - [Boolean Logic Operators](#boolean-logic-operators)
    - [Conditional Statements](#conditional-statements)
    - [Loops](#loops)
    - [List Comprehension](#list-comprehension)
    - [The enumerate() Function](#the-enumerate-function)
5. [Functions](#functions)
    - [Defining a Function](#defining-a-function)
    - [Calling a Function](#calling-a-function)
6. [Task Steps](#task-steps)
    - [Step 1: Initialize Lists and Define the Function](#step-1-initialize-lists-and-define-the-function)
    - [Step 2: Collect User Input for Number of Recipes](#step-2-collect-user-input-for-number-of-recipes)
    - [Step 3: Loop for Recipe Input and Processing](#step-3-loop-for-recipe-input-and-processing)
    - [Step 4: Display Recipes with Details and Difficulty](#step-4-display-recipes-with-details-and-difficulty)
    - [Step 5: Print Complete Ingredients List](#step-5-print-complete-ingredients-list)
7. [Learning Journal](#learning-journal)
8. [Screenshots](#screenshots)
9. [Summary](#summary)

## Introduction

In this exercise, you'll enhance your Python skills by mastering conditional statements, loops, and functions. This step is crucial in your journey to becoming proficient in Python, as these concepts are fundamental in programming logic and organizing code.

## Learning Goals

- Implement conditional statements in Python for logical flow.
- Utilize loops to perform repetitive tasks efficiently.
- Write functions to organize and structure Python code.

## Scripts in Python

Scripts are essential for running multiple lines of code efficiently. Unlike the IPython shell, scripts allow you to edit and store your code on your machine, making debugging and code organization easier.

### Example

```python
# Script to capitalize a first and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your name is", first_name.capitalize(), last_name.capitalize())
```

## Core Operations in Python

### Comparison Operators

Comparison operators are used for comparing values, returning boolean outcomes. These operators are fundamental in decision-making processes in Python programming.

- `==`: Equal to - checks if the values of two operands are equal.
- `!=`: Not equal to - checks if the values of two operands are not equal.
- `>`: Greater than - checks if the left operand is greater than the right operand.
- `>=`: Greater than or equal to - checks if the left operand is greater or equal to the right operand.
- `<`: Less than - checks if the left operand is less than the right operand.
- `<=`: Less than or equal to - checks if the left operand is less or equal to the right operand.

Example:

```python
a = 5 
b = 10

print(a < b) # Checking if 'a' is less than 'b'
print(a > b) # Checking if 'a' is greater than 'b'

# Output: 
# True
# False
```

### Boolean Logic Operators

Boolean logic operators are used to create more complex conditional statements. They operate on boolean values and return boolean outcomes.

- `and`: Logical AND - returns True if both the operands are true.
- `or`: Logical OR - returns True if either of the operands is true.
- `not`: Logical NOT - reverses the boolean value of the operand.

Example:

```python
x = True
y = False

print(x and y) # Logical AND
print(x or y) # Logical OR
print(not x) # Logical NOT

# Output:
# False
# True
# False
```

### Conditional Statements

Conditional statements in Python are used to execute different actions based on certain conditions. These statements help in controlling the flow of the program.

- `if`: Executes a block of code if the specified condition is true.
- `elif`: Known as 'else if'. It checks another condition if the previous conditions were not true.
- `else`: Executes a block of code if none of the preceding conditions are true.

Example:

```python
age = 34

if age < 18:
    print("Minor")
elif age < 60:
    print("Adult")
else:
    print("Senior")

# Output:
# Adult
```

### Loops

Loops in Python are used to execute a block of code repeatedly. They are useful for iterating over a sequence (like a list, tuple, dictionary, set, or string).

- `for`: Iterates over a sequence.
- `while`: Repeats a block of code as long as a condition is true.

Example:

```python
# 'for' loop
for i in range(3):
    print(i)

# Output:
# 1
# 2
# 3

# 'while' loop
i = 0
while i < 3:
    print(i)
    i += 1

# Output:
# 1
# 2
# 3
```

### List Comprehension

List comprehension provides a concise way to create lists based on existing lists. It can be used to apply an expression to each element of a list, filter elements based on a condition, or create combinations.

Example:

```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers if n % 2 == 0]

print(squares)

# Output:
# [4, 16]
```

### The enumerate() Function

The `enumerate()` function adds a counter to an iterable and returns it as an `enumerate` object. This is useful for getting both the index and the value when iterating over a sequence.

Example:

```python
fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Output:
# 0 apple
# 1 banana
# 2 cherry
```

## Functions

Functions in Python are reusable blocks of code that perform a specific task. They help in organizing the code, making it more readable and maintainable. Functions can take inputs (arguments), process them, and return outputs.

### Defining a Function

Use the `def` keyword to define a function, followed by a function name and parentheses. Parameters inside the parentheses are placeholders for the arguments.

Example:

```python
def add_numbers(x, y):
    return x + y
```

This `add_numbers` function adds two numbers `x` and `y`.

### Calling a Function

To use a function, call it by its name and provide the required arguments.

Example:

```python
result = add_numbers(3, 4)
print(result)

# Output:
# 7
```

The `add_numbers` is called with `3` and `4` as arguments.

## Task Steps

### Step 1: Initialize Lists and Define the Function

```python
recipes_list = []
ingredients_list = []

def take_recipe():
    name = input("Enter your recipe name: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))
    ingredients_input = input("Enter your ingredients, separated by a comma: ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",")]
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    return recipe
```

This step initializes two lists, `recipes_list` and `ingredients_list`, for storing recipes and their ingredients. The `take_recipe` function is defined to input and process the recipe details. It splits the input ingredients into a list and forms a dictionary with the recipe's name, cooking time, and ingredients.

### Step 2: Collect User Input for Number of Recipes

```python
n = int(input("How many recipes would you like to enter?: "))
print("----------")
```

The user is prompted to specify the number of recipes they wish to enter. This number (`n`) will control the iteration of the following loop for recipe input.

### Step 3: Loop for Recipe Input and Processing

```python
for i in range(n):
    recipe = take_recipe()
    for ingredient in recipe["ingredients"]:
        if ingredient not in ingredients_list:
            ingredients_list.append(ingredient)
    recipes_list.append(recipe)
    print()
```

In this loop, the `take_recipe` function is called to get each recipe, and its ingredients are checked and added to `ingredients_list` if not already present. Each recipe is then added to `recipes_list`.

### Step 4: Display Recipes with Details and Difficulty

```python
print("\n--------------------------\nRecipe Details\n--------------------------")
for recipe in recipes_list:
    num_ingredients = len(recipe["ingredients"])
    cooking_time = recipe["cooking_time"]

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    print(f"Recipe: {recipe['name'].title()}\n  Time: {recipe['cooking_time']} mins")
    print("  Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"  - {ingredient.title()}")
    print(f"  Difficulty: {difficulty}")
    print()
```

This section prints the details of each recipe. It calculates the difficulty based on cooking time and the number of ingredients, and displays the name, time, ingredients, and difficulty level for each recipe.

### Step 5: Print Complete Ingredients List

```python
print("\n--------------------------\nComplete Ingredients List\n--------------------------")
for ingredient in sorted(ingredients_list):
    print(f"- {ingredient.title()}")
```

Finally, the code prints the complete list of unique ingredients used in all the recipes, sorted alphabetically.

## Learning Journal

- The learning journal included reflects on the experience and learning outcomes from this exercise.

## Screenshots

- Two screenshots demonstrating the command-line interface process are included in the repository, named `Part 1.png` and `Part 2.png`.

## Summary

This exercise solidifies an understanding of Python's core operations, equipping learners with skills to write more dynamic and efficient scripts.
