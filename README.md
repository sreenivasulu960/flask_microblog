# MicroBlog

This project for learning flask and python and we are going to build it step by step.

## Pre-requisties

### Step-1 create virtual environment

```bash
    python -m venv myvenv
```

### Step-2 activate virtual environment

If you are using windows use the command

```bash
    myvenv\Scripts\activate
```

If you are using linux or mac use the command

```bash
    source myvenv/bin/activate
```

### Steo-3 install the requirements.txt

```bash
    pip install -r requirements.txt
```

## How to run

To run the application run the command

```bash
    flask run
```

and then open the browser and go to http://127.0.0.1:5000/

## Source

I have followed the blog written by miguel grinberg. here is the link for the blog(https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

## Stage-1: Create a simple web page

In this stage we are going to create a simple flask application that returns a hello world string

## Stage-2: Returning html

In this stage we extend our application to return a html code instead of a string. We are going to modify our view function to return the below html code. As of now we have hardcoded the user details as dictionary

```python
def index():
    user = {"username": "vasulu"}
    return f"""
    <html>
        <head>
            <title>Home - Microblog</title>
        </head>
        <body>
            <h1>Hello, {user['username']}!</h1>
        </body>
    <
```

**Debug mode:** When you run the application using `flask run` it will run with debug mode off so if you make changes to the code you have to restart the application. But if you run the application using `flask run --debug` it will run with debug mode on and it will automatically restart the application when you make changes to the code.

Instead of mentioning --debug flag every time we can mention it in .flaskenv file and then run the application using `flask run` command.

```
# .flaskenv
FLASK_APP = microblog.py
FLASK_DEBUG = 1
```

## Stage-3: using templates

In this stage we are going to use templates to render the html code. We are going to create a templates folder and inside that folder we are going to create a index.html file and then we are going to use the render_template function to render the html code.

```python
# app/routes.py
from flask import render_template

@app.route('/')
def index():
    user = {"username": "vasulu"}
    return render_template('index.html',title="Home", user=user)
```

We have 3 sub stages in this stage
**stage3.1 variables** -> In this we are going to use the variables in the jinja template (index.html) to display the title and user details

**stage3.2 conditonal statements -> In this stage we are going to use the condtional statements to handle the case where the title is not passed to the template**

**stage3.3 loops -> In this stage we are going to use the loops to display the list of posts**

## Stage4: Template inheritance

lets try to add a navigation bar to our page. since the navigation bar can be on multiple pages we need to repeat the same code in the multiple pages instead of that we can create a base.html file and then inherit it in the other pages.so we are going to create a new file in templates base.html and add the functionality of inheriting the base.html file in index.html

## Stage5: Login Form

lets add a login form to our page. we are going to create a new file in templates login.html and add the functionality of login form in it.For this stage we are going to Flask-WTF extension so we can install it using below command

```bash
    pip install flask-wtf
```

and then we are going to create a new file in app/forms.py and add the functionality of login form in it. we are going to create the form and its fields as python class
