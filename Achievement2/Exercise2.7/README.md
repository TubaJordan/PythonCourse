# Exercise 2.7 Data Analysis and Visualization in Django

## Introduction

This lesson focuses on extending the capabilities of web applications developed using Django by incorporating data analysis and visualization features. These features enable applications to interact dynamically with the data, presenting it in a more insightful and accessible manner. The lesson utilizes a fictitious blog application as an example to demonstrate the concepts.

## Learning Goals

- Engage with elements of two-way communication such as creating forms, obtaining input from users, and creating buttons.
- Implement search and visualization features including reports and charts.
- Utilize Django's QuerySet API, pandas for data manipulation, and matplotlib for data visualization.

## Search for Records

### Overview

In the context of a fictitious blog application, the goal is to enable users to search for blog posts using keywords. This functionality extends the blog's capabilities by allowing for interactive data analysis and visualization, such as displaying blog analytics in tables and charts.

### Process Breakdown

User Form to Search Blog Posts

The first step involves creating a user-input form to facilitate the search for blog posts. This form will be accessible on a dedicated search page, which has been secured through user authentication in previous exercises.

**Implementation**

- **Form Creation:** A form is designed to capture keywords as input from the users. This can be achieved by defining a Django form with a CharField for the keywords.

- **Template Update:** The search page template is updated to include the form, allowing users to input the keywords they wish to search for.

Displaying Search Records

Upon receiving input from the user, the application will search the database for blog posts matching the keywords and display the results.

Steps

1. **Search Functionality:** Utilizing Django's QuerySet API, the application filters the blog posts based on the keywords provided by the user.

2. **Results Presentation:** The filtered records are presented in a table format on the search page, enabling users to review the blog analytics.

Visualization and Charting

To enhance data analysis, the application will also display charts based on the search results, such as a pie chart comparing the views of different blog posts.

**Implementation**

- **Chart Generation:** Using matplotlib, the application generates charts to visually represent the blog analytics. This could involve creating bar charts, pie charts, or line charts depending on the data's nature.

- **Template Update:** The search page template is further updated to include the generated charts, providing a comprehensive view of the blog analytics to the users.

### Data Preparation

Before implementing the above functionalities, sample blog posts and related analytics are added to the Django admin dashboard. This ensures that there is data to search and visualize.

Adding Blog Posts and Analytics

Blog posts and their analytics are added to the admin dashboard, simulating real-world data for testing the search and visualization features.

### Conclusion

The incorporation of search functionality and data visualization into the blog application significantly enhances the user experience. By allowing for easy access and analysis of blog analytics, the application not only becomes more interactive but also provides valuable insights into the blog's performance.

## Creating a User-Input Form

The creation of a user-input form in a Django application involves a three-step process, aimed at enabling users to search for specific blog posts. This example utilizes the blog application's analytics module to illustrate the process.

### Step 1: Create Form `analytics/forms.py`

The initial step requires creating a form in the analytics application to specify the fields for searching blog analytics. This involves:

1. **Form Creation:** A new file named `forms.py` is created within the `analytics` directory.
2. **Importing Django Forms:** The Django forms library is imported to utilize its form creation capabilities.
3. **Defining Form Fields:** The form, `BlogSearchForm`, includes fields for inputting keywords and selecting a chart type for data visualization.

```python
from django import forms

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart')
)

class BlogSearchForm(forms.Form):
    keywords = forms.CharField(max_length=120)
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
```

### Step 2: Update View in analytics/views.py

The `records` view within `analytics/views.py` is updated to incorporate the form, enabling user input to be captured and processed:

1. **Importing the Form:** The `BlogSearchForm` is imported from `analytics/forms.py`.
2. **Updating the View:** The `records` function-based view is modified to instantiate the `BlogSearchForm` and pass it to the template through the context.

```python
from django.shortcuts import render
from .forms import BlogSearchForm

def records(request):
    form = BlogSearchForm(request.POST or None)
    context = {'form': form}
    return render(request, 'analytics/records.html', context)
```

### Step 3: Update Template `analytics/records.html`

The `analytics/records.html` template is edited to display the form, allowing users to input their search criteria:

1. **Form Display:** The template includes the form, utilizing Django's template language to render the form fields and a submit button.
2. **CSRF Protection:** The `{% csrf_token %}` tag is included for security against Cross Site Request Forgery attacks.

```html
<h1>Search for blog analytics</h1>
<hr>
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">search</button>
</form>
```

Upon completing these steps and running the Django development server, the search page will display the updated form, enabling users to search for blog analytics based on keywords and visualize the data through selected chart types.

## Implementing Search Functionality and Displaying Search Records

The process of implementing search functionality and displaying search records in a Django application involves capturing user input, querying the database, and processing the data for display.

### Step 1: Read User Data from the Form

Within the `analytics/views.py` file, the application reads data entered into the form by the user. This involves checking if the form has been submitted (via a POST request) and then extracting the input data.

```python
def records(request):
    form = BlogSearchForm(request.POST or None)
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        chart_type = request.POST.get('chart_type')
        print(keywords, chart_type)
    context = {'form': form}
    return render(request, 'analytics/records.html', context)
```

### Step 2: Extracting Data from the Database using QuerySet

The application uses Django's QuerySet API to access the database and filter records based on the user's input. This step involves querying the `BlogPost` model to find posts that match the specified keywords.

