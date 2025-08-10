""" 
This file contains the routes and route handlers for the application.It contains the 
view functions for the routes "/" and "/index" endpoints

@author: vasulu
@version: 0.4
@date: 2025-aug-09
"""
from app import app
from flask import render_template,flash,redirect
from app.forms import LoginForm
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

@app.route("/login",methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me={form.remember_me.data}")
        return redirect("/index")
    return render_template("login.html",title="Sign In",form=form)