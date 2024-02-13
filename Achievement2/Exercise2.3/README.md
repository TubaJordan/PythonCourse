# Exercise 2.3: Django Models and Automated Testing

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Example Project: Bookstore Application](#example-project-bookstore-application)
   - [Database Blueprint](#database-blueprint)
   - [Django App Creation Per Application Requirements](#django-app-creation-per-application-requirements)
   - [Linking Apps to the Bookstore Application](#linking-apps-to-the-bookstore-application)
4. [Django Models: Defining, Registering, Migrating, and Running](#django-models-defining-registering-migrating-and-running)
5. [Working on the Remaining Models](#working-on-the-remaining-models)
   - [Class Definitions](#class-definitions)
   - [Attribute Specification](#attribute-specification)
   - [Code for Defining and Registering Models](#code-for-defining-and-registering-models)
6. [Testing Django Web Applications](#testing-django-web-applications)
   - [Writing Tests](#writing-tests)
   - [Running Tests](#running-tests)
   - [Best Practices](#best-practices)
7. [Task](#task)
8. [Learning Journal](#learning-journal)
9. [Summary](#summary)

## Introduction

Successful creation of a Django project structure, including an app's structure and a superuser for admin panel access, sets the stage for further development focused on the Model (M) aspect of Django's MVT architecture. The model represents the application's backend database, playing a crucial role in defining what the frontend user experiences by establishing database entities, fields, and relationships early in the development process.

Determining the application's functionality, including the number of pages and target users, is essential. This understanding guides the creation of a Django-implementable application outline through the development of database tables (models).

Accessing the database via a localhost browser for further familiarization, and learning to write and run tests, are critical steps to ensure the application performs as intended.

The focus initially is on defining the desired functionality for a hypothetical Bookstore application.

**Note:** In this context, "application" refers to the Django project as a whole, while "app" denotes smaller functional modules within the project.

## Learning Goals

- Design a database schema for a web application.
- Create and configure Django apps within a project.
- Define and implement Django models based on the application's requirements.
- Write and run automated tests to ensure model reliability.
- Apply these concepts to develop a Recipe application, managing recipes and ingredients.

## Django Models

Django models are Python objects that enable web applications to access and manage database data. They determine the data's structure within the database, specifying field types, default values, and the maximum size of the data.

Defining a model involves writing its structure and other necessary code, without the need for direct database communication. Django automates database interactions, utilizing an object-relational mapper (ORM) to manage SQL queries for operations.

Prior to coding Django models, it is important to consider the specific data required for storage in the application's database.

## Example Project: Bookstore Application

The Bookstore application aims to manage and display information such as sales figures, book details, and customer data. Identifying additional information needs, such as inventory or employee records, is crucial before model creation. Questions to consider include:

- Are there other types of information, besides books, customers, and sales, that need management?
- What specific attributes are required for each category, like names and photos for customers?
- How will these categories (tables/apps) interact within the application?

Decisions on these aspects should be solidified early to facilitate smooth development, as changes to models can be complex and disruptive in later stages.

### Database Blueprint

A database blueprint provides a visual outline of the database's structure, including entities, their attributes, and relationships. This planning step helps in understanding the app's data management needs.

For the Bookstore application, essential categories and their attributes might include:

- **Books**: Information on books, such as name, genre, book type (hardcover, eBook, audiobook), price, and an image placeholder for future addition.
- **Salespersons**: Details of sales staff, including username, name, biography, and a photo placeholder.
- **Customers**: Data on customers, including name, notes, and a photo placeholder.
- **Sales**: Records of sales transactions, detailing the book sold, quantity, price, and date.

This information leads to a structured database blueprint, guiding the creation of Django models for each category, such as "Book", "Customer", "Sale", and "Salesperson".

### Django App Creation Per Application Requirements

Following the outlined requirements, Django apps for books, sales, salespersons, and customers are created using the `python manage.py startapp <app_name>` command. These apps are then linked to the main Bookstore application by updating the `INSTALLED_APPS` setting in the project's `settings.py` file, ensuring they are recognized and managed by Django.

**Example Commands**:

- For the sales app: `python manage.py startapp sales`
- For the salespersons app: `python manage.py startapp salespersons`
- For the customers app: `python manage.py startapp customers`

**Tip**: While it's common to create a separate app for each model category, grouping related models into a single app based on functionality is also a viable approach. This can streamline the project's structure, especially for closely related categories.

### Linking Apps to the Bookstore Application

Apps are integrated into the Bookstore project by adding them to the `INSTALLED_APPS` list in `settings.py`. This step is crucial for Django to acknowledge and interact with the apps, enabling features such as the Django admin interface and database migrations for these newly created models.

## Django Models: Defining, Registering, Migrating, and Running

Defining, registering, migrating, and running Django models for the Bookstore application involves a four-step process:

1. **Defining the Model**: Specify the table as a class within the models.py file. For instance, the Customer class for the customers app might include attributes like name and notes, represented by CharField and TextField, respectively.

    ```python
    class Customer(models.Model):
        name = models.CharField(max_length=120)
        notes = models.TextField()

        def __str__(self):
            return self.name
    ```

    Ensure correct usage of tabs and spaces for indentation to avoid formatting errors.

2. **Registering the Model**: In the admin.py file of the app, import and register the model class to make it accessible from the Django admin interface.

    ```python
    from .models import Customer

    admin.site.register(Customer)
    ```

3. **Migration**: Migrate the model to create the corresponding table in the database. This step involves running `makemigrations` to package model changes and `migrate` to apply these changes.

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

4. **Run Server**: Start the Django server to interact with the models through the admin interface.

    ```shell
    python manage.py runserver
    ```

Navigate to `http://127.0.0.1:8000/admin/` to see and interact with the newly defined models, such as adding or viewing customers.

This process ensures that the Customer class is successfully translated into a table within the database, with `name` and `notes` as columns, and each instance of the class representing a row in the table.

## Working on the Remaining Models

For the remaining models, the process of defining, registering, migrating, and running follows the same steps as described for the Customer model. The summary tables below consolidate the class definitions and attributes for each model in the project.

### Class Definitions

| App          | App/Filename                | Class Definition                    | Table        |
|--------------|-----------------------------|-------------------------------------|--------------|
| customers    | customers/models.py         | class Customer(models.Model):       | Customer     |
| books        | books/models.py             | class Book(models.Model):           | Book         |
| salespersons | salespersons/models.py      | class Salesperson(models.Model):    | Salesperson  |
| sales        | sales/models.py             | class Sale(models.Model):           | Sale         |

### Attribute Specification

Attributes for each class/model are defined within their respective models.py files, detailing the structure and data types of each table in the database.

### Code for Defining and Registering Models

Models defined in the models.py files need to be registered in the admin.py files within each app to make them accessible via the Django admin interface. This involves importing the model class and using the `admin.site.register(ModelClass)` syntax.

### Implementation Steps

1. **Define models**: Specify the structure of your database tables in models.py.
2. **Register models**: Make models accessible in the Django admin by registering them in admin.py.
3. **Migrate**: Apply model changes to the database with `makemigrations` and `migrate`.
4. **Run server**: Start the Django server and navigate to the admin interface to interact with the models.

After completing these steps for all models, the Django admin interface will display all defined models, allowing for data management tasks such as creating, viewing, editing, and deleting records.

This completes the model ("M") component of the Django MVT (Model-View-Template) architecture. The application now has a structured database with models representing the various entities required for the project.

Next, adding tests for the application is crucial to verify functionality and ensure reliability.

## Testing Django Web Applications

Automated tests play a crucial role in uncovering and preventing bugs in applications, offering numerous benefits:

- **Time-saving**: Automated testing reduces the need for manual verification as the application grows, allowing developers to concentrate on development.
- **Preventative measure**: By considering actual requirements and expected outcomes, tests help identify and prevent potential issues during development.
- **Increased coverage**: Tests can comprehensively cover minute and critical functionalities of the app that might be missed otherwise.
- **Reliability**: Thorough testing enhances the trustworthiness of the code, which is particularly valuable in team settings.
- **Strength testing**: Ensures the code's resilience against unintentional breaks caused by future changes.
- **Documentation**: Acts as documentation for the application's intended behavior, guiding development and maintenance.

### Writing Tests

Django provides a structured approach to testing, with a `tests.py` file in each app for writing test cases. These tests aim to verify the accuracy of variables, functions, and the application's logic.

```python
from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(name='Pride and Prejudice', price=23.71)

    def test_book_name(self):
        book = Book.objects.get(id=1)
        expected_name = 'Pride and Prejudice'
        self.assertEqual(book.name, expected_name)
```

### Running Tests

Execute tests with the `manage.py test` command, which provides feedback on each test case's outcome:

```shell
python manage.py test
```

Django supports running specific tests to target particular areas of the application, with options like `--verbosity` for adjusting output detail.

### Best Practices

- **Start early**: Incorporate testing early in the development to catch and address bugs promptly.
- **Automate**: Use Django's testing framework to automate testing processes wherever possible.
- **Document**: Leverage tests as a form of documentation to outline expected application behavior.
- **Continuously test**: Regularly add new tests as the application evolves to cover new features and prevent regressions.

Testing is integral to Django development, ensuring the application functions as expected and remains robust through its development lifecycle.

## Task

Apply the learning from this exercise to the Recipe application, enabling users to create, input, and search recipes by ingredients. Review the Project Brief for high-level application requirements.

1. **Create a folder** named "Exercise 2.3" for task outputs.

2. **Create database blueprint**:
   - Consider information categories (entities) in the Recipe application. Identify attributes and relationships.
   - Draw the schema using a preferred tool or on paper.
   - Save the schema image in "Exercise 2.3" as "recipe-app-schema.jpg".
![Database Blueprint](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement2/Exercise2.3/Screenshots/recipe-app-schema.png)

3. **Create Apps**:
   - With the schema ready, prepare to structure the web application. In the src folder within VSCode's terminal:
     - Use `startapp` command to create project apps.
     - Update the `settings.py` to link new apps to `INSTALLED_APPS`.
     - Screenshot the VSCode structure showing apps and `settings.py`, saving it as "project-structure.jpg" in "Exercise 2.3".
![Create Apps](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement2/Exercise2.3/Screenshots/project-structure.png)

4. **Create Models**:
   - Based on the blueprint, define models in the `models.py` files. Include fields and `__str__` methods.

5. **Register Models**:
   - In `admin.py` of each app, register the created models to make them accessible in Django admin.

6. **Migrate**:
   - Execute `makemigrations` and `migrate` to create database tables from models.
   - Capture a screenshot post-migration as "run-migrations.jpg".
![Run Migration](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement2/Exercise2.3/Screenshots/run-migrations.png)

7. **Write Tests**:
   - Implement tests for the models. (insert example here)
   - Run tests, fix any failures, and repeat until all pass.
   - Save the test report as "Test-Report.jpg".
![Test Report](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement2/Exercise2.3/Screenshots/Test-Report.png)

8. **Run Server**:
   - Start the server and access the admin panel using superuser credentials.

9. **Add Data**:
   - Add at least five recipes via Django admin.
   - Save and name screenshots appropriately in "Exercise 2.3".
![Recipes Added](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement2/Exercise2.3/Screenshots/All-recipes.png)

10. **Upload to GitHub**:
    - Place "Exercise 2.3" in the "Achievement 2" folder in your GitHub repository.
    - Create a "recipe-app" repository and push the `src` folder's code. Include a `.gitignore` file.
    - Add a README with an introduction to the Recipe application.
11. **Share GitHub Links**:
    - Submit "Exercise 2.3" and "recipe-app" repository links for review.

## Learning Journal

- The included learning journal reflects on the experiences and learning outcomes from this exercise.

## Summary

Congratulations on completing this exercise, where the focus was on the critical planning stages for the backend structure of a web application. Instead of diving straight into coding, the importance of drafting a detailed outline for the final product was emphasized. This preparation involves pinpointing the application's basic flow, the objectives of its pages and subpages, its intended users, and other essential elements. The process of how this planned structure translates into Django, through the use of models and the integration of apps into the application, was explored. Additionally, the significance of testing was highlighted, alongside instructions on creating and running tests for the application.

Looking ahead, the next exercise will delve into Django views and templates, representing the V and T in Django's MVT (Model-View-Template) architecture. Now is the opportune moment to apply the knowledge gained from this exercise. The forthcoming task involves developing models for the Recipe application and crafting tests for these models. Ready to proceed? Let's embark on the next phase of development!
