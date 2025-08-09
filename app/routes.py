""" 
This file contains the routes and route handlers for the application.It contains the 
view functions for the routes "/" and "/index" endpoints

@author: vasulu
@version: 0.4
@date: 2025-aug-09
"""
from app import app
from flask import render_template
@app.route('/')
@app.route('/index')

# simple view function that returns a string "Hello, World!"
def index():
    user = {"username": "vasulu"}
    posts = [
        {
            "author": {"username": "ripper"},
            "body": "This is first post"
        },
        {
            "author": {"username": "shadow"},
            "body": "This is the second post"
        }
    ]
    return render_template("index.html",user=user,posts=posts)