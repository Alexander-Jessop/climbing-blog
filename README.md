# Climbing Blog

<div align="right">
<span> 
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT">
  </a>
</span>
<span>
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" alt="Version Badge">
</span>
</div>

## Table of Contents

- [Project Description](#project-description)
- [Getting Started](#getting-started)
- [Running the Project Locally](#running-the-project-locally)
- [Logging In to the Admin Panel](#logging-in-to-the-admin-panel)
- [Credentials](#credentials)
- [Assignment Requirements](#assignment-requirements)
  - [Assignment 1](#assignment-1)
  - [Assignment 2](#assignment-2)
  - [Assignment 3](#assignment-3)
  - [Assignment 4](#assignment-4)
  - [Assignment 5](#assignment-5)

## Project Description

This blog project is an assignment under the Sheridan College -- Ontarion Bright Learn umbrella. It serves as a platform for sharing climbing experiences, insights, and knowledge. Whether you're an avid climber or just curious about the sport, the blog provides valuable content for climbers of all levels. <br>

**View the Live Project:** You can view the live project at https://sheridan-alexander-jessop-a0fc086eb075.herokuapp.com/. <br>

[Back to top](#table-of-contents)

## Getting Started

To get started with this project, you can follow these steps:

1. Clone the Repository: Start by cloning this repository to your local machine:
   ```bash
   git clone https://github.com/Alexander-Jessop/climbing-blog.git
   ```
2. Navigate to the Project Directory:

   ```bash
   cd climbing-blog
   ```

3. Set Up a Virtual Environment: It's a good practice to work within a virtual environment to isolate your project dependencies. You can create one using Python's built-in venv module:

   ```bash
   py -m venv venv
   ```

4. Activate the Virtual Environment:

   ```bash
   source venv\Scripts\activate
   ```

5. Install Project Dependencies: Use pip to install the required Python packages listed in the requirements.txt file:

   ```bash
   pip install -r requirements.txt
   ```

   [Back to top](#table-of-contents)

## Running the Project Locally

To run the Climbing Blog locally, make sure you've completed the "Getting Started" steps and have activated your virtual environment. Then, you can start the Django development server:

```bash
py manage.py runserver
```

The development server will be accessible at http://127.0.0.1:8000/ in your web browser. You can explore the climbing blog and its features locally.

## Logging In to the Admin Panel

To access the admin panel, you'll need to create a superuser account. You can do this by running the following command:

```bash
py manage.py createsuperuser
```

You'll be prompted to enter a username, email address, and password for your superuser account. Once you've created a superuser, you can log in to the admin panel.

[Back to top](#table-of-contents)

## Credentials

A superuser has already been created for the instructor to access the admin panel. The credentials are as follows:

- Username: instructor
- Password: DjangoRocks1!

[Back to top](#table-of-contents)

## Assignment Requirements

### Assignment 1

Assignment - Create & deploy a Django project

In this course, you will create a fully-functional blog which using Python and the Django framework. Each assignment will add new features to this project to ultimately produce a fully-featured web app. This assignment lays the foundation for the entire course and all subsequent assignments.

Use the mysite project built in this module as reference.
Requirements

Pick a topic for a blog. It could be a personal blog, or related to a special topic or interest.

    Set up your GitHub account if you have not already

    Create a new Django project - different than the one used in the course modules. In your ~/PycharmProjects folder, run:

    $ django-admin startproject <project-name> .

    Use snake_case naming for the Django project.

    Use the standard, out-of-box, sqlite3 database (db.sqlite3) to store data.

    Create an index view (at /) with an accompanying test to demonstrate a 200 HTTP response status code.

    Your app will be run locally on your (and the instructor's) machine. The website must run using python manage.py runserver
    Share github repo (public) for this assignment with the instructor

Evaluation

This assignment is graded using the following criteria, each is worth 3 points.
Points Criteria
/ 3 The project contains a .gitignore file suitable for Python projects
/ 3 Repository contains a functional Django project with a README file containing a short description of the project
/ 3 The Django project has an index route at the root path: /
/ 3 The project has a configured test suite and a test for the index view at the root path: /
/ 3 The app is configured to connect to the local sqlite3 database in the settings.py file
/ 3 The project has a valid requirements.txt file containing the libraries used in this project
/ 3 The Django admin is functional and can be accessed by the instructor

Total: / 21
Grade ( / 3 ) Explanation of the Criteria
3 Criteria is met and all functionality is present
2 Criteria is mostly met with some gaps in functionality
1 Criteria is mostly unsatisfied or not functional, though some elements are present
0 Criteria is not met. No visible attempt to satisfy it exists
Code style

1% will be deducted from the final grade for every code style violation in the project on the last commit.

Code style is verified using pylint. To run pylint locally, install:

$ pip install pylint pylint-django

You should already have Pylint enabled in your code editor, but it can also be run from the command line. Run this command from the root of your project from bash:

$ find . -name '\*.py' | xargs pylint

Submission

Submit in the assignment dropbox the full URLs to the GitHub repository link
Running the code

The instructor will run your code using these steps. Make sure your project is compatible.

    Checkout your code from the provided public Github repository.
    Install any new pip modules by running: pip install -r requirements.txt
    Apply any migrations to the local database: python manage.py migrate
    Create a superuser for Django Admin: python manage.py createsuperuser
    Start the website: python manage.py runserver
    Test your website by navigating to: http://127.0.0.1:8000/
    Execute your unit test(s): pytest

requirements.txt

In order to run your code for marking, the instructor's computer must have the required packages to run your code. The packages below will be included as a part of the course standard. Any additional packages you import must also be added to requirements.txt.

[Back to top](#table-of-contents)

### Assignment 2

Part 1 – Module 3: In Practice

**Total Points:** 30

The main objective of this section is to implement the code from Module 3.

Create a Model for Blog Posts (Post model)
**Total Points:** 18

Your task is to create a `Post` model with the properties described in the table below:

| Points | Name      | Required | Description                                                           |
| ------ | --------- | -------- | --------------------------------------------------------------------- |
| 2      | title     | x        | Post title                                                            |
| 2      | content   |          | Article's content                                                     |
| 2      | author    | x        | A user can create multiple blog posts, but a post has only one author |
| 2      | created   |          | A timestamp set only on creation                                      |
| 2      | updated   |          | A timestamp that updates each time the object is saved                |
| 2      | status    | x        | Blog's status: published or draft (default state = draft)             |
| 2      | published |          | Timestamp marking when the blog changed from draft to published       |
| 2      | slug      | x        | Label used for URL, prepopulate with the value in 'title'             |
| 2      | topics    |          | Each post can have multiple topics                                    |

Create a Model for Topics (Topic model)
**Total Points:** 4

You need to create a `Topic` model with the properties described below:

| Points | Name | Required | Description                               |
| ------ | ---- | -------- | ----------------------------------------- |
| 2      | name | x        | Name of the topic (no duplicates allowed) |
| 2      | slug | x        | Prepopulate with the value in 'name'      |

Register Models and Add Data

- **Total Points:** 4
- Register all models to Django Admin.
- Use the guidelines below to create data:
  - Minimum of 10 posts in total
  - At least 3 authors, assigned randomly to posts
  - At least 4 published posts
  - At least 2 posts should have multiple topics

Display and Search Fields

- **Total Points:** 4
- Display the following fields for `Post` and `Topic`:
  - **Post:** 'title', 'created', 'update'; Sort by 'created' field
  - **Topic:** 'name', 'slug'
- Enable search for Posts using:
  - 'title'
  - 'author\_\_username'
  - 'author\_\_first_name'
  - 'author\_\_lastname'

Part 2: Create a model

**Total Points:** 30

- **(3 Points)** Create a new `Comment` model under the blogs app where visitors to your blog can write comments on your posts.
- **(21 Points)** This model will contain the following fields:

| Points | Name     | Required | Description                                                                              |
| ------ | -------- | -------- | ---------------------------------------------------------------------------------------- |
| 3      | post     | x        | A relationship to the Post model. Set `related_name='comments'` on the field             |
| 3      | name     | x        | Name of the person making the comment                                                    |
| 3      | email    | x        | Email address for the commenter                                                          |
| 3      | text     | x        | A field for the actual comment. Consider limiting characters to prevent lengthy comments |
| 3      | approved |          | Boolean field for comment moderation. If true, the comment will be visible, else hidden  |
| 3      | created  |          | Timestamp automatically set on creation                                                  |
| 3      | updated  |          | Timestamp updated each time the object is saved                                          |

Note: Use the appropriate model field type for each field. Fields marked as "required" mean that the user must provide a value – null or empty values are not allowed.

- **(3 Points)** Customize the `str()` value for the `Comment` model
- **(3 Points)** Set the default order of the `Comment` model to return objects sorted by the created timestamp in reverse chronological order.

**Evaluation for Part 2:**

- 3 – Fully met requirements with correct data types, defaults, and attributes
- 2 – Mostly met requirements, but some attributes might be missing or slightly incorrect
- 1 – Mostly unmet requirements with incorrect data types, attributes, or functionality
- 0 – Requirements not met

Part 3: Expose the model in the Django admin

**Total Points:** 14

1. Expose the `Comment` model defined in part 1 in the Django admin. The admin should have the following settings configured:

   - The list display should be customized
   - The comment list should be searchable
   - The list should be filterable by approved records and hide those that are not approved

2. Create an inline model admin for the `Comment` model and register it on the Post admin class. This way, comments on a post can be viewed from the post's detailed view.

   - Display the name, email, comment text, and approved checkbox
   - Don't show any extra form fields
   - Make the name, text, and email fields read-only

   References:

   - [Django Inline Model Admin](https://docs.djangoproject.com/en/4.1/ref/contrib/admin/#inlinemodeladmin-objects)
   - [Implementing Comment System](https://www.samuelledtke.com/blog/implement-comment-system-blog-application-django/)

Part 4: Writing queries

**Total Points:** 27

- Download the attached Python file.
- There are 9 questions to complete, with each question worth 3 marks, making a total of 27 points.
- Practice building queries by creating data in the Django admin and using Django shell to experiment and build your queries. If you find a solution, you can likely use it to answer multiple questions.
- Submit the python file via Dropbox that includes queries which should work on your deployed Heroku app (you can paste the queries in the text box of Dropbox)

[Back to top](#table-of-contents)

### Assignment 3

#### Assignment Description

For this assignment, you are tasked to style your base template using CSS. You will create a look & feel that best suits your taste and the content of your site. The design portion is a creative exercise, but technical considerations covered in this module will be evaluated.

#### Tasks

1. Create a base template with at least one content block which is styled using CSS.

2. Create a home page (view & template) which extends the base template.

3. Render the list of topics contained in the Topic model in a sidebar.

   - Include the total number of posts for each topic (hint: use query annotations). You may display topics without posts – they will have a count of 0.
   - Order the list by the most popular topic (most posts).
   - Limit to the top 10 topics.

4. Ensure that there is sample data in your site's database to appropriately render content.

#### Evaluation Criteria

- Base template structure & design: /3
- At least one content block which is styled using CSS: /3
- Create a home page (view & template) which extends the base template: /3
- Render the list of topics: /3
- Ensure that there is sample data in your site's database to appropriately render content: /3

#### Grade Explanation

- 3: Criteria is met and all functionality is present.
- 2: Criteria is mostly met with some gaps in functionality.
- 1: Criteria is mostly unsatisfied or not functional, though some elements are present.
- 0: Criteria is not met. No visible attempt to satisfy it exists.

[Back to top](#table-of-contents)

### Assignment 4

This assignment continues to build upon your blog project.

In this assignment, we will build pages for Topics. We will create a list view for all the topics which will link to detailed views. The detailed view will consist of a list of posts which are about the provided topic.

#### Requirements

1. **Move global queries to context_processors**

   Move the top topics list query to the `blog.context_processors.base_context` function created in this module. This will expose the top topics on all the site pages.

2. **Build a topic ListView**

   Create a `ListView` that renders all topics defined in the database.

   - Define the URL at `/topics/`. Note the trailing slash.
   - List the topics alphabetically
   - Link the topic to the topic detail view
   - Set the page title block

3. **Build a topic DetailView**

   Create a `DetailView` for the topic

   - Define the URL as `/topics/<slug:slug>/`. Note the trailing slash.
   - Render a list of posts filtered by this topic. This should be formatted like the post previews on the home & post list pages.
   - Only published posts should appear
   - Posts should be ordered by latest to earliest published date

   ##### Hints:

   - Overriding the `get_context_data()` method of the `DetailView` allows the customization of the context variables to the template
   - To access the topic object from the `DetailView`, use the `self.get_object()` method. Alternatively, you can get the `pk` value from `self.kwargs`.
   - Can you use an existing template component/partial to render the post previews?

4. **Define `get_absolute_url` on the Topic model**

   Define and return the appropriate URL for the topic object.

   _Hint:_ use the `reverse()` function to construct the string.

5. **Link topics to their detailed page on the site**

   The topics sidebar:

   - Add a link for each top topic which will bring the user to the topic detail view using the `get_absolute_url`.
   - Add a link to "view all" topics

   The main navigation:

   - Add a link to "Topics"

   The post detail page:

   - Each post has related topics. List these on the post detail page
   - Link each topic to their pages

#### Evaluation

##### Grading Criteria

| Grade | Criteria                           |
| ----- | ---------------------------------- |
| 5     | Context processor                  |
| 5     | Topic list view                    |
| 5     | Topic detailed view                |
| 5     | Define `get_absolute_url`          |
| 5     | Links to topic list & detail pages |

##### Grade ( / 5 )

| Grade | Explanation of the Criteria                                                        |
| ----- | ---------------------------------------------------------------------------------- |
| 5     | Criteria is met and all functionality is present, accompanied with tests           |
| 3     | Criteria is mostly met with some gaps in functionality                             |
| 1     | Criteria is mostly unsatisfied or not functional, though some elements are present |
| 0     | Criteria is not met. No visible attempt to satisfy it exists                       |

[Back to top](#table-of-contents)

### Assignment 5

This assignment adds another feature to your blog website which will collect and save user data and an image to the database as part of a hypothetical photo contest.

Add a link to the contest in the main navigation bar which will take users to a page describing the contest and containing a form in which they can upload their information and photo submission.

The required pieces of information to gather from the user are

    Their name
    Their email address
    An image

In addition to the information gathered, also save the date & time of the submission.

Register the model in the Django admin and customize its presentation so it can be sorted, filtered, etc. by a staff member of your site.

#### Hints:

- To upload files in a form you must set the encoding to "multipart/form-data" by adding the following to the <form> tag: <form enctype="multipart/form-data" ... >

#### Evaluation

##### Grading Criteria

| Grade | Criteria                                                 |
| ----- | -------------------------------------------------------- |
| 5     | Upload form                                              |
| 5     | Django admin                                             |
| 5     | Template presentation, presence of links to contest page |

##### Grade ( / 5 )

| Grade | Explanation of the Criteria                                                        |
| ----- | ---------------------------------------------------------------------------------- |
| 5     | Criteria is met and all functionality is present, accompanied with tests           |
| 3     | Criteria is mostly met with some gaps in functionality                             |
| 1     | Criteria is mostly unsatisfied or not functional, though some elements are present |
| 0     | Criteria is not met. No visible attempt to satisfy it exists                       |

[Back to top](#table-of-contents)
