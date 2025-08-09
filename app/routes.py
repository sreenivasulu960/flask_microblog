""" 
This file contains the routes and route handlers for the application.It contains the 
view functions for the routes "/" and "/index" endpoints

@author: vasulu
@version: 0.1
@date: 2025-aug-09
"""
from app import app

@app.route('/')
@app.route('/index')

# simple view function that returns a string "Hello, World!"
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
    </html>
"""