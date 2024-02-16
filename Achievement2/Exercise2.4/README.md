# Exercise 2.4: Django Views and Templates

## Table of Contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Views and Templates](#views-and-templates)
4. [Creating a Custom Welcome Page](#creating-a-custom-welcome-page)
    - [Understanding the Files and Folder Structure](#understanding-the-files-and-folder-structure)
5. [Files and Folders, the Django Way](#files-and-folders-the-django-way)
    - [Directory and File Setup for the Blog App](#directory-and-file-setup-for-the-blog-app)
6. [Django Views and Templates](#django-views-and-templates)
    - [Function-Based Views (FBV) vs. Class-Based Views (CBV)](#function-based-views-fbv-vs-class-based-views-cbv)
    - [Implementing Views and Templates in the Blog App](#implementing-views-and-templates-in-the-blog-app)
7. [Task](#task)
8. [Summary](#summary)

## Introduction

Exercise 2.4 shifts focus from the model (M) side of Django's MVT (Model-View-Template) architecture to the frontend, exploring views (V) and templates (T). The lesson guides through creating views, templates, and managing URLs to enable frontend page creation for web applications.

## Learning Goals

- Summarize the process of creating views, templates, and mapping URLs in Django projects.
- Explain the concepts of "V" and "T" in Django's MVT architecture.
- Implement custom welcome pages for web applications.

## Views and Templates

Views serve as the logic layer in Django that gets executed upon a URL request by a user. Each view can be either a Python function or a method within a Python class. These views process incoming requests, execute the defined logic, and return a response. Responses from views can vary from simple static data, such as an HTML page or JSON data, to more complex interactions involving database queries and user input processing.

Templates are associated with views to define the structure of the output. Typically, templates are text files in formats like HTML, XML, or CSV, which outline how the data returned by the view should be presented to the user. Django maps views to URLs using a URL configuration, enabling the application to serve different content for different URLs based on the defined logic.
Example Scenario:

Consider a basic blog application. The application has a URL pattern `/articles/` that is mapped to a view named `article_list`. This view queries a database to retrieve a list of articles and passes this list to a template named `article_list.html`. The template renders the list of articles in a structured format for display in the user's browser.

```python
# views.py
from django.shortcuts import render
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})
```

In the URL configuration, the path to this view is defined, linking the URL pattern to the view function.

```python
# urls.py
from django.urls import path
from .views import article_list

urlpatterns = [
    path('articles/', article_list, name='article_list'),
]
```

The template `article_list.html` might look something like this:

```html
<!-- article_list.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Blog Articles</title>
</head>
<body>
    <h1>Articles</h1>
    <ul>
        {% for article in articles %}
            <li>{{ article.title }} by {{ article.author }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

This example demonstrates how Django processes a request for the `/articles/` URL, executes the `article_list` view to fetch articles from the database, and uses the `article_list.html` template to format and display the articles to the user. The seamless integration between URLs, views, and templates forms the foundation of content delivery in Django applications.

## Creating a Custom Welcome Page

Replacing Django's default welcome page with a custom homepage involves a structured approach that integrates views, URLs, and templates within an application. The customization process encompasses four main steps:

1. **Defining the View**: This involves creating a function or class in the `views.py` file within the application directory. This view function or class is responsible for processing incoming requests and returning the appropriate response, typically rendering a template with context data.

2. **Creating the Template(s)**: Templates are created within the `app/templates/` directory. These HTML files define the structure and layout of the webpage. The template should be placed in a directory named after the app within the templates folder to avoid naming conflicts with templates from other apps.

3. **Mapping the URL to View**: The `urls.py` file within the application directory is used to define URL patterns that Django uses to match incoming requests to the correct view. This step involves creating a URL pattern that, when matched, triggers the execution of the associated view function or class.

4. **Registering the URL and View**: Finally, the application's `urls.py` file must be included in the project's main `urls.py` file. This is done by using Django's `include` function, which incorporates the application's URL configurations into the project's overall URL structure.

### Understanding the Files and Folder Structure

Django projects adhere to a specific directory structure, known as the Django way of organizing files and folders. This structure includes predefined locations for models (`models.py`), views (`views.py`), templates (`templates/`), and URL configurations (`urls.py`), among others. This organization ensures a consistent development environment across different Django projects, facilitating code maintenance and understanding by different developers.

For example, to create a custom homepage for a blog application, one might:

- Define a view in `blog/views.py` that retrieves recent posts from the database.
- Create a template `blog/templates/blog/home.html` that formats these posts into an HTML page.
- Map a URL pattern in `blog/urls.py` to this view, such as `path('', views.home, name='home')`.
- Include `blog/urls.py` in the project's main `urls.py` file with `path('blog/', include('blog.urls'))`.

This structured approach not only allows for the customization of the homepage but also promotes modularity and reusability of components across the Django project. While some developers may find this structure limiting, it provides a clear and standardized method for web application development.

## Files and Folders, the Django Way

Django enforces a structured approach for organizing files and pathways within projects. This section provides insights into setting up a custom homepage within a hypothetical "Blog" application, exemplifying Django's directory and file organization standards.

### Directory and File Setup for the Blog App

1. **blog/views.py**: This file is pivotal for defining the application's logic. It contains functions or class methods that process web requests and generate responses. These responses could range from rendering an HTML template to returning JSON data, depending on the request's nature.

    **Directory Structure for the Blog App**:

    ```plaintext
    blog
    ├── __init__.py
    ├── __pycache__
    ├── admin.py
    ├── apps.py
    ├── migrations
    ├── models.py
    ├── tests.py
    └── views.py
    ```

    > **Note**: The `__pycache__` directory is generated automatically to enhance execution speed. It's not Django-specific and can be safely ignored. It will regenerate if removed.

2. **blog/templates/**: This directory is specifically created within the blog app to store its HTML templates. Proper organization here ensures Django can find and render the correct template when a view is called.

    ```plaintext
    blog
    ├── ...
    └── templates
        └── blog
            └── home.html
    ```

    Steps include:
    - Creating a `templates` directory within the blog app.
    - Making a subdirectory within `templates` named after the app (`blog`).
    - Placing the `home.html` template within this subdirectory.
    - Referencing `blog/home.html` in `views.py` directs Django to this template for response rendering.

3. **blog/urls.py**: This file is essential for defining the URL-to-view mappings within the blog app. It outlines how URLs correspond with specific view functions or class methods.

    ```plaintext
    blog
    ├── ...
    ├── templates
    │   └── blog
    ├── tests.py
    ├── urls.py
    └── views.py
    ```

    > **Note**: This example demonstrates URL registration within the app, but it's also feasible to manage URL configurations at the project level.

4. **bookstore/urls.py**: To integrate the blog app's URLs with the wider project, the `urls.py` file in the `bookstore` directory must be updated to include the blog's URL patterns.

    **Project Directory Overview**:

    ```plaintext
    src
    ├── blog
    │   ├── ...
    │   └── views.py
    └── bookstore
        ├── ...
        ├── urls.py
        └── wsgi.py
    ├── db.sqlite3
    └── manage.py
    ```

The primary method organizes templates within their respective app directories, promoting clarity and modularity. An alternative approach places templates in a shared location at the project level, impacting naming conventions and reusability. Regardless of the chosen method, ensuring cohesive management between views and templates is crucial for a well-organized Django project.

## Django Views and Templates

After understanding the key files and their purposes, it's time to craft the initial view: the welcome page for the Blog application. Django supports two primary types of views: Function-Based Views (FBV) and Class-Based Views (CBV), each with distinct advantages.

### Function-Based Views (FBV) vs. Class-Based Views (CBV)

- **FBVs** are straightforward, defined as Python functions. They are ideal for scenarios requiring customized logic, offering simplicity and readability. However, FBVs may involve more boilerplate code and can be less efficient for reuse across different parts of a project.

- **CBVs** leverage Python classes to define views, enhancing reusability and extension. They streamline code by reducing duplication but can be more complex to understand and implement initially.

The choice between FBVs and CBVs depends on project needs. CBVs are advantageous for generic views across multiple apps, minimizing code duplication. In contrast, FBVs offer flexibility for unique views with specific logic.

### Implementing Views and Templates in the Blog App

1. **Defining the View**:

   In `blog/views.py`, start by importing Django's `render` function:

   ```python
   from django.shortcuts import render
   ```

   Define a `home` function to handle requests and render the homepage:

   ```python
   def home(request):
       return render(request, 'blog/home.html')
   ```

   This function processes incoming web requests and returns the `home.html` template as the response.

2. **Creating the Template**:

   Templates should be organized within the app for clarity. For the Blog app, create a `home.html` template in `blog/templates/blog/`. This structure ensures Django correctly identifies and renders the template.

   **Directory Structure**:

   ```plaintext
   blog
      └── templates
          └── blog
              └── home.html
   ```

   The `home.html` might contain basic HTML to welcome users:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>Blog Home</title>
   </head>
   <body>
       <h1>Welcome to the Blog</h1>
   </body>
   </html>
   ```

3. **Mapping View to URL**:

   Define the URL pattern in `blog/urls.py` to connect the homepage route with the `home` view:

   ```python
   from django.urls import path
   from .views import home

   urlpatterns = [
       path('', home, name='home'),
   ]
   ```

4. **Registering the URL and View**:

   Include the Blog app's `urls.py` in the project's main `urls.py` to make the homepage accessible:

   ```python
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('blog.urls')),
   ]
   ```

Running the server (`python manage.py runserver`) and visiting `http://127.0.0.1:8000/` should now display the custom Blog homepage, marking the successful creation and integration of the first view and template.

## Task

### Directions

1. **Load Project**:

   In VSCode, open the A2_Recipe_App/src folder.

2. **Create the view**:
   Pick the app where you want to create the view. Navigate to `recipes/views.py` and define the view. Save the file.

   > **Note**
   > You can select any of the apps to create the home view. However, if you later plan to show data from your database on your homepage, it’ll be a good idea to use the same app, because then the model and view will be able to interact easily.

3. **Create template**:
   a. Create a templates folder under `recipes`.
   b. Create a folder named `recipes` under the newly created templates folder.
   c. Create an HTML file to define your template. Name the file `recipes_home.html`. Be careful to specify the correct template path in the `recipes/views.py` file.
   d. The HTML file is currently empty. Design a welcome page using desired elements and HTML blocks in the `recipes_home.html` file. Save it.

4. **Map view to URL**:
   As this is the welcome page, you’ll want it to appear when the main site (“<http://127.0.0.1:8000/”>) loads. For this:
   a. Create a `urls.py` file in the `recipes` folder.
   b. Specify the path in `recipes/urls.py` to connect the route corresponding to “<http://127.0.0.1:8000/”> with the view specified by `recipes/views.py`. Ensure you import the necessary packages and specify the app name. Save the file.
   c. Update the `urls.py` file in your main recipe project by registering the view to `urlpatterns`. Ensure you import the necessary packages to include the app. Save the file.

5. **Run Server**:
   a. Navigate to A2_Recipe_App/src.
   b. Activate the virtual environment: a2-ve-recipeapp.
   c. Run the server.

6. **Load site in browser**:
   Copy the link to your app and paste it into the browser. You should see your custom welcome page. Take a screenshot of the homepage and save it as “welcome.jpg”.
   ![Welcome Screenshot](https://github.com/TubaJordan/PythonCourse/blob/main/Achievement2/Exercise2.4/screenshots/welcome.jpg)

7. **Upload screenshot to GitHub**:
   a. Create a folder named “Exercise 2.4” within your “Achievement 2” folder on GitHub.
   b. Create a “screenshots” folder within “Exercise 2.4” and upload the “welcome.jpg” screenshot to it.

8. **Upload code to GitHub**:
   Push your code in the src folder to the recipe-app GitHub repository that you’ve already created.

9. **Share links**:
   Share the links to your “Exercise 2.4” GitHub folder and the recipe-app GitHub repository with your tutor for review.

## Summary

The lesson covers fundamentals of creating views and templates in Django, guiding through the process of creating a custom welcome page. It includes learning about Django's structured file and folder system, differences between FBVs and CBVs, and mapping URLs to views.
