# Exercise 2.2: Django Project Set Up

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Django Terminologies](#django-terminologies)
4. [Creating a Django Project Structure](#creating-a-django-project-structure)
5. [Deploying Your Project](#deploying-your-project)
6. [Creating a Django App Structure](#creating-a-django-app-structure)
7. [Django Admin](#django-admin)
8. [Summary](#summary)
9. [Resources](#resources)
10. [Task](#task)
11. [Forum](#forum)

## Introduction

This exercise is a continuation of the journey into web development using Django. After setting up Django in the previous exercise, the focus here is on creating a Django project structure and exploring key terminologies. A hypothetical bookstore application will be developed for hands-on experience.

## Learning Goals

- Understand and describe the basic structure of a Django project.
- Differentiate between Django projects and apps.
- Create and run a Django project locally.
- Create a superuser in the admin interface of a Django web application.

## Django Terminologies

Understanding terminologies in Django development is fundamental to navigating the framework. This section focuses on clarifying two key concepts: project and app.

### Project and App

A Django project represents a complete application structure. It encompasses multiple modules (referred to as apps), configuration files, and a database. The project's name usually reflects the overall application, such as 'Bookstore' for a bookstore management system. Within this project structure, several modular components, or apps, each serve specific functions. For instance, in the Bookstore project, distinct apps could be responsible for managing sales, handling customer interactions, and generating reports. These apps embody Django's "Don’t Repeat Yourself" (DRY) philosophy, promoting efficiency through modular and reusable code.

### Clarification of Terms

- **Application:** Refers to the overall program or project, like the comprehensive Recipe application.
- **App:** Denotes the individual modules within a Django project.

### Example: CareerFoundry Website

In practical terms, consider a website like CareerFoundry. The entire website constitutes a Django project, with individual sections like login, courses, online events, and blogs representing separate apps. Each app serves a distinct purpose, such as the login app enabling user authentication.

### App Reusability Across Projects

Django's flexibility allows for the reuse of apps across different projects. For example, one project might use an app for user authentication, which could be seamlessly integrated into another project with similar requirements.

### Configuration Files and Database

Each Django project includes configuration files and a database. Configuration files manage a variety of project functions:

- Admin login interfaces
- Global and module-specific variables
- Connections between different views and templates

Django typically uses SQLite3 as the default database, but it also supports MySQL and PostgreSQL, configurable in the `settings.py` file.

### Interaction Within a Project

In a Django project, apps interact with each other, with the database, and with configuration files. For instance, in the Bookstore application:

- Each app corresponds to a database table, facilitating app-database interactions.
- Apps like reports and customers might interact to display results.
- Configuration files dictate which database is created and how apps are linked.

### Example: Train Ticketing and Healthcare Management Systems

To illustrate, consider two distinct projects developed by the same team: a Train Ticketing System (TTS) and a Healthcare Management System (HMS). Each system has unique apps for their specific functionalities, like schedule management in TTS and patient appointments in HMS. However, both systems might share a common login app, demonstrating Django's capability for code reusability. This shared app, however, does not imply direct interaction between the two projects; it's a testament to Django's efficiency in development.

In summary, Django's project and app structure, along with its configuration management, allow for efficient, modular, and scalable web application development, where code reuse is a key feature. Understanding these terminologies and interactions lays a strong foundation for efficient web development using Django.

## Creating a Django Project Structure

This section details the process of structuring a Django project, using a new example project named 'CityGuide'. Key commands and files within the Django framework are introduced to give a clear picture of the project setup.

### Initial Setup

To start building the 'CityGuide' project:

1. Open the preferred code editor, such as VSCode, and access the terminal.
2. If using VSCode, access the integrated terminal by selecting 'New Terminal' from the Terminal menu. Alternatively, any standard terminal or command line interface can be used.

### Activating the Virtual Environment

Before beginning project development, activate the previously set up virtual environment. This ensures the project dependencies are isolated and managed effectively. Use the appropriate command for the operating system:

- **Mac/Linux:** `$ source web-dev/bin/activate`
- **Windows:** `web-dev\Scripts\activate.bat`

### Creating the Project

Create the 'CityGuide' project by executing the following command:

- **Mac/Linux/Windows:** `$ django-admin startproject cityguide`

This command utilizes `django-admin`, Django's command-line utility for administrative tasks, to create a new directory named 'cityguide', which forms the base of the project.

### Navigating the Project Structure

After running the command, the project directory 'cityguide' will contain the following files and subdirectories:

```lua
cityguide/
|-- cityguide/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- manage.py
```

- `manage.py`: A command-line utility that lets you interact with the Django project in various ways. It is a thin wrapper around `django-admin`.
- `cityguide/`: The inner directory is the actual Python package for the project.

### Key Files in the Project

- `__init__.py`: An empty file that tells Python that this directory should be considered a Python package.
- `settings.py`: Contains settings for the Django project, including database configuration, installed apps, and other configurations.
- `urls.py`: Defines the URL declarations for the Django project; a “table of contents” for the web application.
- `wsgi.py` and `asgi.py`: Serve as entry-points for WSGI-compatible web servers and ASGI-compatible servers respectively.

### Renaming the Project Directory

To avoid confusion, the outer directory 'cityguide' can be renamed to something more generic like 'src'. This is done using the command:

- `$ mv cityguide src` (modify for the appropriate OS)

### Running Basic Commands

With `manage.py`, several administrative tasks can be performed. Some common commands include:

- `check`: Checks the project for any issues.
- `migrate`: Applies database migrations.
- `runserver`: Starts a development server.
- `startapp`: Creates a new Django app within the project.

By following these steps, the basic structure of a Django project, in this case, 'CityGuide', is established. The process involves setting up the project directory, understanding the purpose of key files, and renaming the project directory for clarity. This foundational setup is crucial for the efficient development of Django applications.

## Deploying Your Project

After establishing the 'CityGuide' project structure, the next step involves setting up and running the project locally. This process enables viewing the web application through a browser via a local development server. Deployment in Django involves two critical steps: running migrations and starting the server.

### Running Migrations

Migrations in Django refer to changes in the database schema. These are crucial for creating necessary database tables, essentially preparing the backend for the application. Changes to the database or data models will require subsequent migrations.

For the 'CityGuide' project, using Django's default SQLite database:

1. Run migrations by executing the command in the terminal within the 'src' directory.
    - Mac/Linux: `$ python manage.py migrate`
    - Windows: `py manage.py migrate`

Executing this command applies migrations and results in the creation of a `db.sqlite3` file in the 'src' directory. This file represents the project's database.

### Running the Server

Django includes a lightweight development server to test the project during development.

1. Start the server to deploy the 'CityGuide' application locally.
    - Mac/Linux/Windows: `$ python manage.py runserver`

By default, the server runs on port 8000. Access the application by navigating to `http://127.0.0.1:8000/` in a web browser. A successful launch displays Django's default landing page, confirming that the server is operational.

### Project Structure Post-Migration

The project directory 'src' now includes the following:

```lua
src/
|-- cityguide/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- db.sqlite3
|-- manage.py
```

With these steps, the 'CityGuide' Django project is successfully set up and running locally. Migrations prepare the database, and the development server allows for real-time testing and interaction with the application. This setup forms the basis for further development, including the creation of specific apps within the project.

## Creating a Django App Structure

In the 'CityGuide' project, multiple apps are essential for handling different functionalities of the city guide application. Django's design supports the creation of standalone apps, which can be repurposed or shared across different projects. This modular approach is exemplified in Django's own structure, with prebuilt features like authentication, administration, and session management being implemented as apps.

### Creating the First App

For 'CityGuide', the first app to be created could be 'Places', focusing on various places of interest in the city. To initiate this:

1. Stop the running server in the terminal using Ctrl+C. On some systems, Ctrl+Shift+C or Ctrl+Break may be needed.
2. Navigate to the 'src' directory in the terminal.
3. Run the command to create the 'Places' app:
    - Mac/Linux: `$ python manage.py startapp places`
    - Windows: `py manage.py startapp places`

### Structure of the 'Places' App

The creation of the 'Places' app results in a new directory within the 'src' folder, structured as follows:

```lua
src/
|-- places/
|   |-- migrations/
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- cityguide/
|   |-- ...
|-- db.sqlite3
|-- manage.py
```

- `migrations/`: Houses migration files for the app.
- `__init__.py`: Marks the directory as a Python package.
- `admin.py`: Used for administrative tasks related to the app.
- `apps.py`: Contains the app configuration.
- `models.py`: Defines the database models for the app.
- `tests.py`: Hosts unit tests for the app's components.
- `views.py`: Responsible for rendering templates and handling the app's logic.

### Integration with the Admin Panel

With the 'Places' app created, the next step is to integrate it with Django's admin panel for tasks like managing data and modifying records. This integration is facilitated through `admin.py` in the app's directory.

The creation of the 'Places' app within the 'CityGuide' project exemplifies Django's app-centric architecture. Each app serves a specific function and is equipped with the necessary components for independent operation. This approach enhances the modularity and reusability of code within Django projects.

## Django Admin

Django's admin interface is a key feature, providing a user-friendly platform for database administration. Accessible via the local server URL, it allows for essential database operations like adding, modifying, and deleting records. This interface also facilitates user management tasks, including creating users, modifying passwords, and setting access rights. Essentially, the Django admin is a built-in module for managing application-related administrative tasks.

### Creating a Superuser and Logging In

For comprehensive administrative access to the 'CityGuide' application, creating a superuser account is essential. This superuser holds the highest level of permissions, enabling full CRUD (create, read, update, delete) capabilities on the application's database. Managing other users and updating their access rights also fall under the superuser's purview.

#### Steps to Create a Superuser

1. **Creating the Superuser**:
    - From the 'src' directory within the virtual environment, execute the command:
        - `python manage.py createsuperuser`
    - During this process, specify a username, email address, and password. The username can default to the machine's username if left blank.

2. **Running the Server**:
    - After the superuser is created, restart the server to activate the admin functionalities.

3. **Logging into Django Admin**:
    - Access the Django admin login page by appending `admin/` to the local server URL (`http://127.0.0.1:8000/admin/`).
    - Log in using the superuser credentials.

#### Interacting with the Admin Interface

Once logged in, the Django admin page presents various options:

- **User Management**: View and manage the list of users, including the newly created superuser.
- **App Integration**: Interface with the 'Places' app within 'CityGuide' for data management.

Setting up the Django admin for the 'CityGuide' project, including the creation of a superuser, is a critical step in establishing robust control over the application. This process allows for effective management of the application's backend and user permissions. With the admin interface set up, the project is now equipped with powerful tools for ongoing management and development.

## Task

### Task Introduction

This task involves setting up and configuring a new Django project named 'A2_Recipe_App'. The process includes creating a dedicated project directory, establishing a virtual environment, installing Django, and initiating the Django project. Key steps include renaming the project directory for clarity, running migrations, and launching a development server to ensure the project is operational. Additionally, a Django superuser account is created for administrative access. The final part of the task focuses on organizing and preparing the project for submission, including capturing necessary screenshots and updating the project's GitHub repository.

### Execution Steps

1. **Create Project Directory**:

- Create a new folder named 'A2_Recipe_App'.

2. **Set Up Virtual Environment**:

- If the 'web-dev' virtual environment is active, deactivate it.
- Create and activate a new virtual environment 'a2-ve-recipeapp':

```bash
python -m venv a2-ve-recipeapp
source a2-ve-recipeapp/bin/activate  # On Mac/Linux
a2-ve-recipeapp\Scripts\activate     # On Windows
```

3. **Install Django**:

- Within the 'a2-ve-recipeapp' environment, install Django:

```bash
pip install django
```

4. **Create Django Project**:

- In 'A2_Recipe_App', create a Django project named 'recipe_project':

```bash
django-admin startproject recipe_project
```

- Directory structure before renaming:

```lua
A2_Recipe_App/
|-- recipe_project/
|   |-- recipe_project/
|   |-- manage.py
```

5. **Rename Project Directory**:

- Rename the 'recipe_project' directory to 'src':

```bash
mv recipe_project src  # On Mac/Linux
rename recipe_project src  # On Windows
```

- Directory structure after renaming:

```lua
A2_Recipe_App/
|-- src/
|   |-- recipe_project/
|   |-- manage.py
```

6. **Run Migrations and Server**:

- Inside 'src', apply migrations and start the Django server:

```bash
cd src
python manage.py migrate
python manage.py runserver
```

7. **Create Superuser**:

- Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

- Follow prompts to set username, email, and password.

8. **Access Admin Dashboard**:

- Navigate to `http://127.0.0.1:8000/admin/` in a web browser and log in with superuser credentials.

This task walkthrough demonstrates the process of setting up a new Django project, running it locally, creating a superuser, and preparing the project for submission. Each step is executed with precision, ensuring the project is ready for further development and review.

## Learning Journal

- The included learning journal reflects on the experiences and learning outcomes from this exercise.

## Summary

In this exercise:

1. **Django Terminology:** Key concepts like 'project' and 'app' were clarified, emphasizing Django's modular structure where projects consist of multiple functional apps.

2. **Project Setup:** A Django project, 'CityGuide', was set up, highlighting essential files and configurations fundamental to Django projects.

3. **App Development:** The 'Places' app within 'CityGuide' demonstrated how apps are structured and function within a Django project.

4. **Django Admin Interface:** Creation and usage of a superuser account were covered, showcasing Django's capabilities for database and user management.

5. **Local Deployment:** The exercise included deploying the 'CityGuide' project locally, illustrating the use of Django's development server for testing.

The next exercise will delve into the 'model' part of Django's MVT architecture, focusing on backend database creation and management.
