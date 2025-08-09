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
