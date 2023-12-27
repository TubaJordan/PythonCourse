# Exercise 1.4: File Handling and Exception Management in Python

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Working with Files in Python](#working-with-files-in-python)
4. [Working with Pickles](#working-with-pickles)
5. [Navigating through Directories with the os Module](#navigating-through-directories-with-the-os-module)
6. [Handling Errors and Exceptions](#handling-errors-and-exceptions)
7. [Task Steps](#task-steps)
    - [Part 1: recipe_input.py Script](#part-1-recipe_inputpy-script)
    - [Part 2: recipe_search.py Script](#part-2-recipe_searchpy-script)
    - [Part 3: Final Steps](#part-3-final-steps)
8. [Learning Journal](#learning-journal)
9. [Screenshots](#screenshots)
10. [Summary](#summary)

## Introduction

In this exercise, you're set to broaden your Python proficiency by diving into the realms of file handling and exception management. This pivotal step is integral in your Python learning journey, as it introduces you to essential aspects of persistent data storage and robust error handling. Grasping these concepts is vital for developing well-structured and resilient Python applications. You'll not only learn how to save and retrieve data using various file types but also enhance your scripts' reliability through effective error management techniques. Embrace this exciting phase, as it brings you closer to mastering Python's more sophisticated and practical applications.

## Learning Goals

- Learn to read and write data to files.
- Understand the use of 'pickles' for complex data structures.
- Master error and exception handling in Python scripts.

## Working with Files in Python

### Working with Text Files

Python's ability to handle text files is a fundamental aspect of file operations. Text files, typically with a `.txt` extension, are one of the most common and straightforward file types you'll encounter.

#### The open() Method

The `open()` function is the gateway to file manipulation in Python. It allows you to open a file in a specified mode:

```python
file = open('example.txt', 'r') # Open 'example.txt' in read mode
# Output: File is opened for reading.
```

#### The read() Method

The `read()` method is used to read the entire contents of a file:

```python
content = file.read()
print(content)
# Output: Displays the entire contents of 'example.txt'.
```

#### The readline() Method

`readline()` reads a single line from the file each time it is called.

```python
first_line = file.readline()
print(first_line)
# Output: Prints the first line from 'example.txt'.
```

#### The readlines() Method

`readlines()` reads all lines in the file and returns them as a list of strings.

```python
lines = file.readlines()
print(lines)
# Output: Prints a list of all lines in 'example.txt'.
```

#### Using the close() Method to Close the File Stream

Closing a file is essential to free up resources.

```python
file.close()
# Output: File 'example.txt' is closed.
```

#### Writing to a File with write()

Use write mode ('w') to write data to a file.

```python
file = open('newfile.txt', 'w')
file.write("Hello, Python!")
file.close()
# Output: 'Hello, Python!' is written to 'newfile.txt'.
```

#### Using the wrtielines() Method

`writelines()` writes a list of strings to the specified file.

```python
lines_to_write = ["First line\n", "Second line\n"]
file = open('newfile.txt', 'w')
file.writelines(lines_to_write)
file.close()
# Output: 'First line' and 'Second line' are written to 'newfile.txt'.
```

#### The with Keyword

The `with` statement simplifies file handling by automatically managing file open and close.

```python
with open('newfile.txt', 'w') as file:
    file.write("Using the with keyword for file operations.")
# Output: The specified text is written, and the file is automatically closed.
```

## Working with Pickles

### Introduction to Pickles

For more complex data structures, like dictionaries, Python's pickle module is used to serialize these objects. Serialized objects are converted into a byte stream (pickles) that can be stored in binary files.

#### Writing with the pickle.dump() Method

First, import the `pickle` module and initialize a complex data structure, like a dictionary:

```python
import pickle

book = {
    'title': 'Python Simplified',
    'author': 'Jane Doe',
    'year': 2021,
    'genres': ['Programming', 'Technology']
}
```

Next, serialize this dictionary and write it to a binary file using `pickle.dump()`:

```python
with open('bookdetails.bin', 'wb') as file:
    pickle.dump(book, file)
# Output: The 'book' dictionary is serialized and saved to 'bookdetails.bin'.
```

The `book` dictionary is now stored as a byte stream in `bookdetails.bin`.

#### Reading from a Binary File with pickle.load()

Use `pickle.load()` to deserialize the byte stream from the binary file, converting it back into a Python object:

```python
with open('bookdetails.bin', 'rb') as file:
    loaded_book = pickle.load(file)

print("Book Details:")
print(f"Title: {loaded_book['title']}")
print(f"Author: {loaded_book['author']}")
print(f"Year: {loaded_book['year']}")
print(f"Genres: {', '.join(loaded_book['genres'])}")
# Output:
# Book Details:
# Title: Python Simplified
# Author: Jane Doe
# Year: 2021
# Genres: Programming, Technology
```

This code snippet reads the binary data from `bookdetails.bin`, treating it as a pickle, and reconstructs the original `book` dictionary.

## Navigating through Directories with the os Module

Python's `os` module is a versatile tool for directory and file management. It offers various commands to interact with the file system.

### The os.getcwd() Command

`os.getcwd()` returns the current working directory. It's useful to understand your script's directory context.

```python
import os
print(os.getcwd())
# Output: Prints the current working directory path.
```

### The os.chdir() Command

`os.chdir()` changes the current working directory. This is useful when your script needs to interact with files in different directories.

```python
os.chdir('/path/to/directory')
print(os.getcwd())
# Output: Changes the directory and prints the new directory path.
```

### The os.listdir() Command

`os.listdir()` lists all files and directories in the current directory. It's helpful when you need to inspect the contents of a directory.

```python
contents = os.listdir()
print(contents)
# Output: Prints a list of files and directories in the current directory.
```

### The os.mkdir() Command

`os.mkdir()` creates a new directory in the current working directory.

```python
os.mkdir('new_directory')
print(os.listdir())
# Output: Creates 'new_directory' and then prints updated directory contents.
```

### A Practical Example

Suppose you have a project directory with separate folders for data and scripts. You want to access a data file from a script:

1. First, find out your current working directory:

```python
print(os.getcwd())
# Output: '/path/to/project/scripts'
```

2. Change the directory to the data folder:

```python
os.chdir('../data')
print(os.getcwd())
# Output: '/path/to/project/data'
```

3. List the contents of the data directory:

```python
print(os.listdir())
# Output: ['datafile1.csv', 'datafile2.csv']
```

4. Open a data file:

```python
with open('datafile1.csv', 'r') as file:
    print(file.read())
# Output: Displays the contents of 'datafile1.csv'.
```

This example illustrates how to navigate directories and manage files using Python's `os` module, showcasing its importance in organizing and accessing file structures in larger projects.

## Handling Errors and Exceptions

Handling errors and exceptions is crucial to ensure your Python scripts run smoothly and handle unexpected situations gracefully.

### Commom Errors in File Handling

During file operations, errors such as a missing file or an incorrect directory path can occur. These errors, if not handled, can cause your script to terminate unexpectedly.

### The try-except Block

Python's `try-except` block allows you to handle potential errors in a controlled manner. It prevents the script from crashing and provides a way to respond to errors appropriately.

Example: Reading a File

Consider an example where you try to open a file that might not exist:

```python
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found. Please check the filename.")
finally:
    print("Execution complete.")
# Output:
# If 'example.txt' exists, its content is printed. Otherwise, "File not found. Please check the filename." is displayed.
```

### Handling Specific Exceptions

Python allows you to handle specific types of exceptions to respond differently to various error conditions.

Example: Division by Zero

Handling a `ZeroDivisionError` when dividing two numbers:

```python
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number to divide by: "))
    result = a / b
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
finally:
    print("Operation attempted.")
# Output:
# If b is 0, "Division by zero is not allowed." If inputs are not valid numbers, "Invalid input. Please enter a valid number."
```

### The finally Block

The `finally` block is executed regardless of whether an exception occurred, making it ideal for performing clean-up actions.

Example: Closing a File

Using `finally` to ensure a file is closed:

```python
file = None
try:
    file = open('example.txt', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found.")
finally:
    if file:
        file.close()
        print("File closed.")
# Output:
# If 'example.txt' is found, its content is printed, followed by "File closed." If not, "File not found." and then "File closed."
```

### The else Block

The `else` block runs if no exceptions were raised in the `try` block.

Example: Successful File Read

Using `else` to execute code only if no exceptions occur:

```python
try:
    file = open('example.txt', 'r')
except FileNotFoundError:
    print("File not found.")
else:
    content = file.read()
    print(content)
    file.close()
# Output:
# If 'example.txt' is found, its content is printed. Otherwise, "File not found."
```

### Using Exceptions in File Handling

Exception handling is particularly useful in file handling scenarios to manage unexpected situations like missing files or permission issues.

Example: Sorting a List from a File

Handling a file to sort a list of items:

```python
try:
    with open('items.txt', 'r') as file:
        items = file.readlines()
        items.sort()
        print(items)
except FileNotFoundError:
    print("File not found.")
# Output:
# Prints the sorted list if 'items.txt' exists. Otherwise, "File not found."
```

## Task Steps

### Part 1: recipe_input.py Script

- Import `pickle` module.
- Define functions for taking recipes and calculating difficulty.
- Use file handling to store recipes in a binary file.

```python
import pickle

# Prints a decorative header for the application
def print_header():
    print("*******************************************************************************************************")
    print("*******************************************************************************************************")
    print("   ______    _______  _______  ___   _______  _______       ___   __    _  _______  __   __  _______   ")
    print("  |    _ |  |       ||       ||   | |       ||       |     |   | |  |  | ||       ||  | |  ||       |  ")
    print("  |   | ||  |    ___||       ||   | |    _  ||    ___|     |   | |   |_| ||    _  ||  | |  ||_     _|  ")
    print("  |   |_||_ |   |___ |       ||   | |   |_| ||   |___      |   | |       ||   |_| ||  |_|  |  |   |    ")
    print("  |    __  ||    ___||      _||   | |    ___||    ___|     |   | |  _    ||    ___||       |  |   |    ")
    print("  |   |  | ||   |___ |     |_ |   | |   |    |   |___      |   | | | |   ||   |    |       |  |   |    ")
    print("  |___|  |_||_______||_______||___| |___|    |_______|     |___| |_|  |__||___|    |_______|  |___|    \n")
    print("*******************************************************************************************************")
    print("*******************************************************************************************************\n")

# Calculates the difficulty level of a recipe
def calc_difficulty(cooking_time, num_ingredients):
    if cooking_time < 10 and num_ingredients < 4:
        return "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        return "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        return "Intermediate"
    else:
        return "Hard"

# Takes a single recipe input from the user
def take_recipe(recipe_num):
    print(f"\n---- Recipe #{recipe_num} ----")

    # Validate recipe name
    while True:
        name = input("Enter your recipe name: ").strip()
        if name:
            break
        print("\nPlease enter a valid recipe name.")

    # Validate cooking time
    while True:
        try:
            cooking_time = int(input("Enter the cooking time (in minutes): "))
            if cooking_time > 0:
                break
            print("\nPlease enter a positive number for the cooking time.")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

    # Validate ingredients
    while True:
        ingredients_input = input("Enter your ingredients, seperated by a comma: ").strip()
        ingredients = [ingredient.strip() for ingredient in ingredients_input.split(",") if ingredient.strip()]
        if ingredients:
            break
        print("\nPlease enter at least one ingredient.")
    
    difficulty = calc_difficulty(cooking_time, len(ingredients))
    return {"name": name, "cooking_time": cooking_time, "ingredients": ingredients, "difficulty": difficulty}

# Main script execution
print_header()
filename = input("Enter the filename to save the recipes: ")

# Load existing data or initialize if file not found
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    data = {"recipes_list": [], "all_ingredients": []}
except Exception as e:
    print(f"An error occured: {e}")
    data = {"recipes_list": [], "all_ingredients": []}

recipes_list, all_ingredients = data["recipes_list"], data["all_ingredients"]

# Collect multiple recipes from the user
n = int(input("\nHow many recipes would you like to enter?: "))
for i in range(1, n+1):
    recipe = take_recipe(i)
    recipes_list.append(recipe)
    for ingredient in recipe["ingredients"]:
        if ingredient not in all_ingredients:
            all_ingredients.append(ingredient)

# Save updated data back to the file
data = {"recipes_list": recipes_list, "all_ingredients": all_ingredients}
    
with open(filename, "wb") as file:
    pickle.dump(data, file)

print("\nRecipes saved successfully!")
```

### Part 2: recipe_search.py Script

- Develop a script to search for recipes based on ingredients.
- Implement error handling for file operations.

```python
import pickle

# Prints a decorative header for the application
def print_header():
    print("********************************************************************************************************************")
    print("********************************************************************************************************************")
    print("   ______    _______  _______  ___   _______  _______       _______  _______  _______  ______    _______  __   __   ")
    print("  |    _ |  |       ||       ||   | |       ||       |     |       ||       ||   _   ||    _ |  |       ||  | |  |  ")
    print("  |   | ||  |    ___||       ||   | |    _  ||    ___|     |  _____||    ___||  |_|  ||   | ||  |       ||  |_|  |  ")
    print("  |   |_||_ |   |___ |       ||   | |   |_| ||   |___      | |_____ |   |___ |       ||   |_||_ |       ||       |  ")
    print("  |    __  ||    ___||      _||   | |    ___||    ___|     |_____  ||    ___||       ||    __  ||      _||       |  ")
    print("  |   |  | ||   |___ |     |_ |   | |   |    |   |___       _____| ||   |___ |   _   ||   |  | ||     |_ |   _   |  ")
    print("  |___|  |_||_______||_______||___| |___|    |_______|     |_______||_______||__| |__||___|  |_||_______||__| |__|  \n")
    print("********************************************************************************************************************")
    print("********************************************************************************************************************\n")

# Displays a single recipe in a readable format
def display_recipe(recipe):
    print(f"\nRecipe: {recipe['name'].title()}")
    print(f"  Time: {recipe['cooking_time']} mins")
    print("  Ingredients:")
    for ingredient in recipe["ingredients"]:
        print(f"  - {ingredient.title()}")
    print(f"  Difficulty: {recipe['difficulty']}")

# Searches for recipes containing a specific ingredient
def search_ingredient(data):
    all_ingredients = data["all_ingredients"]
    print("\n-----------------------")
    print(" Full Ingredients List ")
    print("-----------------------")
    for i, ingredient in enumerate(all_ingredients):
        print(f"{i+1}.) {ingredient.title()}")
    
    # Validate user input for selecting an ingredient
    try:
        while True:
            choice = int(input("\nEnter the number of the ingredient to search: "))
            if 1 <= choice <= len(all_ingredients):
                ingredient_searched = all_ingredients[choice-1]
                break
            print(f"Please enter a number between 1 and {len(all_ingredients)}.")
        
        # Find recipes containing the chosen ingredient
        recipes_with_ingredient = [recipe for recipe in data["recipes_list"] if ingredient_searched in recipe["ingredients"]]
        num_recipes = len(recipes_with_ingredient)

        # Display count of found recipes
        recipe_word = "Recipe" if num_recipes == 1 else "Recipes"

        decoration = "-" * (len(f"{num_recipes} {recipe_word} found containing {ingredient_searched.title()}") + 2)
        print(f"\n{decoration}")
        print(f" {num_recipes} {recipe_word} found containing {ingredient_searched.title()} ")
        print(f"{decoration}")

        # Display each found recipes
        for recipe in recipes_with_ingredient:
            display_recipe(recipe)

    # Handle invalid inputs
    except ValueError:
        print("Invalid input! Please enter a number.")
    except IndexError:
        print("No such ingredient number.")

# Main script execution
print_header()  
filename = input("Enter the filename of your recipe data: ")

# Load data from the file and search for recipes
try:
    with open(filename, "rb") as file:
        data = pickle.load(file)
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
else:
    search_ingredient(data)
```

### Part 3: Final Steps

- Execute both scripts, capture their outputs.
- Store your code, output files, and learning reflections in your GitHub repository.

Image of step 1:

![CMD example of recipe_input.py]()
![CMD example of recipe_search.py]()

## Learning Journal

- The learning journal included reflects on the experience and learning outcomes from this exercise.

## Screenshots

- Two screenshots demonstrating the command-line interface process are included in the repository, named `Recipe_Input.png` and `Recipe_Seach.png`.

## Summary

This exercise equips you with vital skills for file manipulation and error handling in Python, preparing you for more advanced programming challenges and real-world applications.
