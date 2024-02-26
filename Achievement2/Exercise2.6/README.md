# Exercise 2.6 User Authentication in Django

## Table of contents

1. [Introduction](#introduction)
2. [Learning Goals](#learning-goals)
3. [Users and Authentication](#users-and-authentication)
   - [Introduction to Django's User Model](#introduction-to-djangos-user-model)
   - [Setting Up User Authentication](#setting-up-user-authentication)
4. [Creating a User Login Page](#creating-a-user-login-page)
   - [Implementing the Login View](#implementing-the-login-view)
   - [Designing the Login Template](#designing-the-login-template)
5. [Implementing Logout Functionality](#implementing-logout-functionality)
   - [Creating the Logout View](#creating-the-logout-view)
6. [Integrating Authentication into the Blog Application](#integrating-authentication-into-the-blog-application)
   - [Restricting Access to Views](#restricting-access-to-views)
   - [Displaying User-Specific Information](#displaying-user-specific-information)
7. [Links to Login and Logout](#links-to-login-and-logout)
   - [Implementing Clickable Login and Logout Links](#implementing-clickable-login-and-logout-links)
     - [Adding a Login Link](#adding-a-login-link)
     - [Integrating a Logout Link](#integrating-a-logout-link)
8. [Protecting Views](#protecting-views)
   - [Configuration in Settings](#configuration-in-settings)
   - [Securing Views](#securing-views)
9. [Task](#task)
   - [Overview](#overview)
   - [Directions](#directions)
10. [Learning Journal](#learning-journal)
11. [Summary](#summary)

## Introduction

This lesson extends the Django application development by introducing user authentication features. It aims to equip the application with functionality accessible only to registered users, enhancing security and personalization.

## Learning Goals

- Understand the creation and management of user authentication in Django.
- Familiarize with GET and POST methods for handling form submissions.
- Learn to password-protect views and restrict access to authenticated users.

## Users and Authentication

### Introduction to Django's User Model

Django comes equipped with a powerful user authentication system, simplifying user management. The `User` model stores information such as usernames, passwords, and email addresses.

### Setting Up User Authentication

To add authentication to the blog application, start by creating users through the Django admin panel. This enables the differentiation of content and functionality for guests versus logged-in users.

## Creating a User Login Page

### Implementing the Login View

For the blog application, define a `login_view` in `views.py`:

```python
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('blog_home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})
```

This view uses Django’s `AuthenticationForm` to authenticate users, redirecting authenticated users to the blog's homepage.

### Designing the Login Template

Create `login.html` in `templates/auth` to present the login form:

```html
{% extends "base.html" %}

{% block content %}
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
{% endblock %}
```

This template extends a base template and includes Django's CSRF token for security.

## Implementing Logout Functionality

### Creating the Logout View

In `views.py`, add a simple view for logging out users:

```python
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('login_view')
```

This function logs out users and redirects them to the login page.

## Integrating Authentication into the Blog Application

### Restricting Access to Views

Modify blog views to restrict access to authenticated users by using the `login_required` decorator:

```python
from django.contrib.auth.decorators import login_required

@login_required
def post_create_view(request):
    # View logic here
```

### Displaying User-Specific Information

In your blog templates, use the `request.user` object to display user-specific information, such as a welcome message:

```html
{% if user.is_authenticated %}
<p>Welcome, {{ user.username }}!</p>
{% else %}
<p>Welcome, guest!</p>
{% endif %}
```

This example shows how to personalize the blog's header based on the user's authentication status.

## Links to Login and Logout

This section elaborates on integrating single-click login and logout options within the blog application, enhancing user interaction by providing straightforward access to these functionalities.

### Implementing Clickable Login and Logout Links

#### Adding a Login Link

The addition of interactive links for login and logout is best accomplished within templates, as these elements contribute to the user interface.
Example: Implementing a Login Link

In the context of the blog application, consider adding a login link to the homepage. This can be achieved by modifying the home.html template within the blog app.

Before Addition:

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>Blog Home</title>
</head>
<body>
    <h1>Welcome to Our Blog</h1>
    <img src="{% static 'blog/images/welcome.jpg' %}" alt="Welcome" width="600" height="300">
</body>
</html>
```

Adding the Login Link:

To provide a direct link to the login page, insert the following line within the `<body>` section:

```html
<a href="{% url 'login' %}">Login</a>
```

The `{% url %}` template tag dynamically resolves to the URL associated with the `login` view, directing users to the login form upon interaction.

After Addition:

```html
{% load static %}

<!DOCTYPE html>
<html>
<head>
    <title>Blog Home</title>
</head>
<body>
    <h1>Welcome to Our Blog</h1>
    <a href="{% url 'login' %}">Login</a>
    <img src="{% static 'blog/images/welcome.jpg' %}" alt="Welcome" width="600" height="300">
</body>
</html>
```

#### Integrating a Logout Link

Similar to the login link, a logout link offers users the ability to terminate their session directly from the blog's interface.
Example: Adding a Logout Link

Assuming the presence of a logout feature within the blog, add a logout link to the template displaying individual blog posts for authenticated users.

Location for Addition: `post_detail.html` within the blog app.

Implementation Code:

Add the following line at a suitable location within the template:

```html
<a href="{% url 'logout' %}">Logout</a>
```

This link utilizes the `{% url %}` tag to dynamically direct users to the logout view, effectively logging them out.

Consideration for Protected Pages:

For pages requiring user authentication, such as a dashboard or a page for creating new blog posts, ensure the inclusion of logout links to maintain a consistent user experience across the application.

By embedding login and logout links within the blog application's templates, users gain the convenience of easily accessing authentication functionalities, thereby enhancing the overall usability and security of the application. This method of integration aligns with best practices for creating user-friendly web interfaces.

## Protecting Views

### Configuration in Settings

For the blog application, it's crucial to direct unauthenticated users to a login page when they attempt to access restricted areas. This is achieved by specifying a login URL in the project's settings.

### Settings Update

Modify the `settings.py` file to include the path for the login URL:

```python
# Authentication
LOGIN_URL = '/login/'
```

This setting ensures users are redirected to the login page if they try to access views that require authentication.

### Securing Views

Views within the blog application need to be protected to ensure only authenticated users can access certain functionalities, such as creating or editing blog posts.

### Class-Based Views (CBVs)

The blog application utilizes class-based views for listing blog posts and displaying post details. To protect these views, the `LoginRequiredMixin` is used.
Securing BlogListView and BlogDetailView

In `blog/views.py`, import `LoginRequiredMixin` from Django's authentication mixins and apply it to the class definitions:

```python
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
```

### Function-Based Views (FBVs)

For function-based views, such as a view displaying a form for new post creation, the `login_required` decorator is utilized to enforce authentication.

Example: Protecting the New Post View

To secure a view responsible for adding new posts in `blog/views.py`, use the `login_required` decorator:

```python
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/new_post.html', {'form': form})
```

### Behavior of Protected Views

When an attempt is made to access these protected views without being authenticated, Django redirects the user to the login page specified by `LOGIN_URL` in `settings.py`. This mechanism enhances the blog application's security by ensuring that only authorized users can create, edit, or view detailed blog posts.

By implementing view protection through `LoginRequiredMixin` for class-based views and the `login_required` decorator for function-based views, the blog application effectively restricts access to certain functionalities to authenticated users only. This approach not only secures sensitive content but also provides a seamless user experience by redirecting unauthorized access attempts to the login page.

## Task

### Overview

The objective is to incorporate authentication functionalities, including login and logout features, into the Recipe application, enhancing its security and user experience.

### Directions

Authentication Setup

1. Login Feature Implementation:
    - Develop a login view to handle user authentication.
    - Craft a login template to present the authentication form.
    - Configure URL mapping for the login view to ensure it's reachable at “<http://127.0.0.1:8000/login/”>.
    - Embed a login link or button on the homepage, directing users to the login form.
    - Choose a specific page to direct users post-login, ensuring it requires user authentication for access.

2. View Protection:
    - Determine the views or pages within the application that should be accessible only to authenticated users.
    - Modify these views to include authentication checks, redirecting unauthenticated access attempts to the login page.
    - Verify the functionality by accessing the URLs of protected views, ensuring redirection to the login page occurs for unauthenticated requests.

3. Logout Functionality:
    - Introduce a logout option on all authenticated pages.
    - Create a view and template named success.html, displaying a message indicating successful logout along with an option to log back in.
    - Envision and add additional content or features to success.html to enhance its utility and appeal.

4. Application Testing:
    - Utilize the terminal to initiate the server, navigating through the application to simulate a typical user journey from homepage access to logout.
    - Document this journey using a screen recording tool, capturing the login process, authentication form interaction, redirection to a protected page, and the logout process concluding with the success.html page.

5. Code Submission:
    - Update the Recipe application codebase on GitHub, ensuring all new changes are pushed to the repository.

6. Sharing for Review:
    - Share the screencast video and the GitHub repository link with a mentor for feedback and review.

Submission Requirements

- A screencast video showcasing the user journey through login and logout processes within the Recipe application.
- Updated codebase pushed to the designated GitHub repository, reflecting all implemented authentication features and view protections.

Goal

The successful integration of login and logout functionalities, coupled with the protection of specific views within the Recipe application, aims to reinforce application security, personalize user experience, and demonstrate proficiency in managing user authentication within Django applications.

## Learning Journal

- The included learning journal reflects on the experiences and learning outcomes from this exercise.

## Summary

In this comprehensive lesson, participants delved into the intricacies of user authentication within Django applications, mastering the creation, management, and protection of user sessions. The journey encompassed learning how to utilize GET and POST methods for form submissions, integrating Django's built-in authentication system for login and logout functionalities, and employing mechanisms to restrict access to certain views solely to authenticated users. The practical application of these concepts was demonstrated through the enhancement of a blog application, ensuring a secure and personalized user experience by making specific content and functionalities accessible only after successful user authentication. This exercise not only fortified participants' understanding of Django's robust authentication capabilities but also equipped them with essential skills to elevate the security and user management of their web applications.