```python
from .models import BlogPost

def records(request):
    form = BlogSearchForm(request.POST or None)
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        chart_type = request.POST.get('chart_type')
        qs = BlogPost.objects.filter(content__icontains=keywords)
        print(qs.values())
    context = {'form': form}
    return render(request, 'analytics/records.html', context)
```

### Step 3: Convert QuerySet to Pandas DataFrames for Data Processing

For further data processing and to facilitate the generation of charts, the filtered QuerySet is converted into a pandas DataFrame. This step requires the installation of pandas and updating the view to process the QuerySet accordingly.

```python
import pandas as pd

def records(request):
    form = BlogSearchForm(request.POST or None)
    blog_df = None
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        chart_type = request.POST.get('chart_type')
        qs = BlogPost.objects.filter(content__icontains=keywords)
        if qs.exists():
            blog_df = pd.DataFrame(qs.values())
            blog_df['post_id'] = blog_df['post_id'].apply(get_posttitle_from_id)
            blog_df = blog_df.to_html()
    context = {'form': form, 'blog_df': blog_df}
    return render(request, 'analytics/records.html', context)
```

### Displaying the Data

The `analytics/records.html` template is updated to display the search form and the results. The results are shown in a table format, rendered from the DataFrame converted to HTML.

```html
<h1>Search for blog analytics</h1>
<hr>
<form action="" method="POST">
    {% csrf_token %}
    {{ form }}
    <button type="submit">search</button>
</form>

{% if blog_df %}
    {{ blog_df|safe }}
{% else %}
    <h3>no data</h3>
{% endif %}
```

This implementation enables the application to take input from a form, query the database for matching blog posts, and display the analytics. It utilizes Django forms, views, models, and templates, along with pandas for data processing and visualization preparation.

## Visualization and Charting

Implementing chart visualization based on user input enhances the data analysis capabilities of the application. This section covers installing matplotlib, creating charting functions, and updating the application to display charts.

### Installing matplotlib

matplotlib is a Python library used for creating static, animated, and interactive visualizations. Install it using the following command:

```bash
pip install matplotlib
```

### Updating `analytics/utils.py` for Charting Functions

First, create necessary imports and define functions for handling chart images.

```python
from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(6,3))
    if chart_type == '#1':
        # Assume 'views' and 'dates' are columns in 'data'
        plt.bar(data['dates'], data['views'])
    elif chart_type == '#2':
        labels = kwargs.get('labels')
        plt.pie(data['views'], labels=labels)
    elif chart_type == '#3':
        plt.plot(data['dates'], data['views'])
    else:
        print('unknown chart type')
    plt.tight_layout()
    chart = get_graph()
    return chart
```

### Integrating Charting Functionality in `analytics/views.py`

Implement chart generation based on user input and data processing in `analytics/views.py`.

```python
from django.shortcuts import render
from .forms import BlogSearchForm
from .models import BlogPost
import pandas as pd
from .utils import get_posttitle_from_id, get_chart

def records(request):
    form = BlogSearchForm(request.POST or None)
    blog_df = None
    chart = None
    if request.method == 'POST':
        keywords = request.POST.get('keywords')
        chart_type = request.POST.get('chart_type')
        qs = BlogPost.objects.filter(content__icontains=keywords)
        if qs.exists():
            blog_df = pd.DataFrame(qs.values())
            blog_df['post_id'] = blog_df['post_id'].apply(get_posttitle_from_id)
            chart = get_chart(chart_type, blog_df, labels=blog_df['dates'].values)
            blog_df = blog_df.to_html()
    context = {'form': form, 'blog_df': blog_df, 'chart': chart}
    return render(request, 'analytics/records.html', context)
```

### Displaying Charts in `analytics/records.html`

Enhance the template to include the generated chart images.

```html
{% if blog_df %}
    {{ blog_df|safe }}
    <br>
    <img src="data:image/png;base64, {{ chart|safe }}">
{% else %}
    <h3>no data</h3>
{% endif %}
```

This implementation enables users to visualize blog analytics through charts, providing a richer data analysis experience.

## Task Overview for Recipe Application Enhancement

### Implement Search for Recipes

- Conceptualize search criteria, output format, and document these in "Task-2.7".
- Develop a form for inputting search criteria.
- Utilize Django's QuerySet API to fetch data based on the search criteria.
- Convert QuerySets to pandas DataFrames for data manipulation.
- Present search results in a tabulated format, ensuring recipe links are clickable.
- Introduce wildcard search capabilities for more flexible query matching.

### Implement Show-All Feature (Optional)

- Provide functionality to display all recipes without applying search filters.

### Data Visualization

- Document visualization ideas in "Task-2.7", focusing on bar, pie, and line charts.
- Install matplotlib for chart generation.
- Develop and integrate charting functionality based on the documented visualization concepts.

### Write Tests

- Apply testing methodologies to new forms and views, creating tests for validation, pagination, and security.
- Execute tests, capturing the output in a screenshot named "test-outcome.jpg".

### Run Server and Capture Output

- Document the user journey from homepage to logout, including navigation and search actions.
- Record the server execution and user interaction, taking screenshots or creating a screencast named "user-journey.mp4".

### Upload to GitHub

- Organize and upload the "Task-2.7" document, screenshots, and code to the designated GitHub repository.
- Share the repository links with the mentor for review.

## Learning Journal

- The included learning journal reflects on the experiences and learning outcomes from this exercise.

## Summary

This lesson illustrated how to extend a Django application with data analysis and visualization capabilities. By implementing search functionality and data visualization, the application not only becomes more interactive but also provides users with deeper insights into the data.
